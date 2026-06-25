PLUGIN_NAME = "ORB_SLAM3"
PLUGIN_VERSION = "1.0" 
REQUIRED_INPUTS = [
    "/slam/camera/image_raw",
    "/slam/camera/camera_info",
    "/slam/imu/data"
]

OPTIONAL_INPUTS = [
    "/slam/lidar/scan",
    "/slam/odom"
]

OUTPUTS = [
    "/slam_output/pose",
    "/slam_output/path",
    "/slam_output/status"
]