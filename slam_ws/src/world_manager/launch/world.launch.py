from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import (
    EnvironmentVariable,
    LaunchConfiguration,
    PathJoinSubstitution,
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
        description=(
            'Run gz sim server-only (-s -r), with no GUI. Use for CI/sandboxed '
            'environments with no X11 display; the GUI otherwise aborts on '
            'startup when it cannot connect to a display, which then tears '
            'down the whole simulation.'
        ),
    )

    world_file = PathJoinSubstitution([
        EnvironmentVariable('WORKSPACE', default_value='/workspace'),
        'slam_ws', 'worlds', LaunchConfiguration('world_name'), 'world.sdf',
    ])

    gazebo_gui = ExecuteProcess(
        cmd=['gz', 'sim', '-v4', world_file],
        output='screen',
        condition=UnlessCondition(LaunchConfiguration('headless')),
    )

    gazebo_headless = ExecuteProcess(
        cmd=['gz', 'sim', '-s', '-r', '-v4', world_file],
        output='screen',
        condition=IfCondition(LaunchConfiguration('headless')),
    )

    return LaunchDescription([
        world_name_arg,
        headless_arg,
        gazebo_gui,
        gazebo_headless,
    ])
