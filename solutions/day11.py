import numpy as np
import itertools as it
import pandas as pd

#with open('../inputs/test11.txt') as f:
with open('../inputs/day11.txt') as f:
    input = np.loadtxt(f, dtype=str, comments=None)

def make_bool(s):
    if s=='.': return False
    else: return True

def expand(arr):
    empty_row = np.where(np.all(~arr, axis=1))[0]
    empty_col = np.where(np.all(~arr, axis=0))[0]
    passed = 0
    for r in empty_row:
        arr = np.insert(arr, r+passed+1, np.array([False]*arr.shape[1]), axis=0)
        passed+=1
    passed = 0
    for c in empty_col:
        arr = np.insert(arr, c+passed+1, np.array([False]*arr.shape[0]), axis=1)
        passed+=1
    return arr

def expand2(df, factor):
    empty_row = np.where(np.all(~df, axis=1))[0]
    empty_col = np.where(np.all(~df, axis=0))[0]
    inc = 0
    new_cols, new_rows = [], []
    for col in df.columns:
        if col in empty_col: inc += factor-1
        new_cols.append(col+inc)
    inc =0
    for row in df.index:
        if row in empty_row: inc+= factor-1
        new_rows.append(row+inc)
    df.columns = new_cols
    df.index = new_rows
    return df

def dist_btwn(gal1, gal2):
    diff = np.array([abs(gal1[1] - gal2[1]), abs(gal1[0] - gal2[0])])
    return  sum(diff)

def dist_btwn2(gal1, gal2, df):
    gal1_coord = (df.index[gal1[0]], df.columns[gal1[1]])
    gal2_coord = (df.index[gal2[0]], df.columns[gal2[1]])
    return abs(gal1_coord[1] - gal2_coord[1])+ abs(gal1_coord[0] - gal2_coord[0])

new_arry = [list(map(make_bool, line)) for line in input]
msk = np.array(new_arry)

new_msk = expand(msk)

loc = np.where(new_msk)
combs = list(it.combinations(range(len(loc[0])),2))

dists = []
for c in combs:
    d = dist_btwn((loc[0][c[0]],loc[1][c[0]]),
                  (loc[0][c[1]],loc[1][c[1]]))
    dists.append(d)
print('Answer to part 1: {}'.format(sum(dists)))

df_msk = pd.DataFrame(msk)
new_df = expand2(df_msk, 1000000)

loc2 = np.where(msk)
combs2 = list(it.combinations(range(len(loc[0])),2))

dists2 = []
for c in combs2:
    d = dist_btwn2((loc2[0][c[0]],loc2[1][c[0]]),
                  (loc2[0][c[1]],loc2[1][c[1]]),
                  new_df)
    dists2.append(d)
print('Answer to part 2: {}'.format(sum(dists2)))