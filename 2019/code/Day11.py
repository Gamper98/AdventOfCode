from os import read
from types import resolve_bases
from copy import deepcopy

intcodeGlobal = []
iGlobal = 0
relBaseGlobal = 0

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

def readIn():
    global intcodeGlobal, iGlobal, relBaseGlobal
    intcodeGlobal = []
    with open(r"2019\input\input11.txt", "r") as f:
        intcodeGlobal = [ int(x) for x in f.read().rstrip('\n').split(',')]
    for k in range(len(intcodeGlobal)):
        intcodeGlobal.append(0)
    relBaseGlobal = 0
    iGlobal = 0

def subTask(input):
    global intcodeGlobal, iGlobal, relBaseGlobal
    result = []
    while(intcodeGlobal[iGlobal] != 99):
        print("{}. intocode: {}".format(iGlobal, intcodeGlobal[iGlobal]))
        if intcodeGlobal[iGlobal]%100 == 3:
            iGlobal = opcode[3](input, iGlobal, relBaseGlobal, intcodeGlobal)
            continue
        elif intcodeGlobal[iGlobal]%100 == 4:
            iGlobal = opcode[4](result, iGlobal, relBaseGlobal, intcodeGlobal)
            if len(result) == 2:
                return(result)
            continue
        elif intcodeGlobal[iGlobal]%100 == 9:
            iGlobal, relBaseGlobal = opcode[9](iGlobal, relBaseGlobal, intcodeGlobal)
            continue
        iGlobal = opcode[intcodeGlobal[iGlobal]%100](iGlobal, relBaseGlobal, intcodeGlobal)
    result = [2]
    return result

def left(robotPos):
    return (robotPos[0]-1, robotPos[1])

def up(robotPos):
    return (robotPos[0], robotPos[1]-1)

def right(robotPos):
    return (robotPos[0]+1, robotPos[1])

def down(robotPos):
    return (robotPos[0], robotPos[1]+1)

move = {0:left, 1:up, 2: right, 3:down}

def printOutToImage(shipSideGrid):
    with open(r"2019\output11.txt","w") as output:
        for line in shipSideGrid:
            output.write("".join(line) + "\n") 

def taskA(rows, cols):
    readIn()
    robotPosX, robotPosY = int(cols/2), int(rows/2)
    shipSideGrid = []
    rotation = 1
    atleastOnce = 0
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append(['.',0])
        shipSideGrid.append(deepcopy(tmp))
    while True:
        input = 0 if shipSideGrid[robotPosY][robotPosX][0] == '.' else 1
        result = subTask(input)
        if result[0] == 2:
            break
        if result[0] == 1 and shipSideGrid[robotPosY][robotPosX][1] == 0:
            shipSideGrid[robotPosY][robotPosX][1] = 1
            atleastOnce += 1
        shipSideGrid[robotPosY][robotPosX][0] = '.' if result[0] == 0 else '#'
        rotation = (rotation + 1)%4 if result[1] == 1 else (rotation - 1)%4
        robotPosX, robotPosY = move[rotation]((robotPosX, robotPosY))
    print(atleastOnce)

def taskB(rows, cols):
    readIn()
    robotPosX, robotPosY = 1, 1 #int(cols/2), int(rows/2)
    shipSideGrid = []
    rotation = 1
    for i in range(rows):
        tmp = []
        for j in range(cols):
            tmp.append('.')
        shipSideGrid.append(deepcopy(tmp))
    shipSideGrid[robotPosY][robotPosX] = '#'
    while True:
        input = 0 if shipSideGrid[robotPosY][robotPosX] == '.' else 1
        result = subTask(input)
        if result[0] == 2:
            break
        shipSideGrid[robotPosY][robotPosX] = '.' if result[0] == 0 else '#'
        rotation = (rotation + 1)%4 if result[1] == 1 else (rotation - 1)%4
        robotPosX, robotPosY = move[rotation]((robotPosX, robotPosY))
    printOutToImage(shipSideGrid)

#taskA(100,100)
taskB(7,50)