
import os
from meanstd import meanstd
from meanstd import get_latex
import glob
import numpy as np

def read_values(fname):
    f = open(fname)
    lines = f.readlines()
    return np.array([line.split()[1] for line in lines[1:-1]])

N = 10
M = 1
# Change string
file_names = [[f"/home/samsv/Documents/Exjobb/VI-SLAM-UAV/utils/MH{j:02d}_data_LDSO_{i}.txt" for i in range(1,N+1)] for j in range(1,M+1)]

all_data = np.zeros([N,M,6])

for i in range(N):
    for j in range(M):
        all_data[i,j] = read_values(file_names[j][i])


print(all_data[:,:,:].mean(axis=0))

all_data = np.concatenate([all_data[:,:,1:], all_data[:,:,0:1]], axis=2)

fns = [np.mean, np.mean, np.mean, np.mean, np.mean, np.mean]
format_str = [".3f", ".3f",".3f",".3f",".3f",".3f"] # decimal precision for every col
seq_names = ["Machine Hall 1", "Machine Hall 2","Machine Hall 3",  "Machine Hall 4",  "Machine Hall 5"]
bf = [False for i in range(6)] # Do not bold lowest values

res = get_latex(all_data.mean(axis=0), seq_names, format_str=format_str,bf=bf)
f = open("ATE_MH_LDSO.txt", "w") 
f.writelines(res)
f.close()