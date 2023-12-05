import numpy as np

#with open('../inputs/test4.txt') as f:
with open('../inputs/day4.txt') as f:
    inputs=f.readlines()

cards={}
for li in inputs:
    key = int(li.split(':')[0].replace('Card ',''))
    winners, nums = [], []
    for i in li.split(': ')[1].split(' | ')[0].split(' '):
        try: winners.append(int(i))
        except: pass
    for n in li.split(': ')[1].split(' | ')[1].replace('\n','').split(' '):
        try: nums.append(int(n))
        except: pass
    cards[key] = [winners, nums]

total_pts = 0
matches=[]
for c in cards.keys():
    points = 0
    m = 0
    for j in cards[c][0]: 
        if j in cards[c][1]: 
            points = 1 if points ==0 else points*2
            m+=1
    total_pts +=points
    matches.append(m)

print('Answer to Part 1: {}'.format(total_pts))

start_cards = np.ones(len(cards.keys()), dtype=int)
for c in range(len(cards.keys())):
    factor = start_cards[c]
    for i in range(matches[c]): start_cards[c+i+1] += factor

print('Answer to Part 2: {}'.format(sum(start_cards)))