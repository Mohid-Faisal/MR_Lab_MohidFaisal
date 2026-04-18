# Lab Session 4: ROS 2 Launch, Rosbag, and rqt_plot

## 1. Approach and Implementation
* **ROS 2 Launch:** I created a package named `my_launch_pkg` and developed a Python launch file to automate the startup of the `turtlesim_node` and `turtle_teleop_key`. I used `ExecuteProcess` to automate the spawning of a second turtle, ensuring a multi-robot environment from a single command.
* **Data Recording:** I used `ros2 bag record` to capture the velocity and pose topics. This allowed for offline analysis and the ability to replay exact robot movements.
* **Follow-the-Leader Node:** I implemented a Proportional (P) Controller node where `turtle2` calculates Euclidean distance and angular error relative to `turtle1`'s pose to maintain a following behavior.

## 2. Brief Analysis of Findings
* **Control Response:** Analysis via `rqt_plot` showed that the follower turtle's velocity commands closely mirrored the leader's with a small time lag, characteristic of a feedback control loop.
* **Trajectory Data:** The recorded rosbag file confirms that `turtle2` effectively converged on the leader's coordinates whenever the distance error exceeded the defined threshold.
* **Launch Efficiency:** Utilizing launch files eliminated the need for multiple terminal windows, significantly streamlining the deployment of complex multi-node systems.

## 3. Observations
* Replaying `cmd_vel` (input) is necessary for the turtle to move during playback, whereas replaying `pose` (output) only shows data without affecting the simulator.
* Normalizing the angle error in the follow-the-leader code is critical to prevent the follower turtle from spinning 360 degrees when crossing the radian boundary.
