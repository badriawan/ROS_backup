from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    my_publisher = Node(
    package = "robot_python",
    executable = "my_publisher",
    name = "my_publisher"
   
    
    )
    my_subscriber = Node(
    package  = "robot_python",
    executable = "my_subscriber",
    name = "my_subscriber"
    
    )
    ld.add_action(my_publisher)
    ld.add_action(my_subscriber)
    
    return ld
