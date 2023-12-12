#include "rclcpp/rclcpp.hpp"

class My_cpp_py_pkg : public rclcpp::Node
{
    public:
        My_cpp_py_pkg() : Node("my_cpp_py_node")
        {
            RCLCPP_INFO(this->get_logger(), "Hello from ROS2");

        }
private:
};
