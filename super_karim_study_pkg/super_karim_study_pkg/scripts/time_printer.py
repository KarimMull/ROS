#!/usr/bin/env python3
"""Узел, который каждые 5 секунд выводит текущее время"""

import rclpy
from rclpy.node import Node
from datetime import datetime

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        # Создаём таймер с интервалом 5 секунд
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info('Узел time_printer запущен! Ожидайте вывод времени каждые 5 секунд')

    def timer_callback(self):
        # Получаем текущее время в формате ЧЧ:ММ:СС
        current_time = datetime.now().strftime('%H:%M:%S')
        self.get_logger().info(f'Текущее время: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Узел time_printer остановлен пользователем')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
