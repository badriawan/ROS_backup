#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import random

class temperature_data(Node):
    def __init__(self):
        super().__init__("temperature_sensor")
        self.temperature_publisher = self.create_publisher(Int64, "temperature", 10)
        self.temperature_timer = self.create_timer(2.0, self.publish_temperature)        


    def publish_temperature(self):
        self.get_temperature = random.randint(20, 30)
        msg = Int64()
        msg.data = self.get_temperature
        self.temperature_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = temperature_data()
    rclpy.spin(node)
    rclpy.shutdown()
        
if __name__ == "__main__":
    main()