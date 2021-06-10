import open3d as o3d
import numpy as np
from numpy import linalg as la
import sys
from csv import writer

if len(sys.argv) != 3:
    sys.exit("ERR: Not enough input parameters\nUsage: ./meanError plyTest plyGroundTruth")   

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)

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

plyTest = o3d.io.read_point_cloud(sys.argv[1] + plyTestEnding)
plyGT = o3d.io.read_point_cloud(sys.argv[2] + plyGTEnding)

plyTest.paint_uniform_color([1, 0, 0])
plyGT.paint_uniform_color([0, 1, 0])
o3d.visualization.draw_geometries([plyTest, plyGT],
                                      zoom=0.4459,
                                      front=[0.9288, -0.2951, -0.2242],
                                      lookat=[1.6784, 2.0612, 1.4451],
                                      up=[-0.3402, -0.9189, -0.1996])

print("Test:",plyTest)
print("Ground-truth:",plyGT)
plyGT_tree = o3d.geometry.KDTreeFlann(plyGT)
mean_error = 0
for current_point in plyTest.points:
    # Find current_point's 4 nearest neighbors
    [k, idx, _] = plyGT_tree.search_knn_vector_3d(current_point, 2)

    if k < 2:
        sys.exit("ERR: Not enough points in ground-truth")

    # Compute distance to line
    p0, p1 = np.asarray(plyGT.points)[idx[0:], :]
    length = la.norm(p0-p1)
    if length == 0:
        d = la.norm(current_point-p0)
    else:
        t = max(0, min(1, np.dot(current_point-p0, p1-p0)/(length*length)))
        p2 = p0+t*(p1-p0)
        d = la.norm(current_point-p2)
    mean_error += d

mean_error /= len(plyTest.points)

row_contents = [len(plyTest.points), len(plyGT.points), mean_error]
append_list_as_row('result.csv', row_contents)

print("The mean error is:",mean_error)