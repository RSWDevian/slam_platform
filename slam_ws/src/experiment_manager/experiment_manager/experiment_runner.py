"""Orchestrates a single SLAM benchmarking run.

Waits for tf_manager to confirm the robot's own TF (odom -> base_link) is
healthy, requests plugin_manager to load a given plugin, watches its load
status, collects evaluator_ros metrics for a fixed duration, then writes a
JSON report summarizing the run.
"""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import rclpy
from rclpy.node import Node
from slam_interfaces.msg import SLAMMetrics
from std_msgs.msg import String


class ExperimentRunner(Node):

    def __init__(self):
        super().__init__('experiment_runner')

        self.declare_parameter('plugin_id', '')
        self.declare_parameter('duration', 60.0)
        self.declare_parameter('output_dir', '/workspace/results')
        self.declare_parameter('tf_check_timeout', 15.0)

        self.finished = False
        self.exit_code = 0

        self._plugin_id = self.get_parameter('plugin_id').get_parameter_value().string_value
        self._duration = self.get_parameter('duration').get_parameter_value().double_value
        self._output_dir = self.get_parameter('output_dir').get_parameter_value().string_value
        self._tf_check_timeout = self.get_parameter('tf_check_timeout').get_parameter_value().double_value

        if not self._plugin_id:
            self.get_logger().error(
                "experiment_runner requires the 'plugin_id' parameter, e.g. "
                "--ros-args -p plugin_id:=slam_toolbox"
            )
            self.finished = True
            self.exit_code = 1
            return

        self._start_time = self.get_clock().now()
        self._last_plugin_status = ""
        self._plugin_status_message = ""
        self._latest_metrics: Optional[SLAMMetrics] = None
        self._metrics_samples = 0
        self._tf_status: dict = {}
        self._map_odom_ever_available = False

        self._command_pub = self.create_publisher(String, '/plugin_manager/plugin_command', 10)
        self.create_subscription(String, '/plugin_manager/plugin_status', self._on_plugin_status, 10)
        self.create_subscription(SLAMMetrics, '/evaluation/metrics', self._on_metrics, 10)
        self.create_subscription(String, '/tf_manager/tf_status', self._on_tf_status, 10)

        self._finish_timer = self.create_timer(self._duration, self._finish)

        if self._tf_check_timeout > 0:
            self._tf_check_start = self.get_clock().now()
            self._tf_ready_timer = self.create_timer(1.0, self._check_tf_ready)
            self.get_logger().info(
                f"Waiting up to {self._tf_check_timeout}s for 'odom->base_link' TF "
                "to be healthy before loading the plugin"
            )
        else:
            # Give plugin_manager's subscriber a moment to be discoverable on
            # the ROS graph before requesting the load.
            self._load_timer = self.create_timer(1.0, self._request_load)

        self.get_logger().info(
            f"Experiment starting: plugin='{self._plugin_id}', duration={self._duration}s, "
            f"output_dir='{self._output_dir}'"
        )

    def _on_tf_status(self, msg: String) -> None:
        try:
            self._tf_status = json.loads(msg.data)
        except json.JSONDecodeError:
            return
        if self._tf_status.get("map->odom", {}).get("available"):
            self._map_odom_ever_available = True

    def _check_tf_ready(self) -> None:
        base_tf = self._tf_status.get("odom->base_link", {})
        if base_tf.get("available"):
            self._tf_ready_timer.cancel()
            self.get_logger().info("'odom->base_link' TF is healthy, requesting plugin load")
            self._request_load()
            return

        elapsed_s = (self.get_clock().now() - self._tf_check_start).nanoseconds / 1e9
        if elapsed_s >= self._tf_check_timeout:
            self._tf_ready_timer.cancel()
            reason = (
                f"'odom->base_link' TF not available after {self._tf_check_timeout}s "
                f"(tf_manager status: {base_tf or 'no data received on /tf_manager/tf_status - is tf_manager running?'})"
            )
            self.get_logger().error(f"Aborting experiment: {reason}")
            self._finish(aborted=True, abort_reason=reason)

    def _request_load(self) -> None:
        msg = String()
        msg.data = f"load:{self._plugin_id}"
        self._command_pub.publish(msg)
        self.get_logger().info(f"Requested plugin_manager to load '{self._plugin_id}'")
        if hasattr(self, '_load_timer'):
            self._load_timer.cancel()

    def _on_plugin_status(self, msg: String) -> None:
        try:
            payload = json.loads(msg.data)
        except json.JSONDecodeError:
            return

        entry = payload.get(self._plugin_id)
        if entry is None:
            return

        status = entry.get("status", "")
        if status != self._last_plugin_status:
            self.get_logger().info(
                f"Plugin '{self._plugin_id}' status -> {status}: {entry.get('message', '')}"
            )
            self._last_plugin_status = status
            self._plugin_status_message = entry.get("message", "")

    def _on_metrics(self, msg: SLAMMetrics) -> None:
        self._latest_metrics = msg
        self._metrics_samples += 1

    def _finish(self, aborted: bool = False, abort_reason: Optional[str] = None) -> None:
        self._finish_timer.cancel()
        if hasattr(self, '_tf_ready_timer'):
            self._tf_ready_timer.cancel()
        elapsed_s = (self.get_clock().now() - self._start_time).nanoseconds / 1e9

        report = {
            "plugin_id": self._plugin_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "requested_duration_s": self._duration,
            "elapsed_s": elapsed_s,
            "aborted": aborted,
            "abort_reason": abort_reason,
            "final_plugin_status": self._last_plugin_status,
            "plugin_status_message": self._plugin_status_message,
            "metrics_samples": self._metrics_samples,
            "final_metrics": self._metrics_to_dict(self._latest_metrics),
            "tf_status": {
                "final": self._tf_status,
                "map_odom_ever_available": self._map_odom_ever_available,
            },
        }

        output_dir = Path(self._output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp_slug = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = output_dir / f"experiment_{self._plugin_id}_{timestamp_slug}.json"
        with report_path.open("w") as f:
            json.dump(report, f, indent=2)

        if aborted:
            self.get_logger().error(f"Experiment aborted. Report written to {report_path}")
            self.exit_code = 1
        else:
            self.get_logger().info(f"Experiment complete. Report written to {report_path}")
        self.finished = True

    @staticmethod
    def _metrics_to_dict(metrics: Optional[SLAMMetrics]) -> Optional[dict]:
        if metrics is None:
            return None
        return {
            "ate": metrics.ate,
            "cpu_usage": metrics.cpu_usage,
            "memory_usage": metrics.memory_usage,
            "runtime": metrics.runtime,
            "thread_count": metrics.thread_count,
        }


def main(args=None):
    rclpy.init(args=args)
    node = ExperimentRunner()
    try:
        while rclpy.ok() and not node.finished:
            rclpy.spin_once(node, timeout_sec=0.5)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        exit_code = node.exit_code
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
    raise SystemExit(exit_code)


if __name__ == '__main__':
    main()
