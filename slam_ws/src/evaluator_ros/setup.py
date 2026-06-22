from setuptools import find_packages, setup

package_name = 'evaluator_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/evaluator.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhirup',
    maintainer_email='pingking29705@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pose_comparator = evaluator_ros.pose_comparator:main',
            'trajectory_evaluator = evaluator_ros.trajectory_evaluator:main',
            'resource_monitor = evaluator_ros.resource_monitor:main',
            'metrics_publisher = evaluator_ros.metrics_publisher:main',
        ],
    },
)
