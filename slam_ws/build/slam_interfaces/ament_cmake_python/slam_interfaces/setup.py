from setuptools import find_packages
from setuptools import setup

setup(
    name='slam_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('slam_interfaces', 'slam_interfaces.*')),
)
