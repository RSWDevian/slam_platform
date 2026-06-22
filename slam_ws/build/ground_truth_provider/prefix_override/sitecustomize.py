import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/abhirup/slam_platform/slam_ws/install/ground_truth_provider'
