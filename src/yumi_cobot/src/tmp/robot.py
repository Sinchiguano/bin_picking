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

# #Wednesaday 14_August_2019
home_left=[0.0, -130.0, 30.0, 0.0, 39.53, 0.0, 135.0]
home_right=[0.0, -130.0, 30.0, 0.0, 39.95, -1.76, -134.66]
# confdata [-1,-1,0,3]

qtn_temp= [-0.03201502 , 0.99946886, -0.00600282, -0.00100047]

#End Effector...
tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],
                                           [0,-1,  0],
                                           [0, 0, 1]]),np.array([0, 0.0, 0.1142]))

g_timestamp_last_move = 0
g_index_last_move = 0

#home demo position to be close to the target
moves_deg = np.array([[-91.98, -44.15, 21.6, 111.06, 71.47, -69.94, 87.21]])


#home_industrial_obj=[-104.07, -71.35, -36.44, 132.22, 84.2, -87.31, 42.0]

#Tuesday 03_September_2019
home_industrial_obj=[-103.96, -79.35, -14.57, 136.16, 91.4, -102.65, 45.55]



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

def main():
    global home_left
    global tool_cesar_cal


    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    listener = tf.TransformListener()
    
    
    y = YuMiRobot(arm_type='remote')
    y.left.set_tool(tool_cesar_cal)
    y.right.set_tool(tool_cesar_cal)


    rate = rospy.Rate(10)
    move(y)

    y.left.open_gripper(no_wait=False, wait_for_res=True)
    pose_state = y.left.get_pose(raw_res=False)
    y.left.close_gripper(no_wait=False, wait_for_res=True)

    state_robot=False
    temp_flag=False
    previous_trans=[0.0 , 0.0, 0.0]

    tmp=pose_state.quaternion
    orientation_list = [tmp[1],tmp[2],tmp[3],tmp[0]]
    (roll_default, pitch_default, yaw_default)=tf.transformations.euler_from_quaternion(orientation_list)

    #exit(0)
    while (not rospy.is_shutdown()):

        
        try:
            (trans,rot) = listener.lookupTransform('/world','/pose_object', rospy.Time(0))
            from tf.transformations import euler_from_quaternion, quaternion_from_euler

            roll_, pitch_, yaw_=tf.transformations.euler_from_quaternion(rot)

            print('---New computation about quaternions---')
            q_orig = tf.transformations.quaternion_from_euler(roll_default,pitch_default,yaw_default)
            q_rot = quaternion_from_euler(0, 0, yaw_)
            q_new = quaternion_multiply(q_rot, q_orig)
            q_new/=np.linalg.norm(q_new)
            r_new = quaternion_matrix(q_new)
            print(trans, rot)
            time.sleep(3)

            if not trans==None and not rot==None and not previous_trans==trans:
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
