from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package="evaluator_ros",
            executable="pose_comparator",
            output="screen"
        ),
        Node(
            package="evaluator_ros",
            executable="trajectory_evaluator",
            output="screen"
        ),
        Node(
            package="evaluator_ros",
            executable="resource_monitor",
            output="screen"
        ),
        Node(
            package="evaluator_ros",
            executable="metrics_publisher",
            output="screen"
        )
    ])