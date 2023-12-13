import numpy as np

with open('../inputs/test10-4.txt') as f:
#with open('../inputs/day10.txt') as f:
    input = f.readlines()

def next(string, coord, prev):
    if string == '|': 
        borders = [[coord[0]+1, coord[1]],
                   [coord[0]-1, coord[1]]]
    elif string == '-': 
        borders = [[coord[0], coord[1]+1],
                   [coord[0], coord[1]-1]]
    elif string == 'L':
        borders = [[coord[0], coord[1]+1],
                   [coord[0]-1, coord[1]]]
    elif string == 'F':
        borders = [[coord[0]+1, coord[1]],
                   [coord[0], coord[1]+1]]
    elif string == 'J':
        borders = [[coord[0]-1, coord[1]],
                   [coord[0], coord[1]-1]]
    elif string == '7':
        borders = [[coord[0]+1, coord[1]],
                   [coord[0], coord[1]-1]]
    else: return None

    borders = np.asarray(borders)
    prev = np.asarray(prev)
    return borders[np.where(borders != prev)[0][0]]

def is_enclosed(arr):
    msk1, msk2 = [], []
    for row in arr: 
        encl = False
        new_row = []
        for elem in row:
            if not elem: 
                if encl: new_row.append(True)
                else: new_row.append(False)
            else: 
                encl = ~encl
                new_row.append(False)
        msk1.append(new_row)
    msk1 = np.asarray(msk1)

    for row in np.transpose(arr): 
        encl = False
        new_row = []
        for elem in row:
            if not elem: 
                if encl: new_row.append(True)
                else: new_row.append(False)
            else: 
                encl = ~encl
                new_row.append(False)
        msk2.append(new_row)
    msk2 = np.transpose(np.asarray(msk2))

    return msk1*msk2

coords = []
for line in range(len(input)):
    if 'S' in input[line]: 
        coords.append(line)
        row = np.asarray(list(input[line]))
        coords.append(np.where(row=='S')[0][0])

check = []
for i in range(-1,2):
    for j in range(-1,2):
        check.append([coords[0]+i,coords[1]+j])

for c in check:
    c = np.asarray(c)
    if np.any(c == -1): continue

    first_step = input[c[0]][c[1]]
    if first_step == '|':
        first_coords = c
        break

path = [first_coords]
while first_step != 'S':
    loc = next(first_step, first_coords, coords)
    coords = first_coords
    first_coords = loc
    first_step = input[loc[0]][loc[1]]
    path.append(loc)

print('Answer to part 1: {}'.format(int(np.ceil(len(path)/2.))))

new_arr = np.full((len(input), len(input[0][:-1])), fill_value=False, dtype=bool)
#print(new_arr)
for idx in path:
    new_arr[idx[0]][idx[1]]=True

msk = is_enclosed(new_arr)
print('Answer to part 2: {}'.format(np.where(msk)[0].size))