import statistics 
import numpy as np
import pyperclip
import pandas as pd

def get_latex(data, row_names, format_str = None, best_low = True, midrules = None, bf = None):
    rows = []
    best_indices = np.argmin(data, axis=0) if best_low else  np.argmax(data, axis=0)
    if not bf:
        bf = [True for i in range(data.shape[1])]
    for i in range(data.shape[0]):
        row = "&".join([row_names[i]] + [f"\\textbf{{{elem:{format_str[j]}}}}" if (best_indices[j] == i and bf[j]) else f"{elem:{format_str[j]}}"  for j ,elem in enumerate(data[i,:])])
        row += "\\\\\n"
        rows.append(row)

        if midrules and i in midrules:
            rows.append("\\midrule \n")
    return rows


def meanstd(cols, file_name, format_str, names, fns):
    def calc(data,fn):
        return [fn(elem) for elem in data]

    x = np.array([calc(cols, fn) for fn in fns]).T
    res = get_latex(x, names, format_str=format_str)
    f = open(f"{file_name}.txt", "w") 
    f.writelines(res)
    f.close()
