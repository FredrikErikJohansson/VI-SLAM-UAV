import numpy as np
from meanstd import meanstd

f = open("/home/samsv/Downloads/orb_gistad_smooth.csv")
lines = [elem.strip("\n") for elem in f.readlines()]

data = {}
N = len(lines) // 3
for i in range(N):
    key = lines[i*3].split("_")[2]
    numbers_1 = [float(elem) for elem in lines[i*3+1].split(",")[:2]]
    numbers_2 = [float(elem) for elem in lines[i*3+2].split(",")]
    if key in data:
        data[key].append(numbers_1 + numbers_2)
    else:
        data[key] = [numbers_1 + numbers_2]


fns = [np.mean, np.median, np.std, np.min, np.max]

# Add every sequence to seq_names if more than one
seq_names = ["Gistad Oblique"]
format_str = [".5f",".5f",".5f",".5f",".5f"] #decimal precision for every col
names = ["Gistad_Oblique_Fitness", "Gistad_Oblique_Inlier", "Gistad_Oblique_points_src", "Gistad_Oblique_points_dst", "Gistad_Oblique_MPPE"]
for i in range(5):
    cols = [np.array(data[key])[:,i] for key in data.keys()]
    meanstd(cols,names[i], format_str, seq_names, fns)