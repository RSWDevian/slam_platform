from setuptools import find_packages, setup

package_name = 'platform_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/platform.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='abhirup',
    maintainer_email='pingking29705@gmail.com',
    description='Top-level launch file composing the full SLAM platform stack.',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
