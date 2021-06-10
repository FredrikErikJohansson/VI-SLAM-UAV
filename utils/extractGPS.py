import numpy as np
import pyproj
import open3d as o3d
import matplotlib.pyplot as plt

f = open('./DJI_0275.SRT')

lines = f.readlines()
lines = [line for line in lines if line.startswith('[iso')]
data = np.zeros([len(lines),3])
for i, line in enumerate(lines):
    parts = [elem.replace("]","") for elem in line.split()]
    lat = float(parts[24])
    lon = float(parts[26])
    alt = float(parts[28])
    data[i] = [lon, lat, alt]

np.savetxt('org.txt', data) # Save as org

wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')##4326
geocentric= pyproj.Proj('+proj=geocent +datum=WGS84 +units=m +no_defs') ##4978

geocentricdata = np.stack(pyproj.transform( wgs84, geocentric, data[:,0], data[:,1], data[:,2])).T

np.savetxt('geocentric.txt', geocentricdata) # Save to geocentric


# Save as ply
pcd = o3d.geometry.PointCloud()
pcd.colors = o3d.utility.Vector3dVector(np.ones([len(lines), 3]))
pcd.points = o3d.utility.Vector3dVector(geocentricdata)
o3d.io.write_point_cloud("./geocentric.ply", pcd)

pcd.colors = o3d.utility.Vector3dVector(np.ones([len(lines), 3]))
pcd.points = o3d.utility.Vector3dVector(data)
o3d.io.write_point_cloud("./org.ply", pcd)


# plt.scatter(geocentricdata[:,0], geocentricdata[:,1])
# plt.show()

# o3d.visualization.draw_geometries([pcd])

    