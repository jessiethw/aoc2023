import numpy as np

with open('../inputs/test17.txt') as f:
#with open('../inputs/day17.txt') as f:
    inp = np.loadtxt(f, dtype=str, comments=None)

def make_arr(row):
    return [int(i) for i in list(row)]

def find_min_adj(mat, idx, prev_idx):
    dx = idx[1] - prev_idx[1]
    dy = idx[0] - prev_idx[0]
    
    if abs(dx)==1:
        new_idx = [idx[0] - 1, idx[0] + 1]
        if (-1 in new_idx): 
            new_idx.remove(-1)
        elif (arr.shape[0] in new_idx):
            new_idx.remove(arr.shape[0])
        val = min([mat[idx[0],n] for n in new_idx])
        print(val)

arr = np.asarray(list(map(make_arr, inp)))
find_min_adj(arr, [0,0],[0,-1])