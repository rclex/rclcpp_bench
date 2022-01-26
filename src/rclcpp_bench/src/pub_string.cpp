#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

#include <sys/time.h>

using namespace std::chrono_literals;

#define eval_interval 100ms

int str_length;

class Random_String
{
public:
  static std::string get_random_string(const int len)
  {
    static const char alphanum[] =
        "0123456789"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz";

    struct timeval tv;
    gettimeofday(&tv, NULL);
    srand(tv.tv_sec + tv.tv_usec);
    std::string random_string;
    for (int i = 0; i < len; ++i)
    {
      random_string += alphanum[rand() % (sizeof(alphanum) - 1)];
    }

    return random_string;
  }
};

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class MinimalPublisher : public rclcpp::Node
{
public:
  MinimalPublisher()
      : Node("pub_node"), count_(0)
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("testtopic", 10);
    timer_ = this->create_wall_timer(
        eval_interval, std::bind(&MinimalPublisher::timer_callback, this));
  }

private:
  void timer_callback()
  {
    auto message = std_msgs::msg::String();
    message.data = std::to_string(count_++) + Random_String::get_random_string(str_length);
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char *argv[])
{
  if (argc != 3)
  {
    printf("arguments are needed %d\n", argc);
    return 1;
  }
  std::string filename = argv[1];
  str_length = atoi(argv[2]);

  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();
  return 0;
}