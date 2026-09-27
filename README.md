# SLAM PLATFORM
This is a plugin based SLAM platform which is used to provide a modular and neat workflow and comparison for different SLAM algorithms, to be compared on the same or different (user selected) worlds. This platform provides both simulation evaluation and hardware implementation of the SLAM algorithm plugins and can be used to test and use a variety of SLAM algorithms.

- [Development Setup](#development-setup)
- [Workspace Layout](#workspace-layout)
- [Building](#building)
- [Running](#running)
- [Benchmarking (headless, one command)](#benchmarking-headless-one-command)
- [Plugin Status](#plugin-status)

## Development Setup
Clone the repository:
`git clone https://github.com/RSWDevian/slam_platform.git`

Once cloned, a full fledged docker development environment is setup, for the code execution and slam plugin implementation.
Build the repository once: `docker compose build`
Start the container: `docker compose up -d`
Enter the container bash: `docker exec -it slam_platform bash`, or `scripts/enter_dev.sh` (uses `docker-compose.dev.yml`, which additionally mounts your `~/.gitconfig` and `~/.ssh` read-only so `git` works with your identity inside the container).

There are three compose files, layered via `-f` (base + overrides), not standalone alternatives:
- `docker-compose.yml` — the base service: build, image, GPU, X11, volumes. `docker compose up -d` uses this alone for a plain interactive dev container.
- `docker-compose.dev.yml` — override adding `~/.gitconfig`/`~/.ssh` mounts. Used via `docker compose -f docker-compose.yml -f docker-compose.dev.yml ...` (see `scripts/enter_dev.sh`).
- `docker-compose.benchmark.yml` — override for a headless, non-interactive run: builds both workspaces, launches the full platform, benchmarks one plugin, writes a report, then exits. See [Benchmarking](#benchmarking-headless-one-command).

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
Bring up the whole platform (world, robot, bridge, ground truth, TF health check, evaluator, plugin manager) with one command:
```
source slam_ws/install/setup.bash
source plugin_ws/install/setup.bash
ros2 launch platform_bringup platform.launch.py headless:=true active_plugin:=slam_toolbox
```
`world_name`, `headless`, and `active_plugin` are the launch args; see `platform_bringup/launch/platform.launch.py` for the staggered startup order. Each piece can also be launched individually — see that file for the exact package/launch-file list.

`world.launch.py` resolves the world file via the `WORKSPACE` env var (set in `.env`, passed through by `docker-compose.yml`), so it works from any directory. Pass `headless:=true` to run `gz sim` server-only (`-s -r`, no GUI) — useful in CI/sandboxed environments with no X11 display, where the GUI otherwise aborts on startup and tears down the whole simulation. `world_manager_node` (run separately) discovers world directories under `slam_ws/worlds/` and reports which have an actual `world.sdf` on `/world_manager/world_status`.

`tf_manager` monitors a configurable set of transforms (default `odom:base_link,map:odom`) and reports whether each currently resolves on `/tf_manager/tf_status` — a quick way to check the TF tree is healthy before or during a run.

`plugin_manager` reads `slam_ws/src/plugin_manager/config/plugins.yaml` to discover plugins, and reports each one's load status on `/plugin_manager/plugin_status`. Once a plugin is loaded, `plugin_manager` also republishes its pose on `/slam_output/pose` at 10Hz, which is what lets `evaluator_ros` compute a real `ate` against `/ground_truth/pose`. Plugins are loaded by publishing `load:<plugin_id>` to `/plugin_manager/plugin_command` (or via `experiment_manager`, below).

Benchmark a plugin with `experiment_manager`: it waits for `tf_manager` to confirm `odom->base_link` is healthy (aborting fast with a clear reason if not, instead of running the full duration for a useless report), requests `plugin_manager` to load the plugin, collects `evaluator_ros` metrics for a fixed duration, and writes a JSON report to `results/`.
```
ros2 launch experiment_manager run_experiment.launch.py plugin_id:=slam_toolbox duration:=60.0
```

## Benchmarking (headless, one command)
For a fully automated run with no manual steps — builds, launches, benchmarks, and exits:
```
BENCHMARK_PLUGIN=slam_toolbox BENCHMARK_DURATION=60.0 BENCHMARK_WORLD=test_world \
  docker compose -f docker-compose.yml -f docker-compose.benchmark.yml up
```
This runs `scripts/run_benchmark.sh` inside the container, which builds both workspaces, launches `platform_bringup` headlessly, runs `experiment_manager`, then tears the platform down. The report lands in `results/` on the host (mounted volume). All three `BENCHMARK_*` vars are optional and default as shown.

Requires a working NVIDIA driver on the host (`docker-compose.yml` requests `gpus: all`) — without one, `docker compose up` fails at container creation with an `nvml error: driver not loaded` from `nvidia-container-cli`. That's a host-level GPU driver issue, not something in this repo; check `nvidia-smi` on the host first.

## Plugin Status
- `slam_toolbox` — implemented. Wraps the ROS `slam_toolbox` package (managed as a subprocess, driven through its lifecycle, pose read back via the `map` → `base_link` transform).
- `orb_slam3`, `cnn_slam`, `rl_slam` — scaffolded but not yet implemented; `plugin_manager` reports them as `not_implemented` until a matching `SlamPlugin` subclass is added.
