from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    plugin_id_arg = DeclareLaunchArgument(
        'plugin_id',
        description='Plugin id (from plugin_manager/config/plugins.yaml) to benchmark.',
    )

    duration_arg = DeclareLaunchArgument(
        'duration',
        default_value='60.0',
        description='How long to run the experiment for, in seconds.',
    )

    output_dir_arg = DeclareLaunchArgument(
        'output_dir',
        default_value='/workspace/results',
        description='Directory the experiment report JSON is written to.',
    )

    experiment_runner_node = Node(
        package='experiment_manager',
        executable='experiment_runner',
        name='experiment_runner',
        output='screen',
        parameters=[{
            'plugin_id': LaunchConfiguration('plugin_id'),
            'duration': LaunchConfiguration('duration'),
            'output_dir': LaunchConfiguration('output_dir'),
        }],
    )

    return LaunchDescription([
        plugin_id_arg,
        duration_arg,
        output_dir_arg,
        experiment_runner_node,
    ])
