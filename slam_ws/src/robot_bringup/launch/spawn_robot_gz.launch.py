from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import Command, EnvironmentVariable, PathJoinSubstitution


def generate_launch_description():

    robot_file = PathJoinSubstitution([
        EnvironmentVariable('WORKSPACE', default_value='/workspace'),
        'slam_ws', 'robots', 'differential_robot', 'urdf', 'robot.urdf.xacro',
    ])

    robot_description = {
        "robot_description": Command(
            [
                "xacro ",
                robot_file
            ]
        )
    }

    rsp = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
        output="screen"
    )

    spawn = Node(
        package="ros_gz_sim",
        executable="create",
        arguments=[
            "-topic",
            "robot_description",
            "-name",
            "differential_robot",
            "-z",
            "0.1"
        ],
        output="screen"
    )

    return LaunchDescription([
        rsp,
        spawn
    ])