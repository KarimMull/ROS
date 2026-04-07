#!/usr/bin/env python3
"""Узел, который публикует чётные числа и отправляет уведомление о переполнении"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Объявляем параметры
        self.declare_parameter('publish_frequency', 10.0)  # Гц
        self.declare_parameter('overflow_threshold', 100)   # порог переполнения
        self.declare_parameter('numbers_topic', '/even_numbers')
        self.declare_parameter('overflow_topic', '/overflow')
        self.declare_parameter('enable_logging', True)
        
        # Читаем параметры
        self.freq = self.get_parameter('publish_frequency').get_parameter_value().double_value
        self.threshold = self.get_parameter('overflow_threshold').get_parameter_value().integer_value
        self.numbers_topic = self.get_parameter('numbers_topic').get_parameter_value().string_value
        self.overflow_topic = self.get_parameter('overflow_topic').get_parameter_value().string_value
        self.logging = self.get_parameter('enable_logging').get_parameter_value().bool_value
        
        # Публикаторы
        self.publisher = self.create_publisher(Int32, self.numbers_topic, 10)
        self.overflow_publisher = self.create_publisher(Int32, self.overflow_topic, 10)
        
        # Таймер с параметризуемой частотой
        self.timer = self.create_timer(1.0 / self.freq, self.timer_callback)
        
        self.counter = 0
        
        if self.logging:
            self.get_logger().info(f'Издатель запущен: {self.freq}Гц, порог={self.threshold}, топики: {self.numbers_topic} и {self.overflow_topic}')

    def timer_callback(self):
        # Публикуем текущее чётное число
        msg = Int32()
        msg.data = self.counter
        self.publisher.publish(msg)
        
        if self.logging:
            self.get_logger().info(f'Опубликовано: {self.counter}')
        
        # Проверяем на переполнение
        if self.counter >= self.threshold:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_publisher.publish(overflow_msg)
            
            if self.logging:
                self.get_logger().warn(f'ПЕРЕПОЛНЕНИЕ! Опубликовано значение {self.counter} в топик {self.overflow_topic}')
            
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Узел остановлен')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
