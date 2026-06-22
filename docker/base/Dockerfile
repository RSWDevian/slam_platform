FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    software-properties-common \
    build-essential \
    cmake \
    python3 \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-psutil \
    lsb-release \
    gnupg2 \
    locales \
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US en_US.UTF-8

ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key \
 | tee /usr/share/keyrings/ros-archive-keyring.gpg > /dev/null

RUN echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] \
http://packages.ros.org/ros2/ubuntu noble main" \
> /etc/apt/sources.list.d/ros2.list

RUN apt-get update && apt-get install -y \
    ros-jazzy-desktop \
    ros-dev-tools \
    ros-jazzy-rosidl-default-generators \
    ros-jazzy-ros2cli \
    ros-jazzy-ros2interface \
    ros-jazzy-ros2node \
    ros-jazzy-ros2service \
    ros-jazzy-ros2action \
    ros-jazzy-ros2topic \
    ros-jazzy-ros2param \
    ros-jazzy-ros2doctor

RUN rosdep init || true

COPY ros_entrypoint.sh /ros_entrypoint.sh

RUN chmod +x /ros_entrypoint.sh

ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]