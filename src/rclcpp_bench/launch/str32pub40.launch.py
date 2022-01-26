from launch import LaunchDescription
from launch_ros.actions import Node

str_length = '32'
num_pub = '40'


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
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub20',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub20.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub21',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub21.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub22',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub22.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub23',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub23.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub24',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub24.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub25',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub25.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub26',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub26.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub27',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub27.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub28',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub28.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub29',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub29.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub30',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub30.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub31',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub31.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub32',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub32.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub33',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub33.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub34',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub34.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub35',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub35.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub36',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub36.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub37',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub37.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub38',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub38.csv', str_length]
        ),
        Node(
            package='rclcpp_bench',
            executable='pub_string',
            name='pub39',
            arguments=['./results/string/pNs1/' +
                       str_length + '/' + num_pub + '/pub39.csv', str_length]
        ),
    ])
