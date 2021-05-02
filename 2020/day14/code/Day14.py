import re

def readIn(text, maskAndValues):
    with open(text, 'r') as f:
        for line in f.readlines():
            if line.split(' ')[0] == 'mask':
                maskAndValues.append(re.findall(r'= (\w+)',line)[0])
            else:
                mem = re.findall(r'\[(\d+)\] = (\d+)',line)[0]
                maskAndValues.append((int(mem[0]), int(mem[1])))

def bitmaskSystem(mv):
    mask = ''
    memoryAddresses = {}
    for item in mv:
        if len(item) == 2:
            x = bin(item[1]).replace('0b','')
            number = 0
            for i in range(-1, -len(mask)-1, -1):
                if -len(x) <= i and mask[i] == 'X':
                    number += 2**abs(i+1) * int(x[i])
                elif mask[i] != 'X':
                    number += 2**abs(i+1) * int(mask[i])
            memoryAddresses[item[0]] = number
        else:
            mask = item
    print(sum(memoryAddresses.values()))

def bitmaskSystemV2(mv):
    mask = ''
    memoryAddresses = {}
    for item in mv:
        if len(item) == 2:
            x = bin(item[0]).replace('0b','')
            number = [0]            
            for i in range(-1, -len(mask)-1, -1):                
                if -len(x) <= i and mask[i] == '0':
                    number = [num + 2**abs(i+1) * int(x[i]) for num in number]
                elif mask[i] == '1':
                    number = [num + 2**abs(i+1) for num in number]
                elif mask[i] == 'X':
                    count = len(number)
                    number[count:] = [num + 2**abs(i+1) for num in number.copy()]
            for num in number:
                memoryAddresses[num] = item[1]
        else:
            mask = item
    print(sum(memoryAddresses.values()))


maskAndValues = []
readIn(r'2020\day14\input\input.txt', maskAndValues)
#bitmaskSystem(maskAndValues)
bitmaskSystemV2(maskAndValues)