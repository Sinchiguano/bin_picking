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
from tf.transformations import euler_from_quaternion, quaternion_from_euler

#Home position
home_left= [0.0, -130.0, 30.0, 0.01, 39.59, 0.0, 135.0]
home_right= [0.0, -130.0, 30.0, 0.0, 39.98, 0.0, -135.0]

#End Effector...
tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
                                           [0,-1,  0],
                                           [0, 0, 1]]),np.array([0, 0.0, 0.1142]))

def main():
    global home_left
    global tool_cesar_cal
    state_robot=False
    temp_flag=False
    previous_trans=[0.0 , 0.0, 0.0]



    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    listener = tf.TransformListener()
    rate = rospy.Rate(10)


    y = YuMiRobot(arm_type='remote')
    y.left.set_tool(tool_cesar_cal)
    y.right.set_tool(tool_cesar_cal)


    y.left.goto_state(YuMiState([-105.36, -38.59, 20.17, 100.76, 81.85, -84.42, 85.94]),wait_for_res=False)
    pose_state_left = y.left.get_pose(raw_res=False)
    tmp=pose_state_left.quaternion
    orientation_list = [tmp[1],tmp[2],tmp[3],tmp[0]]
    (roll_default, pitch_default, yaw_default)=tf.transformations.euler_from_quaternion(orientation_list)

    time.sleep(2)
    (trans,rot) = listener.lookupTransform('/world','/pose_object', rospy.Time(0))
    previous_trans=trans
    previous_rot=rot

    exit(0)
    while (not rospy.is_shutdown()):
        try:
            (trans,rot) = listener.lookupTransform('/world','/pose_object', rospy.Time(0))


            roll_, pitch_, yaw_=tf.transformations.euler_from_quaternion(rot)

            print('---New computation about quaternions---')
            q_orig = tf.transformations.quaternion_from_euler(roll_default,pitch_default,yaw_default)
            q_rot = quaternion_from_euler(0, 0, yaw_)
            q_new = quaternion_multiply(q_rot, q_orig)
            q_new/=np.linalg.norm(q_new)
            r_new = quaternion_matrix(q_new)
            print(trans, rot)
            time.sleep(3)

            #if not trans==None and not rot==None and not previous_trans==trans:
            if not trans==None and not rot==None and not previous_trans==trans and not previous_rot==rot:
                pose_state.translation=trans
                pose_state.rotation=r_new[:-1,:-1]
                temp_flag=y.left.is_pose_reachable(pose_state)
                print("flag:{}".format(temp_flag))
                move(y)
                previous_trans=trans
                print("It is feasible to reach the given pose {}".format(temp_flag))

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        if temp_flag:
            state_robot=y.left.goto_pose(pose_state, linear=True, relative=False, wait_for_res=True)
            y.left.open_gripper(no_wait=False, wait_for_res=True)
            pose_state.translation[2]=0.065
            state_robot=y.left.goto_pose(pose_state, linear=True, relative=False, wait_for_res=True)
            y.left.close_gripper(force=20,no_wait=False, wait_for_res=True)
            move(y)
            y.left.goto_state(YuMiState(home_industrial_obj),wait_for_res=False)
            y.left.open_gripper(no_wait=False, wait_for_res=True)
            temp_flag=False

        print('moving!!!')
        rate.sleep()

if __name__ == '__main__':
    main()
