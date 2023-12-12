import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial
import math

class TurtlesimController(Node):

    def __init__(self):
        super().__init__('turtlesim_controller')
        self.previous_x = 0
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)
        self.subscription_

        # Set the rate at which to send commands
        self.timer = self.create_timer(1.0, self.timer_callback)

    def pose_callback(self, pose: Pose):
        self.get_logger().info(
            'Turtle Pose - X: %f, Y: %f, Theta: %f' %
            (pose.x, pose.y, pose.theta))


        if pose.x > 1.0 and self.previous_x <= 1.0:
            self.previous_x = pose.x
            self.get_logger().info("Turn into Red")
            self.call_set_pen_service(255,0,0,3,0)
        elif pose.x < 1.0 and self.previous_x > 1.0:
            self.previous_x = pose.x
            self.get_logger().info("Turn into Green")
            self.call_set_pen_service(0,255,0,3,0)


    def timer_callback(self):
        # Command the turtle to move in a circle
        twist_msg = Twist()
        twist_msg.linear.x = 1.0
        twist_msg.angular.z = 1.0
        self.publisher_.publish(twist_msg)

    def call_set_pen_service(self,r,g,b,width,off):
        client = self.create_client(SetPen,"turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger.warn("Waitttt")

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))


    def callback_set_pen(self,future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger.error("Failed")




def main(args=None):
    rclpy.init(args=args)
    controller_node = TurtlesimController()
    rclpy.spin(controller_node)
    controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
