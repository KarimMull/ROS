from setuptools import setup

package_name = 'super_karim_study_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kmull',
    maintainer_email='kmullayanov@duck.com',
    description='Super study package with time printer node',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'time_printer = super_karim_study_pkg.scripts.time_printer:main',
           'even_number_publisher = super_karim_study_pkg.scripts.even_number_publisher:main',
           'overflow_listener = super_karim_study_pkg.scripts.overflow_listener:main',
        ],
    },
)
