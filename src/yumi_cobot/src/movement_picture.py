#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the MIT License license.

import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *
from thesis_library import camera

from yumipy import YuMiRobot
from yumipy import YuMiState
from autolab_core import RigidTransform
import numpy as np
import time

moves_deg = np.array([[35.29, -53.92, 25.63, 183.12, -52.68, -171.06, -12.45],
                    [29.53, -48.13, 15.83, 184.41, -56.09, -157.6, 4.35],
                    [30.69, -37.84, -0.55, 184.03, -62.42, -159.94, 0.77],
                    [45.1, -45.73, -9.83, 181.02, -78.23, -178.92, -27.87]])


# #with chessboard with a correction
tool_cesar_cal = RigidTransform(np.array([[0, 0, 1],
                                          [0, -1, 0],
                                          [1, 0, 0]]), np.array([0, 0.035, 0.1892]))


g_timestamp_last_move = 0
g_index_last_move = 0

def move(yumi_robot):

    global g_index_last_move
    global g_timestamp_last_move
    take_picture=False
    if (time.time() - g_timestamp_last_move) < 4:
        take_picture=False
        print('Remained timeL {}'.format((time.time() - g_timestamp_last_move)))
        return
    take_picture=True
    moves = [YuMiState(p) for p in moves_deg]
    g_index_last_move = (g_index_last_move + 1) % len(moves)
    yumi_robot.right.goto_state(moves[g_index_last_move],wait_for_res=False)
    g_timestamp_last_move = time.time()
    return take_picture
def main():
    global tool_cesar_cal
    #rospy.init_node('make_picture_node', anonymous=True)
    br = tf2_ros.TransformBroadcaster()
    rate = rospy.Rate(10)

    y = YuMiRobot(arm_type='remote')
    request=bool(False)
    counter=int(0)
    while not rospy.is_shutdown():
        frame=camOBJ.get_image()
        if frame is None:
            print('no image!!!')
            continue

        if cv2.waitKey(1) & 0xFF == ord('q'):
            #cv2.imwrite('folder_pictures/temp3.jpg', frame)
            break
        try:
            print('moving!!!')
            request=move(y)
            if request:
                counter+=1
                cv2.imwrite('folder_pictures/frame'+str(counter)+'.jpg', frame)
        except Exception as ex:
            print('')
            continue
        # we should expect to go through the loop 10 times per second
        rate.sleep()
        print('\ncounter:',counter,'\n')
        cv2.imshow('Visulization',frame)
    # When everything done, release the capture
    cv2.destroyAllWindows()
if __name__ == '__main__':
    camOBJ=camera()
    main()
