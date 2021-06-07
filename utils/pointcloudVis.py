import open3d as o3d
import numpy as np

print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("./pointcloud.ply")
print(pcd)
print(np.asarray(pcd.points))
import matplotlib.pyplot as plt
print("Statistical oulier removal")
pcd, ind = pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=1)
#flip z component of normals if needed
#points = np.asarray(pcd.points)
#points[:,2] = -points[:,2]
#pcd.points = o3d.utility.Vector3dVector(points)  # invalidate existing normals

print("normals")
pcd.normals = o3d.utility.Vector3dVector(np.zeros((1, 3)))  # invalidate existing normals
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid( radius=3.0, max_nn=500))
pcd.orient_normals_consistent_tangent_plane(100)
#pcd.orient_normals_to_align_with_direction(
#    np.array([0., 0., -1.])
#)
# print("Ball pivoting reconstruction")
# distances = pcd.compute_nearest_neighbor_distance()
# avg_dist = np.mean(distances)
# radius = 3 * avg_dist
# bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd,o3d.utility.DoubleVector([radius, radius * 2]))
# dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
# dec_mesh.remove_degenerate_triangles()
# dec_mesh.remove_duplicated_triangles()
# dec_mesh.remove_duplicated_vertices()
# dec_mesh.remove_non_manifold_edges()
# radii = [0.001, 0.01, 0.02, 1]
# rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
#     pcd, o3d.utility.DoubleVector(radii))


# print('Poisson surface reconstruction')
# with o3d.utility.VerbosityContextManager(
#         o3d.utility.VerbosityLevel.Debug) as cm:
#     poisson_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
#         pcd, depth=12, scale=1, linear_fit=True)

# bbox = pcd.get_axis_aligned_bounding_box()
# p_mesh_crop = poisson_mesh.crop(bbox)

# print('visualize densities')
# densities = np.asarray(densities)
# density_colors = plt.get_cmap('plasma')(
#     (densities - densities.min()) / (densities.max() - densities.min()))
# density_colors = density_colors[:, :3]
# density_mesh = o3d.geometry.TriangleMesh()
# density_mesh.vertices = poisson_mesh.vertices
# density_mesh.triangles = poisson_mesh.triangles
# density_mesh.triangle_normals = poisson_mesh.triangle_normals
# density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
# print('remove low density vertices')
# vertices_to_remove = densities < np.quantile(densities, 0.01)
# mesh.remove_vertices_by_mask(vertices_to_remove)

#pcd.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([pcd], point_show_normal=True)