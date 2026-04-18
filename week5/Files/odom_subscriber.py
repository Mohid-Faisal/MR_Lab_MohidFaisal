import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):
    def __init__(self):
        super().__init__('odom_subscriber')
        # Subscriber for the /odom topic 
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        self.get_logger().info("Odometry Subscriber Started.")

    def listener_callback(self, msg):
        # Extract X and Y coordinates from the Odometry message [cite: 347]
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        
        # Print out the received messages [cite: 347]
        self.get_logger().info(f'Robot Coordinates -> X: {x:.3f}, Y: {y:.3f}')
        
def main(args=None):
    rclpy.init(args=args)
    node = OdomSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()