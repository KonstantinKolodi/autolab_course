from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/maps', glob('maps/*')),
        # Launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # World files
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
    ],
    install_requires=['setuptools', 'rclpy'],
    zip_safe=True,
    maintainer='konstantin',
    maintainer_email='kokolo@taltech.ee',
    description='A robot controller package for ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "mapping = my_robot_controller.mapping:main",
            "navigation = my_robot_controller.navigation:main",
            "av_nav = my_robot_controller.aw_navigation:main",
        ],
    },
)

