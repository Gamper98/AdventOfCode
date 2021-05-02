def readIn(text, nums):
    with open(text, 'r') as f:
        nums[1:] = [int(x) for x in f.read().rstrip('\n').split('\n')]
        
def countDifs(adapter):
    subt = list(map(lambda x: x[0] - x[1], zip(adapter[1:], adapter[:-1])))
    print(subt)
    return subt

def possibleCombinations(subt):
    combs = [1,1]
    if subt[-2] == 1 and subt[-3] == 1:
        combs.append(2)
    else:
        combs.append(1)
    for i in range(len(subt)-4, -1, -1):
        if subt[i] == 1 and subt[i+1] == 1:
            if subt[i+2] == 3:
                combs.append(sum(combs[1:3]))
                combs.pop(0)
            else:
                combs.append(sum(combs))
                combs.pop(0)
        else:            
            combs.append(combs[-1])
            combs.pop(0)
    return combs[-1]



adapter = [0]
readIn(r'2020\day10\input\input.txt', adapter)
adapter.sort()
adapter.append(adapter[-1]+3)
print(adapter)
subt = countDifs(adapter)
print('{}'.format(subt.count(1)*subt.count(2)))
print(possibleCombinations(subt))