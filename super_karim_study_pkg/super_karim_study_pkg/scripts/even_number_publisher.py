#!/usr/bin/env python3
"""Узел, который публикует чётные числа и отправляет уведомление о переполнении"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        
        # Публикатор для чётных чисел
        self.publisher = self.create_publisher(Int32, '/even_numbers', 10)
        
        # Публикатор для переполнения
        self.overflow_publisher = self.create_publisher(Int32, '/overflow', 10)
        
        # Таймер на 10 Гц
        self.timer = self.create_timer(0.1, self.timer_callback)
        
        # Счётчик
        self.counter = 0
        
        self.get_logger().info('Узел even_pub запущен! Публикуем чётные числа 10 Гц')

    def timer_callback(self):
        # Публикуем текущее чётное число
        msg = Int32()
        msg.data = self.counter
        self.publisher.publish(msg)
        self.get_logger().info(f'Опубликовано: {self.counter}')
        
        # Проверяем на переполнение
        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.overflow_publisher.publish(overflow_msg)
            self.get_logger().warn(f'ПЕРЕПОЛНЕНИЕ! Опубликовано значение {self.counter} в топик /overflow')
            self.counter = 0
        else:
            # Увеличиваем на 2
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
