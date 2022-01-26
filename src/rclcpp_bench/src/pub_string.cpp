#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <sys/time.h>
#include <fstream>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std::chrono_literals;

/* definition for evaluation */
#define eval_interval 1000ms
#define sleep_before_pub_end 5000ms
#define num_comm 10

int str_length;
std::vector<std::string> results;

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
    message.data = Random_String::get_random_string(str_length);
    //RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());

    auto result = std::chrono::system_clock::now();
    publisher_->publish(message);

    //RCLCPP_INFO(this->get_logger(), "clock: %ld", result);
    auto result_us = std::chrono::duration_cast<std::chrono::microseconds>(result.time_since_epoch()).count();
    results.emplace_back(message.data + "," + std::to_string(result_us));

    count_++;
    if (count_ >= num_comm)
    {
      rclcpp::sleep_for(sleep_before_pub_end);
      auto end_message = std_msgs::msg::String();
      end_message.data = "end";
      publisher_->publish(end_message);
      rclcpp::shutdown();
    }
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
  size_t count_;
};

int main(int argc, char *argv[])
{
  std::string filename = argv[1];
  str_length = atoi(argv[2]);

  rclcpp::init(argc, argv);

  rclcpp::spin(std::make_shared<MinimalPublisher>());
  rclcpp::shutdown();

  std::ofstream ofs(filename);
  for (size_t i = 0; i < results.size(); ++i)
  {
    ofs << results.at(i) << std::endl;
  }

  return 0;
}