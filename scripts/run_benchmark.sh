#!/bin/bash
# Builds the workspaces, launches the full platform headlessly, benchmarks
# one plugin for a fixed duration, then tears the platform down.
#
# Configured via env vars (matching docker-compose.benchmark.yml):
#   BENCHMARK_WORLD    world to launch          (default: test_world)
#   BENCHMARK_PLUGIN   plugin id to benchmark   (default: slam_toolbox)
#   BENCHMARK_DURATION experiment duration, sec (default: 60.0)
set -e

source /opt/ros/jazzy/setup.bash

cd /workspace
scripts/build.sh

source slam_ws/install/setup.bash
source plugin_ws/install/setup.bash

WORLD_NAME="${BENCHMARK_WORLD:-test_world}"
PLUGIN_ID="${BENCHMARK_PLUGIN:-slam_toolbox}"
DURATION="${BENCHMARK_DURATION:-60.0}"

ros2 launch platform_bringup platform.launch.py \
  world_name:="$WORLD_NAME" \
  headless:=true &
PLATFORM_PID=$!

# Give the world/robot/bridge/plugin_manager stack time to come up before
# experiment_manager starts polling tf_manager for a healthy TF tree.
sleep 12

ros2 launch experiment_manager run_experiment.launch.py \
  plugin_id:="$PLUGIN_ID" \
  duration:="$DURATION"
EXPERIMENT_RC=$?

kill "$PLATFORM_PID" 2>/dev/null
wait "$PLATFORM_PID" 2>/dev/null

exit "$EXPERIMENT_RC"
