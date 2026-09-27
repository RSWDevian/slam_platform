"""ROS2 node that discovers, loads, and reports the status of SLAM plugins."""
import json
from pathlib import Path

import rclpy
from ament_index_python.packages import get_package_share_directory
from geometry_msgs.msg import PoseStamped
from rclpy.node import Node
from std_msgs.msg import String

from plugin_manager.plugin_loader import PluginLoader
from plugin_manager.plugin_registry import PluginDeclaration, PluginRegistry
from plugin_manager.plugin_status import PluginState, PluginStatus


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
        self._active_plugin_id = None

        self._status_pub = self.create_publisher(String, "~/plugin_status", 10)
        self._slam_pose_pub = self.create_publisher(PoseStamped, "/slam_output/pose", 10)
        self.create_subscription(String, "~/plugin_command", self._on_command, 10)
        self.create_timer(2.0, self._publish_status)
        self.create_timer(0.1, self._publish_slam_pose)

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
        if instance is None:
            self._states[plugin_id] = state
            self.get_logger().warn(f"Plugin '{plugin_id}' not loaded: {state.message}")
            return

        config_path = self._resolve_config_path(declaration)
        try:
            initialized = instance.initialize(self, config_path)
        except Exception as exc:
            state.status = PluginStatus.LOAD_ERROR
            state.message = f"initialize() raised: {exc}"
            self._states[plugin_id] = state
            self.get_logger().error(f"Plugin '{plugin_id}' failed to initialize: {exc}")
            return

        if not initialized:
            state.status = PluginStatus.LOAD_ERROR
            state.message = f"initialize() failed: {getattr(instance, 'status', 'unknown error')}"
            self._states[plugin_id] = state
            self.get_logger().warn(f"Plugin '{plugin_id}' failed to initialize: {state.message}")
            return

        self._instances[plugin_id] = instance
        self._states[plugin_id] = state
        self._active_plugin_id = plugin_id
        self.get_logger().info(f"Plugin '{plugin_id}' loaded and initialized: {state.message}")

    def _resolve_config_path(self, declaration: PluginDeclaration) -> str:
        if not declaration.config:
            return ""
        try:
            share_dir = get_package_share_directory(declaration.package)
        except Exception as exc:
            self.get_logger().warn(
                f"Could not resolve share directory for '{declaration.package}': {exc}"
            )
            return declaration.config
        return str(Path(share_dir) / declaration.config)

    def shutdown_plugins(self) -> None:
        for plugin_id, instance in self._instances.items():
            try:
                instance.shutdown()
            except Exception as exc:
                self.get_logger().warn(f"Error shutting down plugin '{plugin_id}': {exc}")

    def _on_command(self, msg: String) -> None:
        command, _, plugin_id = msg.data.partition(":")
        if not plugin_id:
            self.get_logger().warn(f"Ignoring malformed plugin command: '{msg.data}'")
            return
        if command == "load":
            self._load_plugin(plugin_id)
        else:
            self.get_logger().warn(f"Unknown plugin command '{command}'")

    def _publish_slam_pose(self) -> None:
        if self._active_plugin_id is None:
            return
        instance = self._instances.get(self._active_plugin_id)
        if instance is None:
            return

        try:
            pose = instance.get_current_pose()
        except Exception as exc:
            self.get_logger().warn(
                f"get_current_pose() raised for '{self._active_plugin_id}': {exc}",
                throttle_duration_sec=5.0,
            )
            return

        if pose is None:
            return

        msg = PoseStamped()
        msg.header = pose.header
        msg.pose = pose.pose.pose
        self._slam_pose_pub.publish(msg)

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
        node.shutdown_plugins()
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
