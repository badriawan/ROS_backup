import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtlesimGoToGoal(Node):

    def __init__(self):
        super().__init__('turtlesim_goto_goal')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscription_ = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)
        self.subscription_
        self.timer = self.create_timer(1.0, self.pose_callback)        
        self.current_pose = Pose()


    def pose_callback(self, msg):
        self.current_pose = msg
        self.get_logger().info(
            'Turtle Pose - X: %f, Y: %f, Theta: %f' %
            (self.current_pose.x, self.current_pose.y, self.current_pose.theta))
        
        # Example: Send a goal to move to (x=5.0, y=5.0)
        self.send_goal(5.0, 10.0)

    def send_goal(self, goal_x, goal_y):
        # Calculate the angle to the goal
        angle_to_goal = math.atan2(goal_y - self.current_pose.y, goal_x - self.current_pose.x)

        # Calculate the angular velocity to reach the goal
        angular_velocity = 2.0 * (angle_to_goal - self.current_pose.theta)

        # Create Twist message to command the turtle
        twist_msg = Twist()
        twist_msg.linear.x = 1.0  # Linear velocity
        twist_msg.angular.z = angular_velocity  # Angular velocity

        # Publish the Twist message
        self.publisher_.publish(twist_msg)

        self.get_logger().info(f'Sending goal: X={goal_x}, Y={goal_y}')

    def spin(self):
        rclpy.spin(self)

    def destroy(self):
        self.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    turtlebot_node = TurtlesimGoToGoal()
    try:
        turtlebot_node.spin()
    finally:
        turtlebot_node.destroy()

if __name__ == '__main__':
    main()
