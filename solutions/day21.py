import numpy as np

#with open('../inputs/test21.txt') as f:
with open('../inputs/day21.txt') as f:
    inp = np.loadtxt(f, dtype=str, comments=None)

nstep = 64

def make_bool(v):
    if v == '.': return True
    elif v =='S': return True
    else: return False

def check_valid(a, shape):
    a = list(a)
    if -1 in a:
        a.pop(-1)
    elif shape[1] in a:
        a.pop(shape[1])
    return a

m = np.asarray([list(i) for i in inp])

bool_arr = np.asarray([[False]*m.shape[1]]*m.shape[0])
bool_arr[np.where(m=='S')] = True

for s in range(nstep):
    spots = np.where(bool_arr)
    idx = [(spots[0][i], spots[1][i]) for i in range(len(spots[0]))]
    new_arr = np.asarray([[False]*m.shape[1]]*m.shape[0])
    for i in idx: 
        ix = check_valid(np.asarray([i[0]-1,i[0]+1]), m.shape)
        nx = len(ix)
        iy = check_valid(np.asarray([i[1]-1,i[1]+1]), m.shape)
        ix = np.concatenate([np.asarray(ix), np.asarray([i[0]]*len(iy))])
        iy = np.concatenate([np.asarray([i[1]]*nx), np.asarray(iy)])
        new_idx = (ix, iy)
        new_arr[new_idx] = list(map(make_bool, m[new_idx]))
    bool_arr = new_arr
print('Answer to part 1: {}'.format(len(np.where(bool_arr)[0])))
