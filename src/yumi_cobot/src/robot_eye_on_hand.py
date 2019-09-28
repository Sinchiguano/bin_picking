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
import rospy
from std_msgs.msg import String,Bool
import time

########################################################
#Home position-->> initialize the robot wherever it is!!!
home_left= [0.0, -130.0, 30.0, 0.01, 39.59, 0.0, 135.0]
home_right= [0.0, -130.0, 30.0, 0.0, 39.98, 0.0, -135.0]
########################################################
g_timestamp_last_move = 0
g_index_last_move = 0

#End Effector...
tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],[0,-1,  0],[0, 0, 1]]),np.array([0, 0.0, 0.1142]))

#home demo position to be close to the target
moves_deg = np.array([[-91.98, -44.15, 21.6, 111.06, 71.47, -69.94, 87.21]])

#Tuesday 03_September_2019
home_industrial_obj=[-103.96, -79.35, -14.57, 136.16, 91.4, -102.65, 45.55]

tmpID=None


def move(yumi_robot):

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

def callback_templateID(data):
    global tmpID
    tmpID=data.data
    #rospy.loginfo(rospy.get_caller_id() + "templateID:  %s", data.data)

def retrieve_templateID():
    global tmpID
    return tmpID

def callback_signalControl(data):
    pass
    #rospy.loginfo(rospy.get_caller_id() + "signalControl:  %s", data.data)

def move_leftARM(y):
    #pose correction before interchange the object
    y.left.goto_state(YuMiState([-42.63, -47.53, 51.2, 70.88, 89.62, -66.38, 14.45]),wait_for_res=False)

    #corretion of the orientation of the right arm
    y.right.goto_state(YuMiState([51.28, -57.55, 41.39, 8.12, 47.69, 54.93, -61.18]),wait_for_res=False)
    #get close to the exchange point
    y.right.goto_state(YuMiState( [67.57, -49.31, 42.8, 14.56, 31.15, 50.84, -68.12]),wait_for_res=False)
    y.right.close_gripper(no_wait=False, wait_for_res=True)

    #free the gripper of the left arm and move slight in the north direction
    y.left.open_gripper(no_wait=False, wait_for_res=True)
    y.left.goto_state(YuMiState([-36.57, -47.51, 46.42, 59.54, 95.69, -63.41, -1.04]),wait_for_res=False)

def move_rightARM(y):
    #pose correction before interchange the object
    y.left.goto_state(YuMiState([-52.71, -47.84, 58.19, 86.44, 83.62, -79.57, 31.13]),wait_for_res=False)

    #corretion of the orientation of the right arm
    y.right.goto_state(YuMiState([43.62, -56.21, 34.67, 17.13, 60.46, 33.92, -73.57]),wait_for_res=False)
    #get close to the exchange point
    y.right.goto_state(YuMiState([65.36, -48.48, 41.59, 31.42, 36.39, 22.68, -81.01]),wait_for_res=False)
    y.right.close_gripper(no_wait=False, wait_for_res=True)

    #free the gripper of the left arm and move slight in the north direction
    y.left.open_gripper(no_wait=False, wait_for_res=True)
    y.left.goto_state(YuMiState([-43.74, -47.36, 55.23, 68.68, 88.53, -75.86, 8.33]),wait_for_res=False)

def move_home(y):
    global home_left,home_right
    #Home position for both arms
    y.right.close_gripper(no_wait=False, wait_for_res=True)
    y.left.close_gripper(force=20,no_wait=False, wait_for_res=True)
    y.left.goto_state(YuMiState(home_left))
    y.right.goto_state(YuMiState(home_right))
def main():
    global tool_cesar_cal
    counter=0.0
    state_robot=False
    control_flag=False
    previous_trans=[0.0 , 0.0, 0.0]


    rospy.init_node('tcp_tf', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    listener = tf.TransformListener()
    rospy.Subscriber('/templateID', String, callback_templateID)
    rospy.Subscriber('/signalControl', Bool, callback_signalControl)


    y = YuMiRobot(arm_type='remote')
    y.left.set_tool(tool_cesar_cal)
    y.right.set_tool(tool_cesar_cal)

    #send to home position both arm
    move_home(y)

    # get state of the bridge pose
    move(y)
    pose_state = y.left.get_pose(raw_res=False)
    orientation_list = [pose_state.quaternion[1],pose_state.quaternion[2],pose_state.quaternion[3],pose_state.quaternion[0]]
    (roll_default, pitch_default, yaw_default)=tf.transformations.euler_from_quaternion(orientation_list)


    #Home position for both arms
    move_home(y)

    rate = rospy.Rate(10)
    templateID=None
    while (not rospy.is_shutdown()):
        counter+=1
        try:
            (trans,rot) = listener.lookupTransform('/world','/pose_object', rospy.Time(0))
            roll_, pitch_, yaw_=tf.transformations.euler_from_quaternion(rot)

            print('---New computation about quaternions---')
            q_orig = tf.transformations.quaternion_from_euler(roll_default,pitch_default,yaw_default)
            q_rot = quaternion_from_euler(0, 0, yaw_)
            q_new = quaternion_multiply(q_rot, q_orig)
            q_new/=np.linalg.norm(q_new)
            r_new = quaternion_matrix(q_new)
            templateID= retrieve_templateID()
            # print('trans: {} '.format(trans))
            # print('rot: {}'.format(rot))
            # print('counter: {}'.format(counter))

            if not trans==None and not rot==None and not previous_trans==trans:
                pose_state.translation=trans
                pose_state.rotation=r_new[:-1,:-1]
                control_flag=y.left.is_pose_reachable(pose_state)
                print("flag:{}".format(control_flag))
                move(y)# got to a close pose to the target
                previous_trans=trans


                print("It is feasible to reach the given pose {}".format(control_flag))

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        if control_flag:
            #grasping task
            state_robot=y.left.goto_pose(pose_state, linear=True, relative=False, wait_for_res=True)
            y.left.open_gripper(no_wait=False, wait_for_res=True)
            pose_state.translation[2]=0.04
            state_robot=y.left.goto_pose(pose_state, linear=True, relative=False, wait_for_res=True)
            y.left.close_gripper(force=20,no_wait=False, wait_for_res=True)
            move(y)#return to a close pose to the target


            #default bridge in order to pass the object to the  neighbour
            y.left.goto_state(YuMiState([-61.29, -71.92, 41.76, 24.64, 52.57, -98.59, 42.29]),wait_for_res=False)
            y.right.open_gripper(no_wait=False, wait_for_res=True)
            y.right.goto_state(YuMiState([33.48, -62.78, 42.07, 17.64, 59.23, 51.12, -51.25]),wait_for_res=False)

            # correction in order to exchange the object from one arm to another
            if templateID=='1':
                move_leftARM(y)
            elif templateID=='2':
                move_rightARM(y)

            # #home industrial object for the right side---->>>>
            # y.right.goto_state(YuMiState([46.31, -65.96, 38.6, 9.26, -24.89, -0.75, -100.17]),wait_for_res=False)
            # y.right.open_gripper(no_wait=False, wait_for_res=True)


            #home industrial object for the right side---->>>>
            y.right.goto_state(YuMiState([65.2, -108.57, 6.18, 27.06, 30.48, -76.36, -67.19]),wait_for_res=False)
            y.right.open_gripper(no_wait=False, wait_for_res=True)# drop the object
            y.right.goto_state(YuMiState([54.64, -113.19, 35.4, -0.49, 7.86, -40.14, -52.73]),wait_for_res=False)# in order not to collide


            move_home(y)

            #pose of camera from up to down
            y.right.goto_state(YuMiState([60.25, -16.19, 58.96, 99.07, -72.78, 17.36, -23.21]),wait_for_res=False)
            control_flag=False
        print('moving!!!')
        print('Previous templateID: {}'.format(templateID))
        rate.sleep()

if __name__ == '__main__':
    main()
