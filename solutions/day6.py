import numpy as np
import re

#with open('../inputs/test6.txt') as f:
with open('../inputs/day6.txt') as f:
    inp=f.readlines()

inputs={}
for line in inp:
    key = line.split(':')[0]
    val = re.split('\s+',line.rstrip('\n'))
    inputs[key] = [int(v) for v in val[1:]]

def ways_to_win(inputs):
    beat_the_record=1
    for game in range(len(inputs['Time'])):
        start_guess = int(np.floor(inputs['Distance'][game] / inputs['Time'][game]))
        success = 0
        for t in range(start_guess, inputs['Time'][game]):
            travel = (inputs['Time'][game] - t)*t
            if travel > inputs['Distance'][game]:
                if t == start_guess: print('Succeeded on first guess :(')
                success+=1
            else:
                if success > 0: break
        beat_the_record *= success
    return beat_the_record

beat_the_record = ways_to_win(inputs)
print('Answer to part 1: {}'.format(beat_the_record))

inputs2={}
for line in inp:
    key = line.split(':')[0]
    val = line.split(':')[1].rstrip('\n').replace(' ','')
    inputs2[key] = [int(val)]

beat_the_record = ways_to_win(inputs2)
print('Answer to part 2: {}'.format(beat_the_record))