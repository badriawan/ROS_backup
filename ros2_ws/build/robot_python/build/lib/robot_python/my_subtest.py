import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from example_interfaces.msg import Int64
from example_interfaces.msg import String
from example_interfaces.srv import SetBool



class my_subtest(Node):

    def __init__(self):
        super().__init__("subtest_node")
        #self.subscriber = self.create_subscription(Pose, "/turtle1/pose",self.sub_callback, 10)
        #self.publisher = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.publisher2 = self.create_publisher(Int64,"number",10)
        self.timer = self.create_timer(1.0,self.publish_number)
        self.subscriber2 = self.create_subscription(Int64,"number",self.call_number,10)
        #self.publisher3 = self.create_publisher(Int64,"string",10)
        self.create_service(SetBool,"start_robot",self.call_start_robot)


    # def sub_callback(self, pose: Pose):
    #     msg = Twist()
    #     msg.linear.x = 1.0
    #     msg.angular.z = 0.5
    #     self.publisher.publish(msg)

    def publish_number(self):
        #self.get_num = random.randint(20, 30)
        msg2 = Int64()
        msg2.data = 5
        self.publisher2.publish(msg2)
    
    def call_number(self,msg3):
        # msg3 = String()
        # msg3.data = "Hello"
        self.get_logger().info(str(msg3))

    def call_start_robot(self,request:SetBool.Request,response:SetBool.Response):
        if request.data:
            self.get_logger().info("Start Robot")
        else:
            self.get_logger().info("Stop Robot")
        response.success = False
        return response





def main(args = None):
    rclpy.init(args=args)
    node = my_subtest()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()