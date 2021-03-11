import open3d as o3d
import numpy as np
from numpy import linalg as la
import sys

if len(sys.argv) != 3:
    sys.exit("ERR: Not enough input parameters\nUsage: ./meanError plyTest plyGroundTruth")   

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

print("Test:",plyTest)
print("Ground-truth:",plyGT)
plyGT_tree = o3d.geometry.KDTreeFlann(plyGT)

mean_error = 0
for current_point in plyTest.points:
    # Find current_point's 4 nearest neighbors
    [k, idx, _] = plyGT_tree.search_knn_vector_3d(current_point, 3)

    if k < 3:
        sys.exit("ERR: Not enough points in ground-truth")

    # Include current_point if its in grouth-truth
    [n, _, _] = plyGT_tree.search_radius_vector_3d(current_point, 0.0001)
    n = (1 if n>=1 else 0)

    # Compute distance to line
    p0, p1 = np.asarray(plyGT.points)[idx[(1-n):3-n], :]
    d = la.norm(np.cross(p1-p0, p0-current_point))/la.norm(p1-p0)
    mean_error += d

mean_error /= len(plyTest.points)
print("The mean error is:",mean_error)