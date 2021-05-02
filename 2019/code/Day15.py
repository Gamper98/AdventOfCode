from os import read, remove
from time import sleep

def paramdecoder(i, relBase, intcode):
    c, b, a = int(intcode[i]/100)%10, int(intcode[i]/1000)%10, int(intcode[i]/10000)
    param1, param2, param3 = 0, 0, 0
    if c == 1:
        param1 = i+1
    elif c == 2:
        param1 = relBase+intcode[i+1]
    elif c == 0:
        param1 = intcode[i+1]
    if b == 1:
        param2 = i+2
    elif b == 2:
        param2 = relBase+intcode[i+2]
    elif b == 0:
        param2 = intcode[i+2]
    if a == 1:
        param3 = i+3
    elif a == 2:
        param3 = relBase+intcode[i+3]
    elif a == 0:
        param3 = intcode[i+3]
    return (param1, param2, param3)

def addF(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    intcode[params[2]] = intcode[params[0]] + intcode[params[1]]
    return i+4

def multF(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    intcode[params[2]] = intcode[params[0]] * intcode[params[1]]
    return i+4

def inputC(input, i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    intcode[params[0]] = input
    return i+2

def outputC(result, i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    result.append(intcode[params[0]])
    return i+2

def jumpifTrue(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    if intcode[params[0]]:
        return intcode[params[1]]
    return i+3

def jumpifFalse(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    if not intcode[params[0]]:
        return intcode[params[1]]
    return i+3

def lessThan(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    if intcode[params[0]] < intcode[params[1]]:
        intcode[params[2]] = 1
    else:
        intcode[params[2]] = 0
    return i+4

def equals(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    if intcode[params[0]] == intcode[params[1]]:
        intcode[params[2]] = 1
    else:
        intcode[params[2]] = 0
    return i+4

def relativeBase(i, relBase, intcode):
    params = paramdecoder(i, relBase, intcode)
    relBase += intcode[params[0]]
    return i+2, relBase

opcode = {1: addF, 2: multF, 3: inputC, 4: outputC, 5: jumpifTrue, 6: jumpifFalse, 7: lessThan, 8: equals, 9:relativeBase}
relBase = 0
i = 0
def subTask(result, intcode, input):
    global relBase, i
    while(intcode[i] != 99):
        if intcode[i]%100 == 3:
            if not len(input):
                break
            i = opcode[3](input.pop(), i, relBase, intcode)
        elif intcode[i]%100 == 4:
            i = opcode[4](result, i, relBase, intcode)
            continue
        elif intcode[i]%100 == 9:
            i, relBase = opcode[9](i, relBase, intcode)
            continue
        i = opcode[intcode[i]%100](i, relBase, intcode)

def readIn():
    intcode = []
    with open(r"2019\input\input15.txt", "r") as f:
        intcode = [ int(x) for x in f.read().rstrip('\n').split(',')]
    return intcode

compass = {1: 1, 2: 4, 3: 2, 4: 3}

def taskA():
    intcode = readIn()
    for i in range(len(intcode)):
        intcode.append(0)
    movedFrom = []
    facing = 1 # 1 = fel, 2 = le, 3 = jobb, 4 = bal
    input = [compass[facing]]
    result = []
    iter = 0
    while True:
        subTask(result, intcode, input)
        #print(facing, result, movedFrom)
        #if not iter % 5:
        #   print('iter: {}'.format(iter))
        if result[0] == 0:    
            facing = (facing) % 4 + 1
            input.append(compass[facing])
            if len(movedFrom) and facing == movedFrom[-1]:
                facing = (movedFrom.pop() + 1) % 4 + 1
        elif result[0] == 1:
            movedFrom.append((facing+1)%4+1)
            facing = (facing+2)%4+1
            input.append(compass[facing])
        elif result[0] == 2:
            break
        result = []
        iter += 1
taskA() 