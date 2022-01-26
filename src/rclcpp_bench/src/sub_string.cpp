#include <memory>
#include <fstream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
using std::placeholders::_1;

using namespace std::chrono_literals;

std::vector<std::string> results;

class MinimalSubscriber : public rclcpp::Node
{
public:
  MinimalSubscriber()
      : Node("sub_node")
  {
    subscription_ = this->create_subscription<std_msgs::msg::String>(
        "testtopic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
  }

private:
  void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
  {
    auto result = std::chrono::system_clock::now();
    //RCLCPP_INFO(this->get_logger(), "I heard: '%s'", msg->data.c_str());

    std::string msg_string = msg->data.c_str();
    if (msg_string == "end")
    {
      rclcpp::sleep_for(1000ms);
      rclcpp::shutdown();
    }
    else
    {
      //RCLCPP_INFO(this->get_logger(), "clock: %ld", result);
      auto result_us = std::chrono::duration_cast<std::chrono::microseconds>(result.time_since_epoch()).count();
      results.emplace_back(msg_string + "," + std::to_string(result_us));
    }
  }
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char *argv[])
{
  std::string filename = argv[1];

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();

  std::ofstream ofs(filename);
  for (size_t i = 0; i < results.size(); ++i)
  {
    ofs << results.at(i) << std::endl;
  }

  return 0;
}