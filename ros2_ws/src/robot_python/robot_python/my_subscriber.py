#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import random

class temperature_out(Node):
    def __init__(self):
        super().__init__("temperature_output")
        self.temperature_sub = self.create_subscription(Int64, "temperature",self.sub_temperature, 10)


    def sub_temperature(self,msg):
        self.get_logger().info(str(msg.data))




def main(args=None):
    rclpy.init(args=args)
    node = temperature_out()
    rclpy.spin(node)
    rclpy.shutdown()
        
if __name__ == "__main__":
    main()