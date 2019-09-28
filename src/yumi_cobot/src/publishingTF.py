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

# moves_deg = np.array([[-44.59, -59.09, 29.83, -29.23, 47.63, 148.58, 81.83],
#                         [-47.4, -58.58, 24.45, -27.52, 49.21, 144.21, 80.84],
#                         [-51.58, -56.63, 24.8, -28.82, 43.34, 141.21, 77.44],
#                         [-55.93, -55.3, 16.08, -25.91, 46.72, 135.28, 77.39],
#                         [-60.64, -53.88, 7.1, -23.53, 50.45, 130.33, 78.15],
#                         [-79.9, -45.65, -18.24, -5.3, 66.5, 124.88, 82.09],
#                         [-73.35, -47.58, -8.65, -5.73, 62.1, 127.39, 79.21],
#                         [-64.9, -50.72, 4.48, -6.59, 56.25, 132.02, 76.96],
#                         [-59.22, -53.1, 13.71, -7.48, 52.31, 136.51, 76.83],
#                         [-62.59, -53.29, 9.35, -14.01, 60.72, 123.09, 81.34],
#                         [-67.79, -52.05, 1.85, -13.67, 63.55, 120.77, 83.11],
#                         [-93.39, -49.16, -34.48, -12.49, 78.84, 112.81, 96.09]])

# #with aruco marker and easy_eye calibration
# moves_deg = np.array([[-131.26, -61.49, -20.51, 17.19, -49.4, -67.65, 89.51],
#                         [-127.48, -60.41, -17.73, 15.57, -48.66, -66.58, 87.05],
#                         [-127.48, -60.41, -17.73, 15.57, -48.66, -66.58, 87.05],
#                         [-120.36, -58.31, -16.14, 14.46, -32.37, -69.91, 81.75],
#                         [-115.73, -57.12, -16.25, 11.54, -28.32, -68.18, 77.97],
#                         [-115.73, -57.12, -16.25, 11.54, -12.01, -110.22, 77.97],
#                         [-115.22, -57.53, -18.98, 17.06, -8.92, -115.58, 77.8],
#                         [-120.64, -56.13, -21.05, -1.03, -11.23, -96.51, 77.85],
#                         [-120.64, -56.13, -21.05, -1.03, -13.88, -70.68, 77.85],
#                         [-119.41, -55.22, -33.58, -75.54, -3.38, 4.82, 73.9],
#                         [-124.54, -64.61, -16.71, 9.17, -19.77, -71.65, 77.42]])

# # #with chessboard as a calibration target
# tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
#                                           [0, -1, 0],
#                                           [1, 0, 0]]), np.array([0, 0.035, 0.1892]))


# #with chessboard with a correction 
tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
                                          [0, -1, 0],
                                          [1, 0, 0]]), np.array([0, 0.035, 0.1892]))                                          

# #End Effector...
# tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
#                                            [0,-1,  0],
#                                            [0, 0, 1]]),np.array([0, 0.0, 0.1142]))
################################
# #with aruco as a calibration target
#End Effector...
# tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
#                                            [0,-1,  0],
#                                            [0, 0, 1]]),np.array([0.0, 0.0, 0.0]))

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
    t.child_frame_id = 'ee_link'
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
    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(10)

    # starting the robot interface
    y = YuMiRobot(arm_type='remote')


    y.left.set_tool(tool_cesar_cal)
    state = y.left.get_state(raw_res=False)
    print('State: {}'.format(state))


    while (True):

        pose = y.left.get_pose(raw_res=False)

        # print('translation {}'.format(pose.translation))
        # print('quaternion {}'.format(pose.quaternion))
        # print('rotation matrix \n{}'.format(pose.rotation))
        print('moving!!!')
        #move(y)
        pose_to_tf(br,pose.translation,pose.quaternion)


        # we should expect to go through the loop 10 times per second
        rate.sleep()
if __name__ == '__main__':
    main()
