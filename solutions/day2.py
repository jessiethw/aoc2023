import numpy as np

#with open('../inputs/test2.txt') as f:
with open('../inputs/day2.txt') as f:
    inputs=f.readlines()

games = {}
# Formatting...
for g in inputs:
    first_spl = g.replace('\n', '').split(':')
    sec_split = first_spl[1].split(';')
    key = int(first_spl[0].replace('Game ',''))
    games[key] = []
    for item in sec_split:
        # order into tuples, (r, g, b)
        third_split = item.split(',')
        tup = [0, 0, 0]
        for s in third_split:
            if 'red' in s: tup[0] = int(s.replace(' red',''))
            elif 'green' in s: tup[1] = int(s.replace(' green',''))
            elif 'blue' in s: tup[2] = int(s.replace(' blue',''))
        games[key].append(tuple(tup))

def partOne(games):
    #checking which are possible
    cubes = (12, 13, 14)
    not_allowed = []
    for k in games.keys():
        for tup in games[k]:
            for i in range(3): 
                if tup[i]>cubes[i]: not_allowed.append(k)

    for n in np.unique(not_allowed): games.pop(n)

    print('Part 1 Solution: {}'.format(sum(games.keys())))

def partTwo(games):
    pow=[]
    for k in games.keys():
        r, g, b = list(map(list, zip(*games[k])))
        pow.append(max(r)*max(g)*max(b))
    
    print('Part 2 Solution: {}'.format(sum(pow)))

partTwo(games)
partOne(games)
