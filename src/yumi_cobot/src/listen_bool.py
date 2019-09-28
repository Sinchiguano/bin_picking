#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT license.

"""

"""
import rospy
from std_msgs.msg import String,Bool

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:  %s", data.data)


def callback_bool(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:  %s", data.data)
    # print('data: ',data)
    # print('type: ',type(data))
    #print('data.data: ',data.data)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/chatter", String, callback)
    rospy.Subscriber("/control_signa", Bool, callback_bool)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()