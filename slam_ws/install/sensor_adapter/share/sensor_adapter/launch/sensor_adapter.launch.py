from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sensor_adapter',
            executable='camera_adapter',
        ),
        Node(
            package='sensor_adapter',
            executable='imu_adapter',
        ),
        Node(
            package='sensor_adapter',
            executable='odom_adapter',
        ),
        Node(
            package='sensor_adapter',
            executable='lidar_adapter',
        ),
        Node(
            package='sensor_adapter',
            executable='camera_info_adapter',
        )
    ])