#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/detail/laser_scan__struct.hpp"
#include "std_msgs/msg/detail/int16__struct.hpp"
#include "std_msgs/msg/string.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class LaserScan : public rclcpp::Node
{
  public:
    LaserScan()
    : Node("Laser_scan"), count_(0)
    {
      publisher_1 = this->create_publisher<std_msgs::msg::String>("topic", 10);
      timer_1 = this->create_wall_timer(
      500ms, std::bind(&LaserScan::timer_callback, this));
      publisher_2 = this->create_publisher<sensor_msgs::msg::LaserScan>("scan", 10);
      timer_2 = this->create_wall_timer(
      500ms, std::bind(&LaserScan::timer_callback2, this));
    }

  private:
    void timer_callback()
    {
      auto message = std_msgs::msg::String();
      message.data = "Laser data " + std::to_string(count_++);
      RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
      publisher_1->publish(message);
    }
    
    void timer_callback2()
    {
      auto laser_msg = sensor_msgs::msg::LaserScan();
      laser_msg.header.frame_id = "laser_frame";
      laser_msg.header.stamp = this->now();
      laser_msg.angle_min = 0.0;
      laser_msg.angle_max = 2.0 * M_PI;
      laser_msg.angle_increment = 0.1;
      laser_msg.time_increment = 0.001;
      laser_msg.scan_time = 0.1;
      laser_msg.range_min = 0.0;
      laser_msg.range_max = 10.0;
      for (double angle = laser_msg.angle_min; angle <= laser_msg.angle_max; angle += laser_msg.angle_increment)
      {
       laser_msg.ranges.push_back(5.0 + 3.0 * std::sin(angle));
      }
      //RCLCPP_INFO(this->get_logger(), "Publishing: '%d'", laser_msg.data);

      publisher_2->publish(laser_msg);

    }
    
    rclcpp::TimerBase::SharedPtr timer_1;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_1;
    rclcpp::TimerBase::SharedPtr timer_2;
    rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr publisher_2;
    
   size_t count_;

};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<LaserScan>());
  rclcpp::shutdown();
  return 0;
}
