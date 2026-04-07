#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='study_pkg',
            executable='even_number_publisher',
            name='even_pub',
            output='screen',
            parameters=[
                {'publish_frequency': 8.0},      # 8 Гц вместо 10
                {'overflow_threshold': 80},      # порог 80 вместо 100
                {'numbers_topic': '/even_numbers'},
                {'overflow_topic': '/overflow'},
                {'enable_logging': True},
            ],
        ),
        Node(
            package='study_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
            parameters=[
                {'overflow_topic': '/overflow'},
                {'enable_logging': True},
            ],
        ),
    ])
