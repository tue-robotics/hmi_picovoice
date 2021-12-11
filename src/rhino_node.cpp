#include <ros/ros.h>

int main(int argc, char** argv)
{
  ros::init(argc, argv, "hmi_rhino");

  ros::NodeHandle local_nh("~");

  try
  {
    ros::spin();
  }
  catch (const std::exception& e)
  {
    ROS_FATAL("HmiRhinoNode exception: %s", e.what());
    return 1;
  }
  return 0;
}
