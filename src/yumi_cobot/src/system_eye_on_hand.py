#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Cesar Sinchiguano <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

import sys
sys.path.insert(0, '/home/casch/catkin_ws/src/yumi_cobot/src/project')
from thesis_library import *
from thesis_class import *
from open3d import uniform_down_sample,registration_icp,TransformationEstimationPointToPlane,TransformationEstimationPointToPoint
import pcl
import csv
import time
from tf.transformations import euler_from_quaternion, quaternion_from_euler
import sys
from yumipy import YuMiRobot
from yumipy import YuMiState,YuMiArm_ROS
from autolab_core import RigidTransform
from std_msgs.msg import Bool


model_path='pipeline_model/template_real/'
scene_path='pipeline_pcd/'

tmp='output_pipeline/'
name_file=tmp+'transform_data.csv'
#Home position-->> initialize the robot wherever it is!!!
home_left= [0.0, -130.0, 30.0, 0.01, 39.59, 0.0, 135.0]
home_right= [0.0, -130.0, 30.0, 0.0, 39.98, 0.0, -135.0]
tool_cesar_cal = RigidTransform(np.array([ [-1, 0,  0],[0,-1,  0],[0, 0, 1]]),np.array([0, 0.0, 0.1142]))

counter1=0
counter2=0
counter3=0
flag=False
threshold = 0.02


def do_pointcloud(frame,pc,counter):
    global scene_path
    pcd=do_vector3d(pc)
    tmp=scene_path+'pointcloud'+str(counter)
    cv2.imwrite(tmp+'.jpg', frame)

    write_point_cloud(tmp+'base_link'+'.pcd', pcd)
    write_point_cloud(tmp+'base_link'+'.ply', pcd)

    return pcl.load(tmp+'base_link'+'.pcd')

def do_vector3d(pc):
    temp=np.asarray(pc)
    pc=np.nan_to_num(pc)
    pcd = PointCloud()
    start_timer=time.time()
    pcd.points = Vector3dVector(pc)
    # # eye_on_hand calibration 1
    # pcd.transform([[ 0.04382427, -0.36730281,  0.92906839,  0.1473705 ],
    #                 [-0.99791508, -0.06019866,  0.02327252,  0.02916129],
    #                 [ 0.04738061, -0.92815126, -0.36917517,  0.22427066],
    #                 [ 0.,          0.,          0.,          1.        ]])

    # eye_on_hand calibration up
    pcd.transform([[ 0.05048428, -0.98125195,  0.18599984,  0.36134248],
                    [-0.99868515, -0.04793841,  0.01816262,  0.06204829],
                    [-0.00890557, -0.1866722,  -0.98238189,  0.42836043],
                    [ 0.,          0.,          0.,          1.        ]])

    return pcd

def do_dataset(source,target):
    '''Preprocessing step'''
    #print("Downsample the point cloud and get features with FPFH")
    source_down, source_fpfh = do_preprocessing_pcd(source, 0.003)#in mm
    tmp_source=np.asarray(source_down.points)

    #print("Downsample the point cloud and get features with FPFH")
    target_down, target_fpfh = do_preprocessing_pcd(target, 0.003)#good tunning
    tmp_target=np.asarray(target_down.points)

    return source, target, source_down, target_down, source_fpfh, target_fpfh

def do_preprocessing_pcd(pcd, voxel_size):
    '''Downsample the point cloud'''
    pcd_down = voxel_down_sample(pcd, voxel_size)

    '''Estimate normals'''
    radius_normal = voxel_size * 6
    estimate_normals(pcd_down, KDTreeSearchParamHybrid(radius = radius_normal, max_nn = 30))

    '''Fast Point Feature Histograms'''
    radius_feature = voxel_size * 6
    pcd_fpfh = compute_fpfh_feature(pcd_down,KDTreeSearchParamHybrid(radius = radius_feature, max_nn = 100))

    return pcd_down, pcd_fpfh

def do_ransac_registration(source_down, target_down, source_fpfh, target_fpfh):

    '''RANSAC registration is applied on downsampled point clouds.'''
    threshold = 0.003
    result = registration_ransac_based_on_feature_matching(source_down, target_down, source_fpfh, target_fpfh,threshold,
            TransformationEstimationPointToPoint(False), 4,
            [CorrespondenceCheckerBasedOnEdgeLength(0.9),CorrespondenceCheckerBasedOnDistance(threshold)],
            RANSACConvergenceCriteria(400000, 1000))
    return result

def do_icp_registration(source, target, transformation):


    '''Point-to-plane ICP registration is applied on original points'''
    estimate_normals(source, KDTreeSearchParamHybrid(radius = 0.005, max_nn = 20))
    estimate_normals(target, KDTreeSearchParamHybrid(radius = 0.005, max_nn = 20))
    threshold = 0.005
    result = registration_icp(source, target, threshold,transformation,TransformationEstimationPointToPlane())
    return result

def do_drawing_registration(source, target, transformation):

    source_tmp= copy.deepcopy(source)
    target_tmp = copy.deepcopy(target)
    source_tmp.paint_uniform_color([1, 0.706, 0])
    target_tmp.paint_uniform_color([0, 0.651, 0.929])

    source_tmp.transform(transformation)
    draw_geometries([source_tmp, target_tmp])

def do_passthrough_filter(point_cloud, name_axis = 'z', min_axis = 0.6, max_axis = 1.1):
    pass_filter = point_cloud.make_passthrough_filter()
    pass_filter.set_filter_field_name(name_axis)
    pass_filter.set_filter_limits(min_axis, max_axis)
    return pass_filter.filter()

def do_ransac_plane_segmentation(point_cloud, max_distance = 0.01):

    segmenter = point_cloud.make_segmenter()
    segmenter.set_model_type(pcl.SACMODEL_PLANE)
    segmenter.set_method_type(pcl.SAC_RANSAC)
    segmenter.set_distance_threshold(max_distance)
    inlier_indices, coefficients = segmenter.segment()

    inliers = point_cloud.extract(inlier_indices, negative = False)
    outliers = point_cloud.extract(inlier_indices, negative = True)
    return inliers, outliers

def do_csv_file(tran_rot,counter1,computation_time,max_fitness,min_rmse,aux_rmse,aux_fitness):
    global name_file
    aux_angles=do_rotation_matrix_to_euler_angles(tran_rot[:-1,:-1])
    tmp_list=list(tran_rot[:-1,3])
    q = tf.transformations.quaternion_from_matrix(tran_rot)
    (roll, pitch, yaw) = euler_from_quaternion(q)
    from pyquaternion import Quaternion
    a= Quaternion(matrix=tran_rot)
    print(a)
    print("{} + {}i + {}j + {}k".format(a[0], a[1], a[2], a[3]))
    quat=[a[0], a[1], a[2], a[3]]
    with open(name_file, 'a') as csvfile:# a means append
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #filewriter.writerow(computation_time+aux_rmse+min_rmse+aux_fitness+max_fitness)
        filewriter.writerow(computation_time)

# Calculates rotation matrix to euler angles
def do_rotation_matrix_to_euler_angles(R) :
    sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])

    singular = sy < 1e-6

    if  not singular :
        x = math.atan2(R[2,1] , R[2,2])
        y = math.atan2(-R[2,0], sy)
        z = math.atan2(R[1,0], R[0,0])
    else :
        x = math.atan2(-R[1,2], R[1,1])
        y = math.atan2(-R[2,0], sy)
        z = 0
    return [x* 180 / math.pi, y* 180 / math.pi, z* 180 / math.pi]

def do_publishing_pose(br,transformation):
    pose_translation=list(transformation[:-1,3])
    pose_quaternion = tf.transformations.quaternion_from_matrix(transformation)


    """input in m and rad"""
    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = 'world'
    t.child_frame_id = 'pose_object'
    t.transform.translation.x = pose_translation[0]+0.00
    t.transform.translation.y = pose_translation[1]-0.02
    t.transform.translation.z = pose_translation[2]+0.10
    t.transform.rotation.w = pose_quaternion[3]
    t.transform.rotation.x = pose_quaternion[0]
    t.transform.rotation.y = pose_quaternion[1]
    t.transform.rotation.z = pose_quaternion[2]
    br.sendTransform(t)
    # print('pose_translation {}'.format(pose_translation))
    # print('pose_quaternion {}'.format(pose_quaternion))

    print('pose_translation \n{}'.format(t.transform.translation))
    print('pose_quaternion \n{}'.format(t.transform.rotation))



def main():
    global counter1,counter2,counter3,flag,threshold
    global home_left,home_right,tool_cesar_cal
    templateID=str(0)
    contronlSIGNAL=Bool(False)

    br = tf2_ros.TransformBroadcaster()
    # Publishing bool variable and id of the template to execute the movement of the robot
    pub_template = rospy.Publisher('/templateID', String, queue_size=10)
    pub_control = rospy.Publisher('/signalControl', Bool, queue_size=10)

    y = YuMiRobot(arm_type='remote')

    y.left.set_tool(tool_cesar_cal)
    y.right.set_tool(tool_cesar_cal)
    y.right.close_gripper(no_wait=False, wait_for_res=True)
    y.left.close_gripper(no_wait=False, wait_for_res=True)

    #send to home position both arm
    y.left.goto_state(YuMiState(home_left),wait_for_res=False)
    y.right.goto_state(YuMiState(home_right),wait_for_res=False)




    # Send the right arm into the camera-home position
    # default setup
    # y.right.goto_state(YuMiState([67.66, -129.36, 35.79, -98.77, -63.57, -3.24, -139.03]),wait_for_res=False)
    # top-to-down setup
    y.right.goto_state(YuMiState([60.25, -16.19, 58.96, 99.07, -72.78, 17.36, -23.21]),wait_for_res=False)

    pose_state_left = y.left.get_pose(raw_res=False)
    # print('pose_state_left.quaternion: {}'.format(pose_state_left.quaternion))
    # print('pose_state_left.translation: {}'.format(pose_state_left.translation))
    tmp=pose_state_left.quaternion
    aux=pose_state_left.translation
    #orientation_list = [tmp[1],tmp[2],tmp[3],tmp[0]]
    transformation_= quaternion_matrix([tmp[1],tmp[2],tmp[3],tmp[0]])
    transformation_[0,3]=aux[0]
    transformation_[1,3]=aux[1]
    transformation_[2,3]=aux[2]
    transformation_right=copy.deepcopy(transformation_)
    transformation_awkward= quaternion_matrix([0, 0, 0, 1])
    transformation_awkward[0,3]=0.0
    transformation_awkward[1,3]=0.0
    transformation_awkward[2,3]=0.0


    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        counter1+=1

        # Capture 2D-data
        frame=camObj.get_image()

        # Capture 3D-data
        pc=camObj.get_point_cloud()

        if pc is None:
            print('no PointCloud2!!!')
            continue
        elif frame is None:
            print('no Frame!!!')
            continue

        #Enter to process a depth image and generate the 6D pose estimation
        command=cv2.waitKey(1) & 0xFF
        print('Ready to take scene data!!!')
        print('press t to catch an example (PointCoud data)...')
        if command == ord('t'):
            #y.right.goto_state(YuMiState([58.66, -15.47, 34.38, 93.23, -62.16, -3.32, -34.6]),wait_for_res=False)
            try:
                """Get a scene cloud in the world coordinate system"""
                pcd=do_pointcloud(frame,pc,counter2)
                cloud=copy.deepcopy(pcd)
            except Exception as ex:
                print('Please, place the object into the workspace!!!')
                print(ex)
                continue
            counter2+=1

            # Threshold
            filter = do_passthrough_filter(point_cloud = cloud,name_axis = 'x', min_axis = 0.33, max_axis = 0.65)
            filter = do_passthrough_filter(point_cloud = filter,name_axis = 'y', min_axis = -0.25, max_axis = 0.25)
            pcl.save(filter,scene_path +'filter_objects_'+str(counter2)+'.pcd' )
            print('filter done!')

            # Segmentation process in order to separate the object from table
            table, objects = do_ransac_plane_segmentation(filter, max_distance = 0.01)
            pcl.save(objects,scene_path +'objects_'+str(counter2)+'.pcd' )
            print('segmentation done!')

            pcd = read_point_cloud(scene_path+'objects_'+str(counter2)+'.pcd')
            write_point_cloud(scene_path +'objects_'+str(counter2)+'.ply', pcd)
            print('data convertion done!')

            #The target cloud is a scene image, it is already mapped into the world coordinate system (T: World -> Camera)
            target=read_point_cloud(scene_path+'objects_'+str(counter2)+'.pcd')
            print('upload target done!')

            #Template to match with the image taken from scene
            template_ = [read_point_cloud(rgbd) for rgbd in glob.glob(model_path+'*'+'.ply')]
            #template_.sort()
            print('upload templates done!')

            max_fitness=0.5
            max_fitness_index=0
            rmse=0.0
            rmse_=list()
            fitness_=list()

            for i, source in enumerate(template_):

                #DOWNSAMPLE AND COMPUTE FAST POINT FEATURE HISTOGRAM-->PREPROCESSING STEP: DATA MANIPULATION OF THE POINT CLOUD
                source, target, source_down, target_down, source_fpfh, target_fpfh=do_dataset(source,target)
                #draw_geometries([source,target])
                #RANSAC REGISTRATION-->>global registration
                #-------------------
                ransac_output_tmp=do_ransac_registration(source_down, target_down, source_fpfh, target_fpfh )
                print('ransac done!')
                #do_drawing_registration(source_down, target_down, ransac_output_tmp.transformation)
                #ICP REGISTRATION -->>local registration, point to plane approach
                #-------------------
                icp_output_tmp = do_icp_registration(source_down, target_down,ransac_output_tmp.transformation)
                print('icp done!')
                #do_drawing_registration(source_down, target_down, icp_output_tmp.transformation)
                rmse_.append(icp_output_tmp.inlier_rmse)
                fitness_.append(icp_output_tmp.fitness)
                if icp_output_tmp.fitness>max_fitness:
                    max_fitness=icp_output_tmp.fitness
                    min_rmse=icp_output_tmp.inlier_rmse
                    source_=template_[i]
                    transformation_=icp_output_tmp.transformation
                    templateID=str(i+1)
                    contronlSIGNAL=Bool(True)
            do_drawing_registration(source_, target, transformation_)

            if icp_output_tmp.transformation[0,3]==transformation_awkward[0,3] and  icp_output_tmp.transformation[1,3]==transformation_awkward[1,3]:
                transformation_=transformation_right
                do_publishing_pose(br,transformation_)

            y.right.goto_state(YuMiState(home_right),wait_for_res=False)
        do_publishing_pose(br,transformation_)
        pub_template.publish(templateID)
        pub_control.publish(contronlSIGNAL)

        cv2.imshow('frame',frame)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camObj=camera()
    main()


## NOTE:

#
# '''
# Function evaluate_registration calculates two main metrics.
# fitness measures the overlapping area (# of inlier correspondences / # of points in target). Higher the better.
# inlier_rmse measures the RMSE of all inlier correspondences. Lower the better.
# '''
