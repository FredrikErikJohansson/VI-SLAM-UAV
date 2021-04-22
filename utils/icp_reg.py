import open3d as o3d
import numpy as np
import math 
import copy

print("Load a ply point cloud, print it, and render it")
target = o3d.io.read_point_cloud("./MH02_GT.ply")
source = o3d.io.read_point_cloud("./pointcloud_ldso_mh02.ply")

# Outlier removal
#target, ind = target.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)
#source, ind = source.remove_statistical_outlier(nb_neighbors=20, std_ratio=2)


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0, 0])
    target_temp.paint_uniform_color([0, 1, 0])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])

threshold = 0.5

#Initial transform for ORB EuRoC
trans_init = np.asarray([[0.5, 0., 0., -3.],
                         [0, 0.5, 0, 0.5],
                         [0, 0, 0.5, -3], 
                         [0.0, 0.0, 0, 1.0]])

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

