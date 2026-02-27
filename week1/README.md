# Week 1 Lab: Linux Onboarding and First ROS 2 Node

## Description
This repository contains the deliverables for Week 1 of the Mobile Robotics lab. It includes a basic ROS 2 Humble workspace setup, a custom Python package (`my_first_pkg`), and a node (`simple_node`) that demonstrates logging, file-based counters, and parameter parsing.

## Commands Used
* `mkdir -p ~/ros2_ws/src`
* `colcon build`
* `source install/setup.bash`
* `ros2 pkg create --build-type ament_python my_first_pkg`
* `ros2 run my_first_pkg simple_node`
* `ros2 run my_first_pkg simple_node --ros-args -p student_name:="Mohid"`

## Problems Faced & Solutions
* **Problem:** When attempting to verify the ROS 2 installation as instructed in the lab manual, the command `ros2 --version` returned a `ros2: error: unrecognized arguments: --version` error.
* **Solution:** I discovered that this specific argument isn't universally supported across all ROS 2 Humble installations. Instead, I verified the active distribution by running `printenv ROS_DISTRO` and checked the specific CLI package using `dpkg -l | grep ros-humble-ros2cli`.

## Reflection
As a Mechatronics and Control Engineering student, stepping into the ROS 2 ecosystem has been a highly relevant experience. While I am already accustomed to navigating Linux environments and writing Python code, adapting to the specific architecture of ROS 2—such as sourcing workspaces, managing `ament` build types, and registering entry points in `setup.py`—was a valuable learning curve. Implementing custom logging, file-based state retention, and parameter parsing in `simple_node` effectively bridged the gap between standard scripting and distributed software. I can clearly see how these fundamental concepts of nodes and topics will be essential for integrating hardware interfaces, like microcontrollers and data acquisition sensors, in future automation tasks. Overall, this lab established a strong, practical foundation for developing more complex robotic systems.