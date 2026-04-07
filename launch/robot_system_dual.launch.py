#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def launch_setup(context, *args, **kwargs):
    mode = LaunchConfiguration('mode').perform(context)
    
    if mode == 'fast':
        freq = 20.0
        threshold = 50
        numbers_topic = '/even_numbers_fast'
        overflow_topic = '/overflow_fast'
        print(f"🚀 БЫСТРЫЙ РЕЖИМ: {freq}Гц, порог {threshold}")
    else:  # slow по умолчанию
        freq = 5.0
        threshold = 150
        numbers_topic = '/even_numbers_slow'
        overflow_topic = '/overflow_slow'
        print(f"🐢 МЕДЛЕННЫЙ РЕЖИМ: {freq}Гц, порог {threshold}")
    
    return [
        Node(
            package='study_pkg',
            executable='even_number_publisher',
            name='even_pub',
            output='screen',
            parameters=[
                {'publish_frequency': freq},
                {'overflow_threshold': threshold},
                {'numbers_topic': numbers_topic},
                {'overflow_topic': overflow_topic},
                {'enable_logging': True},
            ],
        ),
        Node(
            package='study_pkg',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
            parameters=[
                {'overflow_topic': overflow_topic},
                {'enable_logging': True},
            ],
        ),
    ]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'mode',
            default_value='slow',
            description='Режим: fast (20Гц, порог50) или slow (5Гц, порог150)'
        ),
        OpaqueFunction(function=launch_setup)
    ])
