from launch import LaunchDescription
from launch_ros.actions import Node

num_pub = '20'
str_length = '64'


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub00',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub00.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub01',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub01.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub02',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub02.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub03',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub03.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub04',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub04.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub05',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub05.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub06',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub06.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub07',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub07.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub08',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub08.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub09',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub09.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub10',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub10.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub11',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub11.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub12',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub12.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub13',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub13.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub14',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub14.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub15',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub15.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub16',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub16.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub17',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub17.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub18',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub18.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub19',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub19.csv', str_length]
        ),
    ])
