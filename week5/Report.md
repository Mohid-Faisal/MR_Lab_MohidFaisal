# Lab Session 5: Gazebo Simulation and SLAM with TurtleBot3

## 1. Approach and Tasks
I configured the workspace for the TurtleBot3 'burger' model and launched the Gazebo environment alongside Cartographer for SLAM. I utilized RViz to visualize LiDAR scans and coordinate transforms (TF).

## 2. Implementation
* **Intermittent Publisher**: I implemented a node that alternates between forward motion (0.2 m/s) and a stop state every 2 seconds using a timer. 
* **Odom Subscriber**: I created a subscriber for the `/odom` topic (nav_msgs/msg/Odometry) to print real-time X/Y coordinates.

## 3. Observations and Discrepancies
* **Motion Issues**: During teleoperation, I observed that high-speed turns or collisions caused the robot to 'trip' in Gazebo, leading to odometry drift and map corruption.
* **Coordinate Frames**: The TF tree showed that the `map` frame is fixed, while the `base_link` moves relative to `odom` based on wheel encoder data.

## 4. Conclusion
This lab provided hands-on experience with 3D simulation and SLAM. I learned how sensor data (LiDAR) and odometry are fused to create an occupancy grid map.
