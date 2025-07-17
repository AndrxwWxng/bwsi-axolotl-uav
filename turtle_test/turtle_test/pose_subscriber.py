#!/usr/bin.env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
#if you import more libraries, add them to dependencies in package.xml
class PosSubNode(Node):
    def __init__(self):
        super().__init__('pose_subscriber')
        self.get_logger().info('Position node has started')
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
        # Add your node logic here
        # For example, you can create a timer, subscribe to topics, etc.
    def pose_callback(self, msg:Pose):
        self.get_logger().info('('+str(msg.x)+', '+str(msg.y)+str(msg.theta)+')')

def main(args=None):
    rclpy.init(args=args)
    node = PosSubNode()
    rclpy.spin(node) #Loops the node
    rclpy.shutdown()


if __name__=='__main__':#Unneeded if you only ever run the node directly with ros2 run 
    main()
