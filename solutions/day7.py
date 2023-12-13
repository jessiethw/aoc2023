import numpy as np
import re

#with open('../inputs/test7.txt') as f:
with open('../inputs/day7.txt') as f:
    inp = f.readlines()

hands = np.asarray([line[:5] for line in inp])
bids = np.asarray([int(line[6:].rstrip('\n')) for line in inp])

def find_replace(string, joker=False):
    if joker: v = 'P'
    else: v='D'

    pairs = [('K','B'), ('Q','C'), ('J', v), ('T','E'),
             ('9','F'), ('8','G'), ('7','H'), ('6','I'),
             ('5','L'), ('4','M'), ('3','N'), ('2','O'),
            ]
    for i,j in pairs:
        string = string.replace(i, j)
    
    return string

def get_rank(hands, with_joker=False):
    # add types to each hand:
    # 6 (5 of a kind), 5 (4 of a kind), 4 (full house)
    # 3 (of a kind), 2 (2 pair), 1 (1 pair), 0 (high card)
    types, new_hands = [], []
    for hand in hands:
        new_hands.append(find_replace(hand, joker=with_joker))

        matcher= re.compile(r'(\w)\1*')
        s = ''
        s= s.join(sorted(hand))
        mmm = [match.group() for match in matcher.finditer(s)]

        if with_joker: 
            check = ['J', 'JJ', 'JJJ', 'JJJJ']
            for c in check:
                if c in mmm: 
                    mmm.remove(c)
                    legs = np.asarray([len(m) for m in mmm])
                    maxidx = np.where(legs==max(legs))[0][0]
                    mmm[maxidx] += c

        if len(mmm) == 1: types.append(6)
        elif len(mmm) == 2: 
            if len(mmm[0])==1 or len(mmm[0])==4: types.append(5)
            else: types.append(4)
        elif len(mmm) == 3:
            if len(mmm[0])==2 or len(mmm[1])==2: types.append(2)
            else: types.append(3)
        elif len(mmm) == 5: types.append(0)
        elif len(mmm) == 4: types.append(1)
        else: print('Invalid hand type found!')

    new_hands = np.asarray(new_hands)
    ranks = np.zeros(len(new_hands), dtype=int)
    rank=1
    for i in range(7):
        msk = np.asarray(types)==i
        idx = np.where(msk)[0][np.argsort(new_hands[msk])]
        
        for j in idx[::-1]: 
            ranks[j] = rank
            rank+=1
    
    return ranks

ranks = get_rank(hands, with_joker=False)
print('Answer to part 1: {}'.format(sum(ranks*bids)))

ranks = get_rank(hands, with_joker=True)
print('Answer to part 2: {}'.format(sum(ranks*bids)))