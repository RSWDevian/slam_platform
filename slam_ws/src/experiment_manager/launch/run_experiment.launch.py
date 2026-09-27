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

    tf_check_timeout_arg = DeclareLaunchArgument(
        'tf_check_timeout',
        default_value='15.0',
        description=(
            'Seconds to wait for tf_manager to report odom->base_link as healthy '
            'before aborting the experiment. Set to 0 to skip the check.'
        ),
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
            'tf_check_timeout': LaunchConfiguration('tf_check_timeout'),
        }],
    )

    return LaunchDescription([
        plugin_id_arg,
        duration_arg,
        output_dir_arg,
        tf_check_timeout_arg,
        experiment_runner_node,
    ])
