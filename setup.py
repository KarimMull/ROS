from setuptools import setup
import os
from glob import glob

package_name = 'study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Добавляем поддержку launch-файлов
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kmull',
    maintainer_email='kmullayanov@duck.com',
    description='Study package for ROS 2 Jazzy',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'first_node = study_pkg.scripts.first_node:main',
            'time_printer = study_pkg.scripts.time_printer:main',
            'even_number_publisher = study_pkg.scripts.even_number_publisher:main',
            'overflow_listener = study_pkg.scripts.overflow_listener:main',
        ],
    },
)
