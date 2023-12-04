import numpy as np

#with open('../inputs/test3.txt') as f:
with open('../inputs/day3.txt') as f:
    inputs=f.readlines()

def check_adj(symb):
    '''symb: which array of symbol locations to check against
    Returns:
    idx: indexes that are a number adjacent to a symbol
    adj_to: indexes of the symbol they are adjacent to'''
    idx = []
    adj_to = []
    for (i,j) in nums:
        allowed_adj = [] #indices adjacent to a number
        row = range(max([i-1,0]), min([i+2,len(inputs)]))
        col = range(max([j-1,0]), min([j+2,len(inputs[i])]))
        for r in row:
            for c in col:
                if (i,j) != (r,c): allowed_adj.append((r,c))
        #allowed_adj = np.unique(allowed_adj, axis=0)
        
        for s in symb:
            if s in allowed_adj: 
                idx.append((i,j))
                adj_to.append(s)
    return idx, adj_to

def get_numbers(ind):
    numbers =[None,]
    for k,n in ind:
        num=inputs[k][n]
        m=n-1
        while m >= 0:
            if inputs[k][m].isdigit(): num= inputs[k][m]+num
            else: m=-1
            m -= 1
        m=n+1
        
        while m < len(inputs[k]):
            if inputs[k][m].isdigit(): num=num+inputs[k][m]
            else: m=1000
            m +=1
        if numbers[-1] != int(num): numbers.append(int(num))
    return numbers

inputs = [i.replace('\n','') for i in inputs]
#find the symbols in each line
symbols = []
#find the numbers in each line
nums= []
#find gears
gears = []
for i in range(len(inputs)):
    for j in range(len(inputs[i])):
        if not inputs[i][j].isalnum() and inputs[i][j]!='.': 
            symbols.append((i,j))
            if inputs[i][j]=='*': gears.append((i,j))
        if inputs[i][j].isdigit():
            nums.append((i,j))

idx, _ = check_adj(symbols)
numbers = get_numbers(idx)

print('Answer to part 1: {}'.format(sum(numbers[1:])))
    
idx2, ad = check_adj(gears)
a, count = np.unique(ad, return_counts=True, axis=0)
gear=0
for k in range(len(count)):
    if count[k] > 1: 
        idx3, _ = check_adj([tuple(a[k])])
        numbers2 = get_numbers(idx3)
        if len(numbers2) > 2:
            gear += numbers2[1]*numbers2[2]

print('Answer to part 2: {}'.format(gear))