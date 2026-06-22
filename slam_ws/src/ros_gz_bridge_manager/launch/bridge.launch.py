from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    camera_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        arguments=[
            '/camera/image_raw@sensor_msgs/msg/Image@gz.msgs.Image'
        ],
        output="screen"
    )

    camera_info_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/camera/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'
        ],
        output='screen'
    )

    lidar_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'
        ],
        output='screen'
    )

    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/imu/data@sensor_msgs/msg/Imu@gz.msgs.IMU'
        ],
        output='screen'
    )

    cmd_vel_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
        ],
        output='screen'
    )

    cmd_odom_bridge = Node(
    package='ros_gz_bridge',
    executable='parameter_bridge',
    arguments=[
        '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry'
    ],
    output='screen'
)

    return LaunchDescription([
        camera_bridge,
        camera_info_bridge,
        lidar_bridge,
        imu_bridge,
        cmd_vel_bridge,
        cmd_odom_bridge
    ])