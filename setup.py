#
# Copyright (c) 2022, TU/e Robotics
# All rights reserved.
#
# Author: Rein Appeldoorn

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['hmi_picovoice'],
    package_dir={'': 'src'},
)

setup(**d)
