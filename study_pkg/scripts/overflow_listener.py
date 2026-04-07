#!/usr/bin/env python3
"""Узел, который слушает сообщения о переполнении"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')
        
        # Объявляем параметры
        self.declare_parameter('overflow_topic', '/overflow')
        self.declare_parameter('enable_logging', True)
        
        # Читаем параметры
        self.overflow_topic = self.get_parameter('overflow_topic').get_parameter_value().string_value
        self.logging = self.get_parameter('enable_logging').get_parameter_value().bool_value
        
        # Подписываемся на топик
        self.subscription = self.create_subscription(
            Int32,
            self.overflow_topic,
            self.callback,
            10
        )
        
        if self.logging:
            self.get_logger().info(f'Слушатель запущен! Слушаю топик {self.overflow_topic}')

    def callback(self, msg):
        self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Получено значение: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Узел остановлен')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
