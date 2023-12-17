import numpy as np
import itertools as it
import pandas as pd

#with open('../inputs/test15.txt') as f:
with open('../inputs/day15.txt') as f:
    inp = pd.read_csv(f, header=None)

def get_ascii(cha):
    return ord(cha)

def hash(seq):
    ascii = list(map(get_ascii, list(seq)))
    current = 0
    for a in ascii:
        current = ((a + current)*17)%256
    return current

def find_label(arr):
    if len(arr) > 0:
        arr = np.transpose(np.asarray(arr))
        return arr[0]
    else: return arr

def focusing_power(box_num, lenses):
    return sum([(box_num+1)*(i+1)*(int(lenses[i][1])) for i in range(len(lenses))])

result = [hash(inp[v].values[0]) for v in inp.keys()]

print('Answer to part 1: {}'.format(sum(result)))

box = {k: [] for k in range(256)}
for v in inp.keys():
    s = inp[v].values[0]
    if '=' in s:
        label = s.split('=')
        key = hash(label[0])
        in_box = find_label(box[key])
        if label[0] not in in_box:
            box[key].append(label)
        else:
            idx = np.where(np.array(in_box)==label[0])[0][0]
            box[key][idx][1] = label[1]

    if '-' in s:
        label = s.split('-')
        key = hash(label[0])
        in_box = find_label(box[key])
        if label[0] in in_box:
            idx = np.where(np.array(in_box)==label[0])[0][0]
            box[key].pop(idx)

tot_fp = 0
for k in box.keys():
    if len(box[k])==0: continue
    tot_fp+=focusing_power(k, box[k])

print('Answer to part 2: {}'.format(tot_fp))