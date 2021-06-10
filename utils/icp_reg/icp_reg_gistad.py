import open3d as o3d
import numpy as np
import math 
import copy
import sys
from csv import writer

# Check for file-ending
plyTestEnding = ""
plyGTEnding = ""
if len(sys.argv[1]) < 4:
    plyTestEnding = ".ply"
elif sys.argv[1][len(sys.argv[1])-4] != '.':
    plyTestEnding = ".ply"

if len(sys.argv[2]) < 4:
    plyGTEnding = ".ply"
elif sys.argv[2][len(sys.argv[2])-4] != '.':
    plyGTEnding = ".ply"

source = o3d.io.read_point_cloud(sys.argv[1] + plyTestEnding)
target = o3d.io.read_point_cloud(sys.argv[2] + plyGTEnding)
point_ORB = o3d.io.read_point_cloud("./gistad_smooth_mono_ORB_1.ply")

# Outlier removal
#target, ind = target.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0, 0]) # Source = red
    target_temp.paint_uniform_color([0, 1, 0]) # Target = green
    source_temp.transform(transformation)
    asd = source.get_axis_aligned_bounding_box()
    asdasd = target.get_axis_aligned_bounding_box()
    #tri = o3d.geometry.TriangleMesh.create_coordinate_frame()
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])

def get_rot_mat(axis, angle):
    if axis == 'x':
        return np.asarray([
            [1, 0, 0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle), math.cos(angle)]])
    if axis == 'y':
        return np.asarray([
            [math.cos(angle), 0, math.sin(angle)],
            [0, 1, 0],
            [-math.sin(angle), 0, math.cos(angle)]])
    if axis == 'z':
        return np.asarray([
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]])

threshold = 0.5

trans_init = np.asarray([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]])




#ORB
points = np.asarray(source.points)
trans_ORB = np.mean(points, axis=0)
points = points - trans_ORB
scale_ORB = np.std(points)
points = points / scale_ORB 
source.points = o3d.cpu.pybind.utility.Vector3dVector(points)

# ORB pointcloud
orb_points = np.asarray(point_ORB.points)
trans_ORB_points = np.mean(orb_points, axis=0)
print("mean", trans_ORB_points)
print("points", orb_points)

orb_points = orb_points - trans_ORB_points
scale_ORB_points = np.std(orb_points)
print("std", np.std(orb_points))
orb_points = orb_points / scale_ORB_points
#orb_points = orb_points - trans_ORB
#orb_points = orb_points / scale_ORB
point_ORB.points = o3d.cpu.pybind.utility.Vector3dVector(orb_points)

#geocentric
points2 = np.asarray(target.points)
trans = np.mean(points2, axis = 0)
points2 = points2 - trans
scale = np.std(points2)
points2 = points2 / scale
#target.points = o3d.cpu.pybind.utility.Vector3dVector(points2)




# Initial alignment here
#print(source.points)
point_ORB, ind = point_ORB.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)
# draw_registration_result(source, target, trans_init)
#source.scale(1, source.get_center())



source.rotate(get_rot_mat('x', math.pi), source.get_center())
source.rotate(get_rot_mat('y', -math.pi/4), source.get_center())

#point_ORB = point_ORB.rotate(get_rot_mat('x', math.pi), point_ORB.get_center())
print(get_rot_mat('x', math.pi), point_ORB.get_center())
#point_ORB = point_ORB.rotate(get_rot_mat('y', -math.pi/4), point_ORB.get_center())
print(get_rot_mat('y', -math.pi/4), point_ORB.get_center())




# Point_ORBs rotations for world pos -> geocentric
# orb_trans_to_center = np.asarray([[1, 0, 0, -0.01968551]
#     ,[0, 1, 0, -0.00078007]
#     ,[0, 0, 1, -0.00245327]
#     ,[0, 0, 0, 1]])

orb_rot_x = np.asarray([[ 1.0000000e+00,  0.0000000e+00,  0.0000000e+00, 0.]
    ,[ 0.0000000e+00, -1.0000000e+00, -1.2246468e-16, 0.]
    ,[ 0.0000000e+00,  1.2246468e-16, -1.0000000e+00, 0.]
    ,[ 0.,          0.,          0.,          1.]]) #center: [-0.01968551 -0.00078007 -0.00245327]


orb_rot_y = np.asarray([[ 0.70710678,  0.,         -0.70710678, 0.]
    ,[ 0.,          1.,          0.,        0.]
    ,[ 0.70710678,  0.,          0.70710678, 0.]
    ,[ 0.,          0.,          0.,          1.]]) #center: [-0.01968551 -0.00078007 -0.00245327]

# orb_trans_back = np.asarray([[1, 0, 0, 0.01968551]
#     ,[0, 1, 0, 0.00078007]
#     ,[0, 0, 1, 0.00245327]
#     ,[0, 0, 0, 1]])




#source.rotate(get_rot_mat('y', math.pi/4), source.get_center())
#target.scale(100, source.get_center())
#source.scale(100, source.get_center())
#source.translate((0,1,2.5))
# source.rotate(get_rot_mat('x', -math.pi/2 - math.pi/8), source.get_center())
# source.rotate(get_rot_mat('z', -math.pi/2 + math.pi/8), source.get_center())

#draw_registration_result(source, target, trans_init)

# print("Initial alignment")
# evaluation = o3d.pipelines.registration.evaluate_registration(
#     source, target, threshold, trans_init)
# print(evaluation)


# reg_p2p = o3d.pipelines.registration.registration_icp(
#     source, target, threshold, trans_init,
#     o3d.pipelines.registration.TransformationEstimationPointToPoint(with_scaling=False),
#     o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=200))
# print(reg_p2p)
# print("Transformation is:")
# print(reg_p2p.transformation)
# draw_registration_result(source, target, reg_p2p.transformation)

#source.transform(reg_p2p.transformation)

trans_init_boy = np.asarray([[ 0.56069522,  0.77439823,  0.2931352,   0.03059684]
 ,[-0.41783235,  0.57025177, -0.70726873,  0.01357388]
 ,[-0.71486852,  0.27408083,  0.64330607, -0.02221874]
 ,[ 0.,          0.,          0.,          1.        ]])


trans_init_boy2 = np.asarray([[ 0.48317586,  0.66164968,  0.24369843,  0.24839897]
 ,[-0.37064238,  0.48965084, -0.59455397,  0.1946286 ]
 ,[-0.59982785,  0.23041245,  0.56368856, -0.18015819]
 ,[ 0.,          0.,          0.,          1.        ]])


point_ORB.transform(orb_rot_x)
point_ORB.transform(orb_rot_y)
point_ORB.transform(trans_init_boy)
# append_list_as_row('result.csv', [sys.argv[1]])
# row_contents = [reg_p2p.fitness, reg_p2p.inlier_rmse]
# append_list_as_row('result.csv', row_contents)

target.paint_uniform_color([0, 0, 0])

#To geocentric
orb_points = np.asarray(point_ORB.points)
#print(scale_ORB_points)
orb_points = orb_points / scale_ORB_points
orb_points = orb_points - trans_ORB_points

orb_points = orb_points * scale
orb_points = orb_points + trans

point_ORB.points = o3d.cpu.pybind.utility.Vector3dVector(orb_points)

#point_ORB = point_ORB.rotate(get_rot_mat('x', math.pi), point_ORB.get_center())
#point_ORB = point_ORB.rotate(get_rot_mat('z', -math.pi/4))


asd = target.get_axis_aligned_bounding_box()
asdasd = point_ORB.get_axis_aligned_bounding_box()

o3d.visualization.draw_geometries([ target, point_ORB, asd, asdasd])

print(np.min(point_ORB.points))
print(np.max(point_ORB.points))

# Save as ply
#print(len(point_ORB.points))
point_ORB.colors = o3d.utility.Vector3dVector(np.ones([len(point_ORB.points), 3]))
o3d.io.write_point_cloud("ORB_geocentric_pointcloud.ply", point_ORB)


o3d.io.write_point_cloud("TARGET.ply", target)
o3d.io.write_point_cloud("SOURCE.ply", source)

