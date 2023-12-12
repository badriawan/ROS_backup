from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robot_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/robot_python.launch.py'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts':[
        "test_node = robot_python.my_first_node:main",
        "my_publisher = robot_python.my_publisher:main",
        "my_subscriber = robot_python.my_subscriber:main",
        "my_service = robot_python.my_service:main",
        "my_subtest = robot_python.my_subtest:main",
        "turtlesim_go = robot_python.turtlesim_go:main"
        ],
          'launch.frontend': [
            'launch = launch:robot_python.launch[launch.frontend]',
        ],
    },
)
