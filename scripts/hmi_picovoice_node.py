#!/usr/bin/env python3
#
# Copyright (c) 2022, TU/e Robotics
# All rights reserved.
#
# Author: Rein Appeldoorn

import rospy

from hmi_picovoice.server import Server

if __name__ == '__main__':
    rospy.init_node("hmi_picovoice")

    context_url = rospy.get_param("~context_url", "")
    require_endpoint = rospy.get_param("~require_endpoint", False)
    rate = rospy.get_param("~rate", 10.)

    if not context_url:
        rospy.logfatal("Missing required parameter '~context_url'")
        exit(1)

    Server(rospy.get_name(), context_url, require_endpoint, rate)
    rospy.spin()
