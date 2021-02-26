import open3d as o3d
import numpy as np

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("./pointcloud.ply")
print(pcd)
print(np.asarray(pcd.points))
import matplotlib.pyplot as plt
print("Statistical oulier removal")
pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=40,
                                                    std_ratio=0.0002)
#flip z component of normals if needed
#points = np.asarray(pcd.points)
#points[:,2] = -points[:,2]
#pcd.points = o3d.utility.Vector3dVector(points)  # invalidate existing normals

print("normals")
pcd.normals = o3d.utility.Vector3dVector(np.zeros((1, 3)))  # invalidate existing normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
        radius=1.0, max_nn=100))
pcd.orient_normals_consistent_tangent_plane(100)

# print("triangulation")
# radii = [0.005, 0.01, 0.02, 0.04]
# rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
#     pcd, o3d.utility.DoubleVector(radii))


# print('run Poisson surface reconstruction')
# with o3d.utility.VerbosityContextManager(
#         o3d.utility.VerbosityLevel.Debug) as cm:
#     mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
#         pcd, depth=9,scale=0.7, linear_fit=True)

o3d.visualization.draw_geometries([pcd], point_show_normal=True)
