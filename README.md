# This package provides an autonomous navigation system for AUTOWARE using ROS 2.
# Building and using the package

Clone the repository into your home directory: git clone https://github.com/KonstantinKolodi/autolab_course

Copy "autolab" folder into your home directory. after you can delete old autolab_course folder, we don't need it.

To run the container, open a new terminal and run the following command first: xhost +local:docker

Log you in as the root user:

docker run -it --rm --privileged --net=host \
  --env=DISPLAY \
  --env=QT_X11_NO_MITSHM=1 \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /home/<your_user>/autolab/ros2_ws:/ros2_ws \
  -v /home/<your_user>/autolab/autoware_map:/autoware_map \
  --workdir /ros2_ws \
  mohsen_aw:full bash

Build the package: colcon build

# Launching Autonomous Navigation of Ego Vehicle

Run the mission: ros2 launch my_robot_controller car_nav.launch.py

# Features

Autonomous navigation

Single launch file

Three goal destinations

# Dependencies

Ubuntu 22.04

latest TurtleBot3 repository

ROS 2 (Humble)

Navigation and SLAM tools (if needed for mapping visualization)

AUTOWARE docker package from Moodle

# Troubleshooting

Check location path of autolab package

Check remove build and install folders, buiild the package afterwards.
