import numpy as np

#with open('../inputs/test5.txt') as f:
with open('../inputs/day5.txt') as f:
    inp=f.readlines()

inputs={}
for line in inp[1:]:
    if line =='\n': continue
    elif line[0].isalpha(): 
        key = line.split(' ')[0]
        inputs[key] = []
    else: 
        maps = [int(l) for l in line.rstrip('\n').split(' ')]
        inputs[key].append(maps)

def get_locale(seeds, inputs):
    location = 100000000000
    for seed in seeds:
        for val in inputs.keys():
            for mapping in inputs[val]:
                if seed >= mapping[1] and seed < (mapping[1] + mapping[2]): 
                    seed = mapping[0] + (seed - mapping[1])
                    break
        location=min(seed,location)
    return location

seeds1 = [int(i) for i in inp[0].rstrip('\n').split(' ')[1:]]
location = get_locale(seeds1, inputs)
print('Answer to part 1: {}'.format(location))

s = list(zip(*(seeds1[::2], seeds1[1::2])))

#This all is very inefficient and takes wayyyy too long. 
#Might work on another solution later...

# loc = []
# for seeds2 in [range(set[0],set[0]+set[1]) for set in s]:
#     print(seeds2)
#     loc.append(get_locale(seeds2, inputs))

# # print('Answer to part 2: {}'.format(min(loc)))