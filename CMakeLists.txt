cmake_minimum_required(VERSION 3.0.2)
project(hmi_picovoice)

#add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  roslib
)

catkin_package(
  CATKIN_DEPENDS
    rospy
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############
