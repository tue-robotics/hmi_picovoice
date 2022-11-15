cmake_minimum_required(VERSION 3.0.2)
project(hmi_picovoice)

find_package(catkin REQUIRED COMPONENTS
  actionlib
  hmi
  picovoice_msgs
  rospy
)

catkin_python_setup()

catkin_package()

#############
## Install ##
#############

catkin_install_python(PROGRAMS
  scripts/${PROJECT_NAME}_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
