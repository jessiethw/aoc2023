import numpy as np
import pandas as pd

#with open('../inputs/test13.txt') as f:
with open('../inputs/day13.txt') as f:
    input = f.readlines()

def find_mirror(puzzle):
    for i in range(1,len(puzzle)):
        if np.all(puzzle[i-1] == puzzle[i]):
            if (i==1) or (i==len(puzzle)-1): 
                return i
            elif np.all(puzzle[i-2] == puzzle[i+1]):
                if (i==2) or (i==len(puzzle)-2): 
                    return i
                elif np.all(puzzle[i-3] == puzzle[i+2]): 
                    if (i==3) or (i==len(puzzle)-3): 
                        return i
                    elif np.all(puzzle[i-4] == puzzle[i+3]): 
                        if (i==4) or (i==len(puzzle)-4): 
                            return i
                        elif np.all(puzzle[i-5] == puzzle[i+4]): 
                            if (i==5) or (i==len(puzzle)-5): 
                                return i
                            elif np.all(puzzle[i-6] == puzzle[i+5]): 
                                return i
    return None

puzzles = {}
new_arry = []
i = 0
for line in input:
    if ('#' not in line) or ('.' not in line):
        puzzles[i] = np.array(new_arry, dtype=str)
        new_arry = []
        i+=1
    else:
        new_arry.append(list(line.rstrip('\n')))
puzzles[i] = np.array(new_arry,dtype=str)

note_sum = 0
for puzz in puzzles.keys():
    row = find_mirror(puzzles[puzz])
    if row == None:
        col = find_mirror(np.transpose(puzzles[puzz]))
        note_sum += col
    else: 
        note_sum +=(row)*100

print('Answer to part 1: {}'.format(note_sum))