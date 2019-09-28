#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT license.

"""

"""

import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *
from yumipy import YuMiRobot
from yumipy import YuMiState,YuMiArm_ROS
from autolab_core import RigidTransform
from yumipy import YuMiRobot

# starting the robot interface
y = YuMiRobot(arm_type='remote')



# #Wednesaday 14_August_2019 confdata 0,0,0,4
home_left=[0.0, -130.0, 30.0, 0.0, 39.53, 0.0, 135.0]
home_right=[0.0, -130.0, 30.0, 0.0, 39.95, -1.76, -134.66]




# getting the current pose of the right end effector
#pose = y.right.get_pose()





# print('pose:',pose)
# temp_flag=y.left.is_pose_reachable(pose)
# print('temp_flag: {}'.format(temp_flag))
# #move right arm forward by 5cm using goto_pose
# pose.translation[0] += 0.05
# #y.left.goto_pose(pose)
# y.left.goto_pose( pose, linear=True, relative=False, wait_for_res=True)


# # getting the current pose of the right end effector
# pose = y.right.get_pose()
# # move right arm forward by 5cm using goto_pose
# pose.translation[0] += 0.05
# y.right.goto_pose(pose)
