#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.
#!/usr/bin/env python
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *



def data_to_transform(r_matrix,t_position):
    r_matrix[0,3] =t_position[0]
    r_matrix[1,3] =t_position[1]
    r_matrix[2,3] =t_position[2]

    return r_matrix



if __name__ == '__main__':

    rospy.init_node('cam_tf_listener_r')

    listener = tf.TransformListener()

    rate = rospy.Rate(10.0)
    counter=1
    translation_mean=list()
    rotation_mean=list()
    print('=======')
    while (True):
        #print('')
        try:
            #(trans1,rot1) = listener.lookupTransform('/world','/camera_link', rospy.Time(0))
            (trans1,rot1) = listener.lookupTransform('ee_link_r','/camera_link', rospy.Time(0))
            if not trans1==None and not rot1==None:
                translation_mean.append(trans1)
                rotation_mean.append(rot1)
                counter+=1
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        #Rq = quaternion_matrix(rot1)
        #tf_robot_cam=data_to_transform(rot1,trans1)
        print('trans:\n{}'.format(trans1))
        print('rot:\n{}'.format(rot1))
        print('-----------------------------------')

        rate.sleep()
