from setuptools import find_packages, setup

package_name = 'sensor_adapter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/sensor_adapter.launch.py']),
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
            "camera_adapter = sensor_adapter.camera_adapter:main",
            "camera_info_adapter = sensor_adapter.camera_info_adapter:main",
            "imu_adapter = sensor_adapter.imu_adapter:main",
            "odom_adapter = sensor_adapter.odom_adapter:main",
            "lidar_adapter = sensor_adapter.lidar_adapter:main"
        ],
    },
)
