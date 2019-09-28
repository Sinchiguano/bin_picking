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
from yumipy import YuMiRobot
from yumipy import YuMiState
from autolab_core import RigidTransform

# with aruco marker and easy_eye calibration eye in hand

moves_deg = np.array([[117.45, -56.45, -4.88, -119.77, 132.21, 138.14, -41.45],
                        [126.78, -54.86, -7.94, -119.18, 130.6, 144.74, -50.02],
                        [137.2, -53.75, -13.63, -119.76, 128.31, 149.09, -59.0],
                        [145.71, -53.4, -19.64, -120.79, 126.16, 150.95, -65.92],
                        [150.89, -53.42, -23.83, -121.59, 124.73, 151.48, -69.93],
                        [144.46, -56.13, -11.15, -117.47, 127.59, 159.16, -66.53],
                        [135.43, -56.59, -4.57, -116.02, 129.92, 157.27, -59.2],
                        [117.18, -59.2, 4.53, -114.48, 133.5, 148.31, -43.44],
                        [107.24, -61.67, 13.28, -108.29, 133.15, 150.3, -38.65]])

# tool_cesar_cal = RigidTransform(np.array([ [1, 0,  0],
#                                            [0,1,  0],
#                                            [0, 0, 1]]),np.array([0, 0, 0]))


#with chessboard with a correction 
tool_cesar_cal = RigidTransform(np.array([[ -0.9922444, -0.0046806, -0.1242145],
                                          [ -0.0882110,  0.7305723,  0.6771137],
                                          [ 0.0875783,  0.6828192, -0.7253191]]), np.array([0.0, 0.0, 0.0]))    


# tool_cesar_cal = RigidTransform(np.array([[0.0887406,  0.0865996, -0.9922830],
#                                         [-0.6828846,  0.7305213,  0.0026840],
#                                         [0.7251164,  0.6773766,  0.1239644 ] ]), np.array([0, 0.0, 0.0]))    

                                                                              

#Home position for the camera in the following setup: Eye in hand
home_camera=[96.01, -57.26, 70.18, 162.37, 114.49, 180.36, -97.91]


g_timestamp_last_move = 0
g_index_last_move = 0

def move(yumi_robot):
    import time
    global g_index_last_move
    global g_timestamp_last_move

    if (time.time() - g_timestamp_last_move) < 8:
        print('Remained timeL {}'.format((time.time() - g_timestamp_last_move)))
        return

    #Object that encapsulates a yumi arm joint angle configuration.
    moves = [YuMiState(p) for p in moves_deg]

    g_index_last_move = (g_index_last_move + 1) % len(moves)

    yumi_robot.right.goto_state(moves[g_index_last_move])
    g_timestamp_last_move = time.time()


def pose_to_tf(br,pose_translation,pose_quaternion):

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'base_link'
    t.child_frame_id = 'ee_link_r'
    t.transform.translation.x = pose_translation[0]
    t.transform.translation.y = pose_translation[1]
    t.transform.translation.z = pose_translation[2]
    t.transform.rotation.w = pose_quaternion[0]
    t.transform.rotation.x = pose_quaternion[1]
    t.transform.rotation.y = pose_quaternion[2]
    t.transform.rotation.z = pose_quaternion[3]
    br.sendTransform(t)

def main():
    global tool_cesar_cal
    rospy.init_node('base_link_tcp_link_r', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(10)

    # starting the robot interface
    y = YuMiRobot(arm_type='remote')


    #y.right.set_tool(tool_cesar_cal)
    state = y.right.get_state(raw_res=False)
    print('State: {}'.format(state))

    counter=0.0
    while (True):
        counter+=1
        pose = y.right.get_pose(raw_res=False)
        print('moving!!!',counter)
        print('translation {}'.format(pose.translation))
        # print('quaternion {}'.format(pose.quaternion))
        # print('rotation matrix \n{}'.format(pose.rotation))
        print('publishing right TF (robot base -->> ee_link_r)!!!')
        #move(y)
        pose_to_tf(br,pose.translation,pose.quaternion)


        # we should expect to go through the loop 10 times per second
        rate.sleep()
if __name__ == '__main__':
    main()
