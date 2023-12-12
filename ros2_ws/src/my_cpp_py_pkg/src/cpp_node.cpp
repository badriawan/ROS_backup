
#include "rclcpp/rclcpp.hpp"
#include "my_cpp_py_pkg/cpp_header.hpp"

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("My_cpp_py_pkg");
    rclcpp::spin(node);
    rclcpp::shutdown();
}