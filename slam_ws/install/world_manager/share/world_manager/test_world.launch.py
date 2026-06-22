from pathlib import Path

from launch import LaunchDescription
from launch.actions import ExecuteProcess   

def generate_launch_description():

    worksppace_root = Path.cwd()

    world_file = (
        worksppace_root / "worlds" / "test_world" / "world.sdf"
    )

    gazebo = ExecuteProcess(
        cmd=[
            "gz",
            "sim",
            "-v4",
            world_file
        ],
        output="screen"
    )

    return LaunchDescription([
        gazebo
    ])