import open3d as o3d
import numpy as np
import math 
import copy

print("Load a ply point cloud, print it, and render it")
source = o3d.io.read_point_cloud("./ORB_V101_mono.ply")
target = o3d.io.read_point_cloud("./LDSO_V101_mono.ply")

# Outlier removal
target, ind = target.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)
source, ind = source.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)

def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0, 0]) # Source = red
    target_temp.paint_uniform_color([0, 1, 0]) # Target = green
    source_temp.transform(transformation)
    asd = source.get_axis_aligned_bounding_box()
    asdasd = target.get_axis_aligned_bounding_box()
    o3d.visualization.draw_geometries([source_temp, target_temp,asd,asdasd],
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
# Initial alignment here
#source.scale(4, source.get_center())
source.rotate(get_rot_mat('x', -math.pi/8), source.get_center())
#source.rotate(get_rot_mat('y', -math.pi/2), source.get_center())
#source.rotate(get_rot_mat('y', -math.pi/8), source.get_center())
target.rotate(get_rot_mat('x', -math.pi/8), target.get_center())


draw_registration_result(source, target, trans_init)

print("Initial alignment")
evaluation = o3d.pipelines.registration.evaluate_registration(
    source, target, threshold, trans_init)
print(evaluation)


reg_p2p = o3d.pipelines.registration.registration_icp(
    source, target, threshold, trans_init,
    o3d.pipelines.registration.TransformationEstimationPointToPoint(with_scaling=True),
    o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=2000))
print(reg_p2p)
print("Transformation is:")
print(reg_p2p.transformation)
draw_registration_result(source, target, reg_p2p.transformation)

# Save as ply
o3d.io.write_point_cloud("TARGET.ply", target)
o3d.io.write_point_cloud("SOURCE.ply", source)

