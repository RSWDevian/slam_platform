import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    default_config = os.path.join(
        get_package_share_directory("plugin_manager"), "config", "plugins.yaml"
    )

    plugins_config_arg = DeclareLaunchArgument(
        "plugins_config",
        default_value=default_config,
        description="Path to the plugin registry YAML file.",
    )

    active_plugin_arg = DeclareLaunchArgument(
        "active_plugin",
        default_value="",
        description="Plugin id to load automatically at startup (optional).",
    )

    plugin_manager_node = Node(
        package="plugin_manager",
        executable="plugin_manager_node",
        name="plugin_manager",
        output="screen",
        parameters=[{
            "plugins_config": LaunchConfiguration("plugins_config"),
            "active_plugin": LaunchConfiguration("active_plugin"),
        }],
    )

    return LaunchDescription([
        plugins_config_arg,
        active_plugin_arg,
        plugin_manager_node,
    ])
