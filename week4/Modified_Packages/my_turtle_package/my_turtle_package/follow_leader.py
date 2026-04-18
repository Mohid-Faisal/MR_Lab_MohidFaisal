import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class FollowerNode(Node):
    def __init__(self):
        super().__init__('follower_node')
        # Subscribing to both poses to calculate relative distance 
        self.leader_pose = None
        self.follower_pose = None
        
        self.sub_leader = self.create_subscription(Pose, '/turtle1/pose', self.leader_callback, 10)
        self.sub_follower = self.create_subscription(Pose, '/turtle2/pose', self.follower_callback, 10)
        self.publisher = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        
        # Control Loop Timer (20Hz)
        self.create_timer(0.05, self.control_loop)

    def leader_callback(self, msg):
        self.leader_pose = msg

    def follower_callback(self, msg):
        self.follower_pose = msg

    def control_loop(self):
        if self.leader_pose is None or self.follower_pose is None:
            return

        # Calculate Euclidean Distance
        dx = self.leader_pose.x - self.follower_pose.x
        dy = self.leader_pose.y - self.follower_pose.y
        distance = math.sqrt(dx**2 + dy**2)

        msg = Twist()
        # Only move if the leader is more than 1 unit away
        if distance > 1.0:
            # Linear Velocity (P-Control)
            msg.linear.x = 1.5 * distance
            
            # Angular Velocity (Target Angle - Current Angle)
            goal_theta = math.atan2(dy, dx)
            angle_error = goal_theta - self.follower_pose.theta
            
            # Normalize angle to prevent erratic spinning
            if angle_error > math.pi: angle_error -= 2*math.pi
            if angle_error < -math.pi: angle_error += 2*math.pi
            
            msg.angular.z = 6.0 * angle_error
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FollowerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()