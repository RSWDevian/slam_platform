# SLAM PLATFORM
This is a plugin based SLAM platform which is used to provide a modular and neat workflow and comparison for different SLAM algorithms, to be compared on the same or different (user selected) worlds. This platform provides both simulation evaluation and hardware implementation of the SLAM algorithm plugins and can be used to test and use a variety of SLAM algorithms.

- [Development Setup](#development-setup)
- [Workspace Layout](#workspace-layout)
- [Building](#building)
- [Running](#running)
- [Plugin Status](#plugin-status)

## Development Setup
Clone the repository:
`git clone https://github.com/RSWDevian/slam_platform.git`

Once cloned, a full fledged docker development environment is setup, for the code execution and slam plugin implementation.
Build the repository once: `docker compose build`
Start the container: `docker compose up -d`
Enter the container bash: `docker exec -it slam_platform bash`

## Workspace Layout
- `slam_ws/` — the core platform: simulation worlds/robots, sensor adapters, ground truth provider, the ROS↔Gazebo bridge, the evaluator, and `plugin_manager` (discovers and loads SLAM plugins at runtime).
- `plugin_ws/` — the SLAM algorithm plugins themselves (`orb_slam_plugin`, `cnn_slam_plugin`, `rl_slam_plugin`, `slam_toolbox_plugin`), kept as a separate workspace so plugins can be added/swapped independently of the core platform. `slam_plugin_base` holds the shared `SlamPlugin` interface every plugin implements.

## Building
Inside the container, build both workspaces:
```
scripts/build.sh
```
which sources ROS 2 and runs `colcon build --symlink-install` in `slam_ws` and `plugin_ws`.

## Running
There is no single top-level launch file yet — bring the pieces up individually (each in its own terminal, inside the container, with `source slam_ws/install/setup.bash` and `source plugin_ws/install/setup.bash` sourced):

```
ros2 launch world_manager world.launch.py world_name:=test_world   # simulation world
ros2 launch robot_bringup spawn_robot_gz.launch.py                 # spawn the robot
ros2 launch ros_gz_bridge_manager bridge.launch.py                 # bridge sensors, /cmd_vel, /tf
ros2 launch ground_truth_provider ground_truth_provider.launch.py
ros2 launch tf_manager tf_manager.launch.py                        # TF tree health check
ros2 run evaluator_ros metrics_publisher
ros2 run evaluator_ros resource_monitor
ros2 run plugin_manager plugin_manager_node
```

`world.launch.py` resolves the world file via the `WORKSPACE` env var (set in `.env`, passed through by `docker-compose.yml`), so it works from any directory. Pass `headless:=true` to run `gz sim` server-only (`-s -r`, no GUI) — useful in CI/sandboxed environments with no X11 display, where the GUI otherwise aborts on startup and tears down the whole simulation. `world_manager_node` (run separately) discovers world directories under `slam_ws/worlds/` and reports which have an actual `world.sdf` on `/world_manager/world_status`.

`tf_manager` monitors a configurable set of transforms (default `odom:base_link,map:odom`) and reports whether each currently resolves on `/tf_manager/tf_status` — a quick way to check the TF tree is healthy before or during a run.

`plugin_manager` reads `slam_ws/src/plugin_manager/config/plugins.yaml` to discover plugins, and reports each one's load status on `/plugin_manager/plugin_status`. Plugins are loaded by publishing `load:<plugin_id>` to `/plugin_manager/plugin_command` (or via `experiment_manager`, below).

Once the pieces above are running, benchmark a plugin with `experiment_manager`: it requests `plugin_manager` to load the plugin, waits for it to come up, collects `evaluator_ros` metrics for a fixed duration, and writes a JSON report to `results/`.
```
ros2 launch experiment_manager run_experiment.launch.py plugin_id:=slam_toolbox duration:=60.0
```

## Plugin Status
- `slam_toolbox` — implemented. Wraps the ROS `slam_toolbox` package (managed as a subprocess, driven through its lifecycle, pose read back via the `map` → `base_link` transform).
- `orb_slam3`, `cnn_slam`, `rl_slam` — scaffolded but not yet implemented; `plugin_manager` reports them as `not_implemented` until a matching `SlamPlugin` subclass is added.

Note: `ate` in an experiment report will read `0.0` until a plugin publishes its estimated pose on `/slam_output/pose` for `evaluator_ros` to compare against ground truth — `slam_toolbox` currently only exposes pose via TF, not that topic.
