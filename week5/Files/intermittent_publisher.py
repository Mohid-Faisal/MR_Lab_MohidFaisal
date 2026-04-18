import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SmoothIntermittentPublisher(Node):
    def __init__(self):
        super().__init__('intermittent_publisher')
        # Publisher for the /cmd_vel topic 
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Control variables
        self.target_velocity = 0.2
        self.current_velocity = 0.0
        self.kp = 0.1  # Proportional gain for smooth acceleration

        # Timer 1: State switching every 2 seconds 
        self.switch_timer = self.create_timer(2.0, self.switch_state_callback)

        # Timer 2: High-frequency control loop (20 Hz)
        self.control_timer = self.create_timer(0.05, self.control_loop_callback)

        self.get_logger().info("Smooth Intermittent Publisher Started.")

    def switch_state_callback(self):
        # Toggle target velocity between 0.2 and 0.0
        if self.target_velocity > 0.0:
            self.target_velocity = 0.0
            self.get_logger().info("State: STOPPING")
        else:
            self.target_velocity = 0.2
            self.get_logger().info("State: MOVING FORWARD")

    def control_loop_callback(self):
        # P-Controller logic
        error = self.target_velocity - self.current_velocity
        self.current_velocity += self.kp * error

        # Publish the smoothed velocity
        msg = Twist()
        msg.linear.x = self.current_velocity
        msg.angular.z = 0.0
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SmoothIntermittentPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()