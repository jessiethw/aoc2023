import numpy as np

with open('../inputs/test16.txt') as f:
#with open('../inputs/day16.txt') as f:
    inp = np.loadtxt(f, dtype=str, comments=None)

def ref(m, prev_idx, current_idx):
    dx = current_idx[0] - prev_idx[0]
    dy = current_idx[1] - prev_idx[1]
    if m[current_idx[0]][current_idx[1]] == '.':
        return [[current_idx[0] +dx,
                current_idx[1] +dy]]
    elif m[current_idx[0]][current_idx[1]] == '/':
        return [[current_idx[0] -dy,
                current_idx[1] -dx]]
    elif m[current_idx[0]][current_idx[1]] == '\\':
        return [[current_idx[0] +dy,
                current_idx[1] +dx]]
    elif m[current_idx[0]][current_idx[1]] == '|':
        if abs(dy) == 1: 
            return [[current_idx[0]-dy, current_idx[1]],
                    [current_idx[0]+dy, current_idx[1]]]
        else:
            return [[current_idx[0] +dx,
                    current_idx[1] +dy]]
    elif  m[current_idx[0],current_idx[1]] == '-':
        if abs(dx) == 1: 
            return [[current_idx[0], current_idx[1]-dx],
                    [current_idx[0], current_idx[1]+dx]]
        else:
            return [[current_idx[0] +dx,
                    current_idx[1] +dy]]

def is_valid(m, idx):
    valid = True
    if np.any(np.array(idx)<0): 
        valid=False
    elif np.any(np.array(idx)>len(m[0])): 
        valid=False
    elif np.any(np.array(idx)>len(m)): 
        valid=False

    return valid

mp = np.asarray([list(row) for row in inp])

prev_idx = [[0,-1]]
idx = [[0,0]]
path = [[0,0]]
dp=1
while dp == 1:
    for i in range(len(idx)):
        new_idx = ref(mp, prev_idx[i], idx[i])
        print(prev_idx[i], idx[i])
        for n in new_idx:
            check = is_valid(mp, n)
            if check and (n not in path): 
                path.append(n)
            else: 
                new_idx.remove(n)
        print(new_idx)
    if len(new_idx)==0: 
        dp=0
    else:
        prev_idx = idx
        idx = new_idx
print(path)

# while len(check) >0:
#     prev_init = init
#     init = new_init
#     new_init = 

# print(new_init)

