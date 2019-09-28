#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT license.

"""
Inspired by MoveIt tutorial
"""
#from ur10_class_01 import *
# import tf
# import tf2_ros
# from tf.transformations import *

import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *
from yumipy import YuMiRobot
from yumipy import YuMiState,YuMiArm_ROS
from autolab_core import RigidTransform
import numpy as np
import csv
import time


name_file='joints_yumi.csv'


def do_csv_file(state_left):
    global name_file
    with open(name_file, 'a') as csvfile:# a means append
        filewriter = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(state_left+[''])

def main():
    #rospy.init_node('joint_nodes', anonymous=True)
    r=rospy.Rate(10)
    y = YuMiRobot(arm_type='remote')
    # #with chessboard as a calibration target
    tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
                                              [0, -1, 0],
                                              [1, 0, 0]]), np.array([0, 0.035, 0.1892]))
    # state_left = y.left.get_state(raw_res=False)
    # state_right = y.right.get_state(raw_res=False)
    # print('state_left: {}'.format(state_left))
    # print('state_right: here {}'.format(state_right))

    y.left.set_tool(tool_cesar_cal)

    counter=0
    while(not rospy.is_shutdown()):
        frame=camObj.get_image()
        if frame is None:
            print('no image!!!')
            continue
        try:
            state_left = y.left.get_state(raw_res=False)
            print('state_left: {}'.format(state_left))
            print('counter: {}'.format(counter))
        except rospy.ROSInterruptException:
            return
        except KeyboardInterrupt:
            return
        command=cv2.waitKey(1) & 0xFF
        if command == ord('t'):
            counter+=1
            print('The current pose was appended:\n{}'.format(state_left))
            do_csv_file([state_left])
            time.sleep(0.5)
            print ("============ Python movement complete!")
        r.sleep()
        cv2.imshow('frame',frame)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #object_ur10 = UniversalRobot()
    camObj=camera()
    main()
