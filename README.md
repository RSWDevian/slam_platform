# SLAM PLATFORM
This is a plugin based SLAM platform which is used to provided a modular and neat workflow and comparism for different SLAM algorithms, to be compared on the same or different (user selected worlds). This platform provides both simulation evaluation and hardware implementation of the SLAM algorithm plugins and can be used to test and use a variety of SLAM algorithms.

- [Development Setup](#development-setup)

## Development Setup
Clone the repository:
`git clone https://github.com/RSWDevian/slam_platform.git`

Once cloned, a full fledged docker development environment is setup, for the code execution and slam plugin implementation. 
Build thhe repository once: `docker compose build`
Start the container: `docker compose up -d`
Enter the container bash: `docker exec -it slam_platform bash`