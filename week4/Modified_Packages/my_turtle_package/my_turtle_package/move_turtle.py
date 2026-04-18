import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import math

class InfiniteTurtleController(Node):
    def __init__(self):
        super().__init__('infinite_turtle_controller')
        
        # 1. Setup Service Client for Spawning
        self.spawner = self.create_client(Spawn, 'spawn')
        while not self.spawner.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for turtlesim spawn service...')

        # 2. Spawn Turtle 2 (Triangle) and Turtle 3 (Square)
        self.spawn_turtle(2.0, 2.0, 0.0, 'turtle2')
        self.spawn_turtle(8.0, 8.0, 0.0, 'turtle3')

        # 3. Publishers
        self.pub1 = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        
        # State variables for Turtle 2 (Triangle)
        self.t2_state = "MOVE" 
        self.t2_timer_count = 0

        # State variables for Turtle 3 (Square)
        self.t3_state = "MOVE"
        self.t3_timer_count = 0
        
        # Timer runs every 0.1 seconds (10Hz)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def spawn_turtle(self, x, y, theta, name):
        """Helper function to send a spawn request"""
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name
        # We use call_async so we don't block the main thread
        self.spawner.call_async(request)
        self.get_logger().info(f'Request sent to spawn {name}')

    def timer_callback(self):
        # --- TURTLE 1: INFINITE CIRCLE ---
        circ_msg = Twist()
        circ_msg.linear.x = 2.0
        circ_msg.angular.z = 1.0 
        self.pub1.publish(circ_msg)

        # --- TURTLE 2: INFINITE TRIANGLE ---
        tri_msg = Twist()
        self.t2_timer_count += 1
        if self.t2_state == "MOVE":
            tri_msg.linear.x = 2.0
            if self.t2_timer_count > 20:
                self.t2_state = "TURN"
                self.t2_timer_count = 0
        elif self.t2_state == "TURN":
            tri_msg.angular.z = 2.094  # 120 degrees
            if self.t2_timer_count > 10:
                self.t2_state = "MOVE"
                self.t2_timer_count = 0
        self.pub2.publish(tri_msg)

        # --- TURTLE 3: INFINITE SQUARE ---
        sq_msg = Twist()
        self.t3_timer_count += 1
        if self.t3_state == "MOVE":
            sq_msg.linear.x = 2.0
            if self.t3_timer_count > 20:
                self.t3_state = "TURN"
                self.t3_timer_count = 0
        elif self.t3_state == "TURN":
            sq_msg.angular.z = 1.571  # 90 degrees
            if self.t3_timer_count > 10:
                self.t3_state = "MOVE"
                self.t3_timer_count = 0
        self.pub3.publish(sq_msg)

def main(args=None):
    rclpy.init(args=args)
    node = InfiniteTurtleController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()