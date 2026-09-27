"""Top-level launch file: world, robot, ROS-Gazebo bridge, ground truth,
TF health check, evaluator, and plugin manager - staggered so each stage's
dependencies (e.g. the world existing before the robot spawns into it) are
up before the next stage starts.

Does not include experiment_manager: that's a one-shot tool run separately,
on demand, once this stack is up (see README).
"""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def _include(package, launch_file, launch_arguments=None):
    path = os.path.join(get_package_share_directory(package), 'launch', launch_file)
    return IncludeLaunchDescription(
        PythonLaunchDescriptionSource(path),
        launch_arguments=launch_arguments,
    )


def generate_launch_description():
    world_name_arg = DeclareLaunchArgument(
        'world_name',
        default_value='test_world',
        description='Name of the world directory under slam_ws/worlds to launch.',
    )
    headless_arg = DeclareLaunchArgument(
        'headless',
        default_value='false',
        description='Run gz sim server-only (-s -r), with no GUI.',
    )
    active_plugin_arg = DeclareLaunchArgument(
        'active_plugin',
        default_value='',
        description='Plugin id to load automatically once plugin_manager comes up (optional).',
    )

    world = _include('world_manager', 'world.launch.py', [
        ('world_name', LaunchConfiguration('world_name')),
        ('headless', LaunchConfiguration('headless')),
    ])

    # gz sim needs a few seconds to load the world and start serving its
    # create service before ros_gz_sim can spawn the robot into it.
    robot = TimerAction(period=6.0, actions=[
        _include('robot_bringup', 'spawn_robot_gz.launch.py'),
    ])

    # Bridge, ground truth, TF health check, and the evaluator all depend on
    # the robot existing (for TF/joint/sensor topics) but not on each other.
    sensing = TimerAction(period=9.0, actions=[
        _include('ros_gz_bridge_manager', 'bridge.launch.py'),
        _include('ground_truth_provider', 'ground_truth_provider.launch.py'),
        _include('tf_manager', 'tf_manager.launch.py'),
        _include('evaluator_ros', 'evaluator.launch.py'),
    ])

    plugin_manager = TimerAction(period=11.0, actions=[
        _include('plugin_manager', 'plugin_manager.launch.py', [
            ('active_plugin', LaunchConfiguration('active_plugin')),
        ]),
    ])

    return LaunchDescription([
        world_name_arg,
        headless_arg,
        active_plugin_arg,
        world,
        robot,
        sensing,
        plugin_manager,
    ])
