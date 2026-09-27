from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    required_transforms_arg = DeclareLaunchArgument(
        'required_transforms',
        default_value='odom:base_link,map:odom',
        description='Comma-separated parent:child transform pairs to monitor.',
    )

    tf_manager_node = Node(
        package='tf_manager',
        executable='tf_manager_node',
        name='tf_manager',
        output='screen',
        parameters=[{
            'required_transforms': LaunchConfiguration('required_transforms'),
        }],
    )

    return LaunchDescription([
        required_transforms_arg,
        tf_manager_node,
    ])
