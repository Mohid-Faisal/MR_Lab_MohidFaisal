import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        self.declare_parameter('student_name', 'student_name not set')
        student_name = self.get_parameter('student_name').get_parameter_value().string_value
        
        self.get_logger().info('Welcome to Mobile Robotics Lab')
        
        if student_name == 'student_name not set':
            self.get_logger().info('student_name not set')
        else:
            self.get_logger().info(f'Student Name: {student_name}')
            
        script_dir = os.path.dirname(os.path.realpath(__file__))
        counter_file = os.path.join(script_dir, 'run_counter.txt')
        
        count = 1
        if os.path.exists(counter_file):
            with open(counter_file, 'r') as f:
                content = f.read().strip()
                if content.isdigit():
                    count = int(content) + 1
                    
        self.get_logger().info(f'Run count: {count}')
        
        with open(counter_file, 'w') as f:
            f.write(str(count))

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    
    rclpy.spin_once(node, timeout_sec=0.1)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
