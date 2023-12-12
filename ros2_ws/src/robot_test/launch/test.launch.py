from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    talker = Node(
    package = "demo_nodes_cpp",
    executable = "talker",
    name = "my_talk",
    remappings=[("/chatter" , "/my_chatter")],
    parameters=[
        {"param_name" : "value"},
        {"param2" : 19}
    ]
    
    )
    listener = Node(
    package  = "demo_nodes_py",
    executable = "listener",
    remappings=[("/chatter" , "/my_chatter")]

    
    )
    ld.add_action(talker)
    ld.add_action(listener)
    
    return ld
