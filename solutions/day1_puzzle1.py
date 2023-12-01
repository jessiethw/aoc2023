'''Day 1 Puzzle 1 solution'''

with open('../inputs/day1.txt') as f:
    calib=f.readlines()

nums = [1,2,3,4,5,6,7,8,9]
strs = ['one','two','three','four','five','six','seven','eight','nine']

def get_calib(calib, verbose = False):
    values = []
    for item in calib:
        num = ''
        if verbose: print(item)
        for digit in item:
            try:
                if int(digit) in nums: num+=digit
            except: 
                continue
        if verbose: print(int(num[0]+num[-1]))
        values.append(int(num[0]+num[-1]))
    return values

values = get_calib(calib)
print('Part 1 Solution: {}'.format(sum(values)))

for i in range(len(calib)):
    item = calib[i]
    for s in range(len(strs)):
        item = item.replace(strs[s],strs[s]+str(nums[s])+strs[s])
    calib[i] = item

values2 = get_calib(calib)
print('Part 2 Solution: {}'.format(sum(values2)))