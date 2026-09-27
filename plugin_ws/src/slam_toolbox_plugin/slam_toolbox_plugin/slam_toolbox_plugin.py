"""
SlamPlugin wrapper around the ROS slam_toolbox package.

slam_toolbox is a full standalone ROS node: it consumes LaserScan + TF
directly over topics rather than exposing a per-frame call API, so this
wrapper manages it as a subprocess instead of doing the SLAM computation
in-process. Pose/trajectory are read back the same way any downstream
consumer would: by looking up the map -> base_link transform slam_toolbox
publishes.
"""
import subprocess
import time
from typing import Any, Dict, Optional

from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from nav_msgs.msg import Path
from rclpy.node import Node
from rclpy.time import Time
from slam_plugin_base.slam_plugin_base import SlamPlugin
from tf2_ros import (
    Buffer,
    ConnectivityException,
    ExtrapolationException,
    LookupException,
    TransformListener,
)


class SlamToolboxPlugin(SlamPlugin):

    def __init__(self):
        super().__init__()
        self.plugin_name = "slam_toolbox_plugin"
        self._process: Optional[subprocess.Popen] = None
        self._tf_buffer: Optional[Buffer] = None
        self._tf_listener: Optional[TransformListener] = None
        self._trajectory = Path()

    def initialize(self, node: Node, config_path: str) -> bool:
        self.node = node

        if not config_path:
            self.status = "Error: no config_path provided"
            return False

        try:
            self._process = subprocess.Popen(
                [
                    "ros2", "run", "slam_toolbox", "sync_slam_toolbox_node",
                    "--ros-args", "--params-file", config_path,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
        except OSError as e:
            self.status = f"Error: failed to launch slam_toolbox: {e}"
            return False

        # slam_toolbox fails fast (missing package, bad params) - give it a
        # moment and check it didn't immediately exit before declaring success.
        time.sleep(0.5)
        if self._process.poll() is not None:
            output = self._process.stdout.read().decode(errors="replace") if self._process.stdout else ""
            self.status = f"Error: slam_toolbox exited immediately (rc={self._process.returncode}): {output[-500:]}"
            return False

        # slam_toolbox is a managed lifecycle node: it starts "unconfigured"
        # and does nothing (no /scan subscription) until explicitly driven
        # through configure -> activate.
        if not self._set_lifecycle_state("configure"):
            return False
        if not self._set_lifecycle_state("activate"):
            return False

        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, node)
        self._trajectory.header.frame_id = "map"

        self.config["config_path"] = config_path
        self.initialized = True
        self.status = "Running"
        return True

    def _set_lifecycle_state(self, transition: str, retries: int = 10, delay: float = 1.0) -> bool:
        last_error = ""
        for _ in range(retries):
            try:
                result = subprocess.run(
                    ["ros2", "lifecycle", "set", "/slam_toolbox", transition],
                    capture_output=True, text=True, timeout=10.0,
                )
            except (OSError, subprocess.TimeoutExpired) as e:
                last_error = str(e)
                time.sleep(delay)
                continue

            if result.returncode == 0:
                return True
            last_error = result.stderr.strip() or result.stdout.strip()
            time.sleep(delay)

        self.status = f"Error: lifecycle transition '{transition}' failed: {last_error}"
        return False

    def process_image(self, image_msg, timestamp: float) -> None:
        # slam_toolbox consumes LaserScan + TF directly over ROS topics; it
        # is not driven by per-frame pushes, so this is intentionally a no-op.
        pass

    def process_imu(self, imu_msg, timestamp: float) -> None:
        # Same as process_image: slam_toolbox does not take IMU input directly.
        pass

    def get_current_pose(self) -> Optional[PoseWithCovarianceStamped]:
        if self._tf_buffer is None:
            return None

        try:
            transform = self._tf_buffer.lookup_transform(
                "map",
                "base_link",
                Time(),
            )
        except (LookupException, ConnectivityException, ExtrapolationException) as e:
            self.node.get_logger().warn(
                f"slam_toolbox_plugin: could not look up map -> base_link transform: {e}",
                throttle_duration_sec=5.0,
            )
            return None

        pose = PoseWithCovarianceStamped()
        pose.header = transform.header
        pose.pose.pose.position.x = transform.transform.translation.x
        pose.pose.pose.position.y = transform.transform.translation.y
        pose.pose.pose.position.z = transform.transform.translation.z
        pose.pose.pose.orientation = transform.transform.rotation

        self._trajectory.header.stamp = transform.header.stamp
        self._append_to_trajectory(transform)

        return pose

    def _append_to_trajectory(self, transform) -> None:
        pose_stamped = PoseStamped()
        pose_stamped.header = transform.header
        pose_stamped.pose.position.x = transform.transform.translation.x
        pose_stamped.pose.position.y = transform.transform.translation.y
        pose_stamped.pose.position.z = transform.transform.translation.z
        pose_stamped.pose.orientation = transform.transform.rotation
        self._trajectory.poses.append(pose_stamped)

    def get_trajectory(self) -> Optional[Path]:
        if not self._trajectory.poses:
            return None
        return self._trajectory

    def get_status(self) -> str:
        if self._process is not None and self._process.poll() is not None:
            self.status = f"Error: slam_toolbox exited (rc={self._process.returncode})"
        return self.status

    def shutdown(self) -> None:
        if self._process is not None and self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=5.0)
            except subprocess.TimeoutExpired:
                self._process.kill()
                self._process.wait()
        self._process = None
        self.initialized = False
        self.status = "Shutdown"

    def configure(self, config: Dict[str, Any]) -> bool:
        self.config.update(config)
        return True
