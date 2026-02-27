# Post-Lab Questions

**1. Define: node, topic, package, workspace. Provide one sentence each.**
* **Node:** A standalone process that performs specific computations or tasks within the ROS 2 graph.
* **Topic:** A named communication channel where nodes publish and subscribe to stream messages asynchronously.
* **Package:** An organized directory containing ROS 2 code, dependencies, and build configurations required to create a functional software unit.
* **Workspace:** A central directory where multiple ROS 2 packages are grouped together, compiled, and installed.

**2. Explain why sourcing is required. What happens if you do not source a workspace?**
Sourcing overlays the workspace's environment variables onto your current terminal session so the system knows where to find your ROS 2 installations and custom packages. If you do not source a workspace, commands like `ros2 run` will fail with an error stating the package or command cannot be found.

**3. What is the purpose of `colcon build`? What folders does it generate?**
The `colcon build` command compiles the source code and builds the packages located in the `src` directory. Upon execution, it generates three new folders in the workspace: `build/`, `install/`, and `log/`.

**4. In your own words, explain what the `entry_points` console script does in `setup.py`.**
The `entry_points` dictionary registers a specific Python function (like `main`) as a standalone executable command, telling ROS 2 exactly which script to run when the user executes a command like `ros2 run my_first_pkg simple_node`.

**5. Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected by a topic.**
+-----------------------+                         +-----------------------+
|    Publisher Node     |                         |    Subscriber Node    |
|     (e.g., Lidar)     |                         | (e.g., Obstacle Avoid)|
|                       |      /scan_data         |                       |
|   Publishes Message   +------------------------>+   Receives Message    |
|                       |                         |                       |
+-----------------------+                         +-----------------------+