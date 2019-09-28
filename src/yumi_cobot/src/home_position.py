#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""
Sinchiguano
"""
import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *
from yumipy import YuMiRobot
from yumipy import YuMiState,YuMiArm_ROS
from autolab_core import RigidTransform

#Home position
home_left= [0.0, -130.0, 30.0, 0.01, 39.59, 0.0, 135.0]
home_right= [0.0, -130.0, 30.0, 0.0, 39.98, 0.0, -135.0]
#camera# # confdata [0,0,0,4]


#End Effector...
tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
                                           [0,-1,  0],
                                           [0, 0, 1]]),np.array([0, 0.0, 0.1142]))


def move(yumi_robot):
    import time
    global g_index_last_move
    global g_timestamp_last_move

    #Object that encapsulates a yumi arm joint angle configuration.
    moves = [YuMiState(p) for p in moves_deg]
    g_index_last_move = (g_index_last_move + 1) % len(moves)
    yumi_robot.left.goto_state(moves[g_index_last_move],wait_for_res=False)
    #yumi_robot.right.goto_state(moves[g_index_last_move],wait_for_res=False)
    g_timestamp_last_move = time.time()

def pose_to_tf(br,pose_translation,pose_quaternion):

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'yumi_tcp'
    t.transform.translation.x = pose_translation[0]
    t.transform.translation.y = pose_translation[1]
    t.transform.translation.z = pose_translation[2]
    t.transform.rotation.w = pose_quaternion[0]
    t.transform.rotation.x = pose_quaternion[1]
    t.transform.rotation.y = pose_quaternion[2]
    t.transform.rotation.z = pose_quaternion[3]
    br.sendTransform(t)

#def main():
# global tool_cesar_cal
# global home_left
# global home_right

rospy.init_node('home_movement', anonymous=True)
y = YuMiRobot(arm_type='remote')
y.left.set_tool(tool_cesar_cal)
y.right.set_tool(tool_cesar_cal)

y.left.goto_state(YuMiState(home_left),wait_for_res=False)
y.right.goto_state(YuMiState(home_right),wait_for_res=False)
state_left = y.left.get_state(raw_res=False)
state_right = y.right.get_state(raw_res=False)

print('state_left: {}'.format(state_left))
print('state_right: {}'.format(state_right))


y.left.open_gripper(no_wait=False, wait_for_res=True)
y.right.open_gripper(no_wait=False, wait_for_res=True)
y.left.close_gripper(no_wait=False, wait_for_res=True)
y.right.close_gripper(no_wait=False, wait_for_res=True)

#    rate = rospy.Rate(10)

#     while (not rospy.is_shutdown()):

#         try:
#             print('moving!!!')
#             #move(y)
#         except:
#             print('Linux function was not executed')
#             continue


#         rate.sleep()

# if __name__ == '__main__':
#     main()
