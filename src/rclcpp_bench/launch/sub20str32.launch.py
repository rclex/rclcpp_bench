from launch import LaunchDescription
from launch_ros.actions import Node

num_sub = '20'
str_length = '32'


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub00',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub00.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub01',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub01.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub02',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub02.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub03',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub03.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub04',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub04.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub05',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub05.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub06',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub06.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub07',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub07.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub08',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub08.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub09',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub09.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub10',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub10.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub11',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub11.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub12',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub12.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub13',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub13.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub14',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub14.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub15',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub15.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub16',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub16.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub17',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub17.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub18',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub18.csv']
        ),
        Node(
            package='rclcpp_bench',
            executable='sub_string',
            name='sub19',
            arguments=['./results/string/p1sN/' +
                       str_length + '/' + num_sub + '/sub19.csv']
        ),
    ])
