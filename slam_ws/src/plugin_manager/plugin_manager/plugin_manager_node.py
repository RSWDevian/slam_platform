"""ROS2 node that discovers, loads, and reports the status of SLAM plugins."""
import json
from pathlib import Path

import rclpy
from ament_index_python.packages import get_package_share_directory
from rclpy.node import Node
from std_msgs.msg import String

from plugin_manager.plugin_loader import PluginLoader
from plugin_manager.plugin_registry import PluginRegistry
from plugin_manager.plugin_status import PluginState


class PluginManagerNode(Node):

    def __init__(self):
        super().__init__("plugin_manager")

        default_config = str(
            Path(get_package_share_directory("plugin_manager")) / "config" / "plugins.yaml"
        )
        self.declare_parameter("plugins_config", default_config)
        self.declare_parameter("active_plugin", "")

        config_path = self.get_parameter("plugins_config").get_parameter_value().string_value
        self._registry = PluginRegistry.from_yaml(config_path)
        self._loader = PluginLoader()
        self._states = {
            plugin_id: PluginState(plugin_id=plugin_id) for plugin_id in self._registry.list_ids()
        }
        self._instances = {}

        self._status_pub = self.create_publisher(String, "~/plugin_status", 10)
        self.create_subscription(String, "~/plugin_command", self._on_command, 10)
        self.create_timer(2.0, self._publish_status)

        self.get_logger().info(
            f"Discovered {len(self._registry.list_ids())} plugin(s): "
            f"{', '.join(self._registry.list_ids())}"
        )

        active_plugin = self.get_parameter("active_plugin").get_parameter_value().string_value
        if active_plugin:
            self._load_plugin(active_plugin)

    def _load_plugin(self, plugin_id: str) -> None:
        declaration = self._registry.get(plugin_id)
        if declaration is None:
            self.get_logger().error(f"Unknown plugin id '{plugin_id}'")
            return

        instance, state = self._loader.load(declaration)
        self._states[plugin_id] = state
        if instance is not None:
            self._instances[plugin_id] = instance
            self.get_logger().info(f"Plugin '{plugin_id}' loaded: {state.message}")
        else:
            self.get_logger().warn(f"Plugin '{plugin_id}' not loaded: {state.message}")

    def _on_command(self, msg: String) -> None:
        command, _, plugin_id = msg.data.partition(":")
        if not plugin_id:
            self.get_logger().warn(f"Ignoring malformed plugin command: '{msg.data}'")
            return
        if command == "load":
            self._load_plugin(plugin_id)
        else:
            self.get_logger().warn(f"Unknown plugin command '{command}'")

    def _publish_status(self) -> None:
        payload = {plugin_id: state.to_dict() for plugin_id, state in self._states.items()}
        msg = String()
        msg.data = json.dumps(payload)
        self._status_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PluginManagerNode()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, rclpy.executors.ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
