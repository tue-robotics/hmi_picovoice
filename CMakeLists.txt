cmake_minimum_required(VERSION 3.0.2)
project(hmi_picovoice)

#add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  roslib
)

catkin_package(
  CATKIN_DEPENDS
    roscpp
    roslib
)

###########
## Build ##
###########

#set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${PROJECT_SOURCE_DIR}/cmake/)
#find_package(PORTAUDIO REQUIRED)
#find_package(LIBSNDFILE REQUIRED)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#add_library(${PROJECT_NAME}
#)

#target_link_libraries(${PROJECT_NAME}
#  ${catkin_LIBRARIES}
#)

add_executable(${PROJECT_NAME}_porcupine
  src/porcupine_node.cpp
)
target_link_libraries(${PROJECT_NAME}_porcupine ${catkin_LIBRARIES})

#add_executable(${PROJECT_NAME}_rhino
#  src/rhino_node.cpp
#)
target_link_libraries(${PROJECT_NAME}_porcupine ${catkin_LIBRARIES})

#############
## Install ##
#############
