from launch import LaunchDescription
from launch_ros.actions import Node

from launch.substitutions import Command
from launch.substitutions import PathJoinSubstitution

from launch_ros.substitutions import FindPackageShare
from pathlib import Path

def generate_launch_description():

    worksppace_root = Path.cwd()

    robot_file = (worksppace_root / "robots" / "differential_robot" / "urdf" / "robot.urdf.xacro")

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
        parameters=[robot_description]
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        output="screen"
    )

    jsp = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        output='screen'
    )

    return LaunchDescription([
        rsp,
        rviz,
        jsp
    ])