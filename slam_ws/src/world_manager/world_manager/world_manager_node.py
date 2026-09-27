"""ROS2 node that discovers available simulation worlds and reports status."""
import json
import os
from pathlib import Path

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class WorldManagerNode(Node):

    def __init__(self):
        super().__init__('world_manager')

        self.declare_parameter('active_world', 'test_world')
        self.declare_parameter(
            'worlds_dir',
            str(Path(os.environ.get('WORKSPACE', '/workspace')) / 'slam_ws' / 'worlds'),
        )

        self._active_world = self.get_parameter('active_world').get_parameter_value().string_value
        worlds_dir = self.get_parameter('worlds_dir').get_parameter_value().string_value
        self._worlds = self._discover_worlds(Path(worlds_dir))

        self._status_pub = self.create_publisher(String, '~/world_status', 10)
        self.create_timer(2.0, self._publish_status)

        available = [name for name, present in self._worlds.items() if present]
        missing = [name for name, present in self._worlds.items() if not present]
        self.get_logger().info(
            f"Discovered {len(self._worlds)} world director"
            f"{'y' if len(self._worlds) == 1 else 'ies'} under '{worlds_dir}': "
            f"{len(available)} with a world.sdf ({', '.join(available) or 'none'}), "
            f"{len(missing)} empty ({', '.join(missing) or 'none'})"
        )
        if self._active_world not in self._worlds:
            self.get_logger().warn(
                f"active_world '{self._active_world}' was not found under '{worlds_dir}'"
            )
        elif not self._worlds[self._active_world]:
            self.get_logger().warn(
                f"active_world '{self._active_world}' has no world.sdf yet"
            )

    @staticmethod
    def _discover_worlds(worlds_dir: Path) -> dict:
        worlds = {}
        if not worlds_dir.is_dir():
            return worlds
        for entry in sorted(worlds_dir.iterdir()):
            if entry.is_dir():
                worlds[entry.name] = (entry / 'world.sdf').is_file()
        return worlds

    def _publish_status(self) -> None:
        payload = {
            "active_world": self._active_world,
            "worlds": {
                name: {"available": available}
                for name, available in self._worlds.items()
            },
        }
        msg = String()
        msg.data = json.dumps(payload)
        self._status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = WorldManagerNode()
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
