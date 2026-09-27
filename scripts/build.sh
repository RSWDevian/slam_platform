#!/bin/bash
source /opt/ros/jazzy/setup.bash

cd /workspace/slam_ws
colcon build --symlink-install

cd /workspace/plugin_ws
colcon build --symlink-install
