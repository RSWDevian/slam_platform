from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package="ground_truth_provider",
            executable="pose_provider"
        ),

        Node(
            package="ground_truth_provider",
            executable="path_provider"
        ),

        Node(
            package="ground_truth_provider",
            executable="odom_provider"
        ),
    ])