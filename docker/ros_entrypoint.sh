#!/bin/bash
set -e

source /opt/ros/jazzy/setup.bash

export CMAKE_PREFIX_PATH=/opt/ros/jazzy:${CMAKE_PREFIX_PATH}

if [ -f /workspace/slam_ws/install/setup.bash ]; then
    source /workspace/slam_ws/install/setup.bash
fi

if [ -f /workspace/plugin_ws/install/setup.bash ]; then
    source /workspace/plugin_ws/install/setup.bash
fi

exec "$@"