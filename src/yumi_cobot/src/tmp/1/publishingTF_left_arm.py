#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

"""

"""
import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *

# from yumi_class import MoveGroup,all_close,measurements
from yumipy import YuMiRobot
from yumipy import YuMiState
from autolab_core import RigidTransform


# #with chessboard with a correction 
tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
                                          [0, -1, 0],
                                          [1, 0, 0]]), np.array([0, 0.035, 0.1892]))                                          

# #End Effector...
# tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
#                                            [0,-1,  0],
#                                            [0, 0, 1]]),np.array([0, 0.0, 0.1142]))

#Home position
home_left=[1.25, -129.84, 29.98, -0.76, 40.78, -5.78, 136.29]


g_timestamp_last_move = 0
g_index_last_move = 0

def move(yumi_robot):
    import time
    global g_index_last_move
    global g_timestamp_last_move

    if (time.time() - g_timestamp_last_move) < 4:
        print('Remained timeL {}'.format((time.time() - g_timestamp_last_move)))
        return

    #Object that encapsulates a yumi arm joint angle configuration.
    moves = [YuMiState(p) for p in moves_deg]

    g_index_last_move = (g_index_last_move + 1) % len(moves)

    yumi_robot.left.goto_state(moves[g_index_last_move],wait_for_res=False)
    g_timestamp_last_move = time.time()


def pose_to_tf(br,pose_translation,pose_quaternion):

    """input in m and rad"""
    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'base_link'
    t.transform.translation.x = 0
    t.transform.translation.y = 0
    t.transform.translation.z = 0
    t.transform.rotation.w = 1
    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    br.sendTransform(t)

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'base_link'
    t.child_frame_id = 'ee_link_l'
    t.transform.translation.x = pose_translation[0]
    t.transform.translation.y = pose_translation[1]
    t.transform.translation.z = pose_translation[2]
    t.transform.rotation.w = pose_quaternion[0]
    t.transform.rotation.x = pose_quaternion[1]
    t.transform.rotation.y = pose_quaternion[2]
    t.transform.rotation.z = pose_quaternion[3]
    br.sendTransform(t)

def main():
    global home_left
    global tool_cesar_cal
    #rospy.init_node('tcp_tf', anonymous=True)
    rospy.init_node('base_link_tcp_link_l', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(10)

    # starting the robot interface
    y = YuMiRobot(arm_type='remote')


    y.left.set_tool(tool_cesar_cal)
    state = y.left.get_state(raw_res=False)
    print('State: {}'.format(state))

    counter=0.0
    while (True):
        counter+=1
        pose = y.left.get_pose(raw_res=False)
        print('moving!!!',counter)
        print('translation {}'.format(pose.translation))
        # print('quaternion {}'.format(pose.quaternion))
        # print('rotation matrix \n{}'.format(pose.rotation))
        print('publishing left TF (robot base -->> calibration_target)!!!')
        #move(y)
        pose_to_tf(br,pose.translation,pose.quaternion)


        # we should expect to go through the loop 10 times per second
        rate.sleep()
if __name__ == '__main__':
    main()
