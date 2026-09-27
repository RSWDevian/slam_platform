"""Orchestrates a single SLAM benchmarking run.

Requests plugin_manager to load a given plugin, watches its load status,
collects evaluator_ros metrics for a fixed duration, then writes a JSON
report summarizing the run.
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

        self.finished = False
        self.exit_code = 0

        self._plugin_id = self.get_parameter('plugin_id').get_parameter_value().string_value
        self._duration = self.get_parameter('duration').get_parameter_value().double_value
        self._output_dir = self.get_parameter('output_dir').get_parameter_value().string_value

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

        self._command_pub = self.create_publisher(String, '/plugin_manager/plugin_command', 10)
        self.create_subscription(String, '/plugin_manager/plugin_status', self._on_plugin_status, 10)
        self.create_subscription(SLAMMetrics, '/evaluation/metrics', self._on_metrics, 10)

        # Give plugin_manager's subscriber a moment to be discoverable on the
        # ROS graph before requesting the load; fires once then cancels.
        self._load_timer = self.create_timer(1.0, self._request_load)
        self._finish_timer = self.create_timer(self._duration, self._finish)

        self.get_logger().info(
            f"Experiment starting: plugin='{self._plugin_id}', duration={self._duration}s, "
            f"output_dir='{self._output_dir}'"
        )

    def _request_load(self) -> None:
        msg = String()
        msg.data = f"load:{self._plugin_id}"
        self._command_pub.publish(msg)
        self.get_logger().info(f"Requested plugin_manager to load '{self._plugin_id}'")
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

    def _finish(self) -> None:
        self._finish_timer.cancel()
        elapsed_s = (self.get_clock().now() - self._start_time).nanoseconds / 1e9

        report = {
            "plugin_id": self._plugin_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "requested_duration_s": self._duration,
            "elapsed_s": elapsed_s,
            "final_plugin_status": self._last_plugin_status,
            "plugin_status_message": self._plugin_status_message,
            "metrics_samples": self._metrics_samples,
            "final_metrics": self._metrics_to_dict(self._latest_metrics),
        }

        output_dir = Path(self._output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp_slug = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = output_dir / f"experiment_{self._plugin_id}_{timestamp_slug}.json"
        with report_path.open("w") as f:
            json.dump(report, f, indent=2)

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
