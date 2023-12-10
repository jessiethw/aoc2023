import numpy as np
import pandas as pd

#with open('../inputs/test9.txt') as f:
with open('../inputs/day9.txt') as f:
    sequencies = pd.read_csv(f, delimiter=' ', header=None)

def get_next(seq):
    seq = np.asarray(seq)
    arrs = [seq[-1]]
    while not np.all(seq==0):
        seq = np.diff(seq)
        arrs.append(seq[-1])
    return sum(arrs)

def get_prev(seq):
    seq = np.asarray(seq)
    arrs = [seq[0]]
    while not np.all(seq==0):
        seq = np.diff(seq)
        arrs.append(seq[0])
    new_val = 0
    for v in arrs[::-1][1:]:
        new_val = v - new_val
    return new_val

next_elem, prev_elem = [], []
for i in sequencies.index:
    next_elem.append(get_next(sequencies.loc[i].values))
    prev_elem.append(get_prev(sequencies.loc[i].values))

print('Answer to part 1: {}'.format(sum(next_elem)))
print('Answer to part 2: {}'.format(sum(prev_elem)))