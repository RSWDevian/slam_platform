"""ROS2 node that monitors a configured set of TF transforms and reports
whether each one currently resolves - a health check for the platform's TF
tree (e.g. odom -> base_link from the robot, map -> odom from an active SLAM
plugin) that other tools (experiment_manager, a user) can check before or
during a run.
"""
import json

import rclpy
from rclpy.node import Node
from rclpy.time import Time
from std_msgs.msg import String
from tf2_ros import (
    Buffer,
    ConnectivityException,
    ExtrapolationException,
    LookupException,
    TransformListener,
)


class TfManagerNode(Node):

    def __init__(self):
        super().__init__('tf_manager')

        self.declare_parameter('required_transforms', 'odom:base_link,map:odom')
        raw = self.get_parameter('required_transforms').get_parameter_value().string_value
        self._pairs = self._parse_pairs(raw)

        self._tf_buffer = Buffer()
        self._tf_listener = TransformListener(self._tf_buffer, self)
        self._status = {
            pair_id: {"available": False, "message": "not checked yet"}
            for pair_id in self._pairs
        }

        self._status_pub = self.create_publisher(String, '~/tf_status', 10)
        self.create_timer(1.0, self._check_transforms)
        self.create_timer(2.0, self._publish_status)

        self.get_logger().info(
            f"Monitoring {len(self._pairs)} transform(s): {', '.join(self._pairs.keys())}"
        )

    @staticmethod
    def _parse_pairs(raw: str) -> dict:
        pairs = {}
        for entry in raw.split(','):
            entry = entry.strip()
            if not entry:
                continue
            parent, sep, child = entry.partition(':')
            if not sep:
                continue
            pairs[f"{parent}->{child}"] = (parent, child)
        return pairs

    def _check_transforms(self) -> None:
        for pair_id, (parent, child) in self._pairs.items():
            try:
                self._tf_buffer.lookup_transform(parent, child, Time())
            except (LookupException, ConnectivityException, ExtrapolationException) as e:
                self._status[pair_id] = {"available": False, "message": str(e)}
            else:
                self._status[pair_id] = {"available": True, "message": "ok"}

    def _publish_status(self) -> None:
        msg = String()
        msg.data = json.dumps(self._status)
        self._status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = TfManagerNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
