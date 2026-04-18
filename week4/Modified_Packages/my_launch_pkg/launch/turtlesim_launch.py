from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        # Starts the main simulator [cite: 212-215]
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        # Starts the keyboard teleop in a new window [cite: 216-218]
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e'
        ),
        # Task 1: Automatically spawn a second turtle at (x=2, y=2) [cite: 249]
        ExecuteProcess(
            cmd=[['ros2 service call /spawn turtlesim/srv/Spawn "{x: 2.0, y: 2.0, theta: 0.0, name: \'turtle2\'}"']],
            shell=True
        )
    ])