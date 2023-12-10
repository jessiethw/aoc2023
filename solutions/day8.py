import numpy as np
import pandas as pd
import re

#with open('../inputs/test8-3.txt') as f:
with open('../inputs/day8.txt') as f:
    inp = f.readlines()

directions = list(inp[0].rstrip('\n').replace('L','0').replace('R','1'))
directions = np.asarray(directions, dtype=int)
maps = {}
for m in inp[2:]:
    maps[m[:3]] = (m[7:10],m[12:15])

df = pd.DataFrame(maps)

def find_steps(start, end):
    steps = 0
    passed = False
    while not passed:
        for d in directions:
            start = df[start][d]
            steps +=1
        p = re.search(end, start)
        if p: passed = True
    return steps

steps = find_steps('AAA', 'ZZZ')
print('Answer to part 1: {}'.format(steps))

matches = []
for k in df.columns:
    m = re.search("(\w\w)A", k)
    if m: 
        print(find_steps(k, "(\w\w)Z"))


# steps = 0
# passed = 0
# while passed != len(matches):
#     passed = 0
#     for d in directions:
#         for i in range(len(matches)):
#             matches[i] = df[matches[i]][d]
#         steps+=1
#     for m in matches:
#         p = re.search("(\w\w)Z", m)
#         if p: passed+=1
#     print(steps)
