#!/bin/bash
set -e

source /opt/ros/jazzy/setup.bash

if [ -f /workspace/slam_ws/install/setup.bash ]; then
    source /workspace/slam_ws/install/setup.bash
fi

if [ -f /workspace/plugins_ws/install/setup.bash ]; then
    source /workspace/plugins_ws/install/setup.bash
fi

exec "$@"