FROM ros:jazzy
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]

RUN apt update && apt install -y \
build-essential \
cmake \
git \
curl \
wget \
nano \
vim \
gdb \
htop \
tree \
software-properties-common

RUN apt install -y \
python3-pip \
python3-colcon-common-extensions \
python3-vcstool \
python3-rosdep

RUN apt install -y \
ros-jazzy-ros-gz \
ros-jazzy-rviz2 \
ros-jazzy-rqt \
ros-jazzy-rqt-image-view \
ros-jazzy-rqt-graph \
ros-jazzy-slam-toolbox

RUN apt install -y \
libopencv-dev \
libeigen3-dev \
libboost-all-dev \
libglew-dev \
libyaml-cpp-dev \
libpcl-dev

RUN apt install -y \
python3-numpy \
python3-scipy \
python3-pandas \
python3-matplotlib

COPY docker/ros_entrypoint.sh /
RUN chmod +x /ros_entrypoint.sh
WORKDIR /workspace
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]