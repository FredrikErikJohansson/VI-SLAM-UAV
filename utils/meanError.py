import open3d as o3d
import numpy as np
import sys
import math 

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
    [k, idx, _] = plyGT_tree.search_knn_vector_3d(current_point, 4)

    if k < 4:
        sys.exit("ERR: Not enough points in ground-truth")

    # Include current_point if its in grouth-truth
    [n, _, _] = plyGT_tree.search_radius_vector_3d(current_point, 0.0001)
    n = (1 if n>=1 else 0)

    # Construct a plane
    p0, p1, p2 = np.asarray(plyGT.points)[idx[(1-n):4-n], :]
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    ux, uy, uz = u = [x1-x0, y1-y0, z1-z0]
    vx, vy, vz = v = [x2-x0, y2-y0, z2-z0]
    u_cross_v = [uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx]
    point  = np.array(p0)
    a, b, c = normal = np.array(u_cross_v)
    d = -point.dot(normal)

    # Calculate perpendicular distance to the plane
    d = abs((a * current_point[0] + b * current_point[1] + c * current_point[2] + d))  
    e = (math.sqrt(a * a + b * b + c * c)) 
    mean_error += d/e

mean_error /= len(plyTest.points)
print("The mean error is:",mean_error)