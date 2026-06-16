import os
from glob import glob
from setuptools import setup

PACKAGE_NAME = 'manufacturing_tb'

setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    packages=[PACKAGE_NAME],
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages',
            ['resource/' + PACKAGE_NAME]),
        # Include our package.xml file
        (os.path.join('share', PACKAGE_NAME), ['package.xml']),
        # Include all launch files.
        (os.path.join('share', PACKAGE_NAME, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', PACKAGE_NAME, 'config'), glob(os.path.join('config', '*.yaml'))) 
    ],
    install_requires=['setuptools'],
    zip_safe=True
)