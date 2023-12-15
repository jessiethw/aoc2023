import numpy as np
import itertools as it
import pandas as pd

with open('../inputs/test14.txt') as f:
#with open('../inputs/day14.txt') as f:
    input = np.loadtxt(f, dtype=str, comments=None)

def roll(idx, col):
    rolling = True
    i = idx + 1
    while rolling:
        if i == len(col): break
        if col[i] == '.':
            col[i] = 'O'
            col[i-1] = '.'
            i+=1
        else:
            rolling = False
    return col

def roll_north(col):
    for i in range(len(col))[::-1]:
        if col[i] == 'O': col = roll(i, col)
    return col

def is_round(s):
    if s=='O': return True
    else: return False

def get_weight(col):
    m = list(map(is_round, col))
    loc = np.where(m)[0]
    weights = range(1,len(col)+1)[::-1]
    tot_weight =0
    for k in loc: tot_weight+= weights[k]
    return tot_weight

def washing_machine(puzzle):
    #north
    npuzzle = []
    for col in np.transpose(puzzle): 
        npuzzle.append(roll_north(col)[::-1])
    puzzle = np.asarray(npuzzle)

    #west
    npuzzle = []
    for row in np.transpose(puzzle): 
        npuzzle.append(roll_north(row[::-1])[::-1])
    puzzle = np.asarray(npuzzle)

    #south
    npuzzle = []
    for col in np.transpose(puzzle): 
        npuzzle.append(roll_north(col))
    puzzle = np.asarray(npuzzle)

    #east
    npuzzle = []
    for row in np.transpose(puzzle): 
        npuzzle.append(roll_north(row))
    puzzle = np.asarray(npuzzle[::-1])
    
    return puzzle

def dumb_repeat(puzzle, iter):
    soln = []
    for i in range(iter):
        puzzle = washing_machine(puzzle)
        # if puzzle.tolist() in soln:
        #     idx = (1000000001 - i)%len(soln)
        #     puzzle_out = soln[idx]
        #     return np.asarray(puzzle_out)
        soln.append(puzzle)#.tolist())
    print(soln)
    print('Failed in {} iterations'.format(iter))
    return None

puzzle = []
for line in input[::-1]:
    puzzle.append(list(line))
puzzle = np.asarray(puzzle)

soln = 0
for col in np.transpose(puzzle):
    new_col = roll_north(col)[::-1]
    soln+=get_weight(new_col)

print('Answer to part 1: {}'.format(soln))

puzzle = []
for line in input:
    puzzle.append(list(line))
puzzle = np.asarray(puzzle)
new_puzzle = washing_machine(puzzle)

bil_puzzle = dumb_repeat(new_puzzle, 3)
# soln = 0
# for col in np.transpose(bil_puzzle):
#     soln+=get_weight(col)

# print('Answer to part 2: {}'.format(soln))