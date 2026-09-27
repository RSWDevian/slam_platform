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