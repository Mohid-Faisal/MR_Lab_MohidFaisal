# Lab Report: ROS 2 Workspace and Turtle Control

## Objectives
* Set up a ROS 2 workspace.
* Initialize Git for version control.
* Create a new Python-based ROS 2 package.
* Develop a node to control turtlesim movement patterns.

## Tasks Performed
### 1. Workspace Setup
I created the workspace directory `~/ros2_ws/src` and built it using `colcon build`. I also configured the `.bashrc` to source the workspace automatically.

### 2. Version Control
I initialized a Git repository in the `src` folder and configured my global username and email.

### 3. Package Creation
I created `my_turtle_package` with dependencies on `rclpy` and `turtlesim`.

### 4. Turtle Control
I developed `move_turtle.py` to publish `Twist` messages to the `turtle1/cmd_vel` topic. The script was modified to handle multiple turtles and complex patterns including circles and triangles.

## Conclusion
The lab successfully demonstrated the fundamentals of ROS 2 package management and basic robot motion control via topic publishing.
