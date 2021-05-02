import queue

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
    print(relBase,i,len(intcode))
    while(intcode[i] != 99):
        if intcode[i]%100 == 3:
            if(input.empty()):
                break
            i = opcode[3](input.get(), i, relBase, intcode)
        elif intcode[i]%100 == 4:
            i = opcode[4](result, i, relBase, intcode)
            continue
        elif intcode[i]%100 == 9:
            i, relBase = opcode[9](i, relBase, intcode)
            continue
        i = opcode[intcode[i]%100](i, relBase, intcode)

def readIn():
    intcode = []
    with open(r"2019\input\input13.txt", "r") as f:
        intcode = [ int(x) for x in f.read().rstrip('\n').split(',')]
    return intcode
    
def taskA():
    intcode = []
    result = []
    blocksSum = 0
    readIn(intcode)
    subTask(result, intcode)
    for i in range(0, len(result)-2, 3):
        if(result[i+2] == 2):
            blocksSum += 1
    print(blocksSum)
    
def gameBoard(result, gameboardTable):
    row = 0
    tmp = []
    ballx = 0
    dashx = 0
    for i in range(0 ,len(result)-2, 3):
        if result[i+1] != row:
            gameboardTable.append(tmp.copy())
            tmp = []
            row += 1
        if result [i+2] == 0:
            tmp.append(" ")
        elif result [i+2] == 1:
            tmp.append("#")
        elif result [i+2] == 2:
            tmp.append("@")
        elif result [i+2] == 3:
            tmp.append("=")
            dashx = result[i]
        else:
            tmp.append("o")
            ballx = result[i]
    return ballx, dashx

def simulateInput(input, ballx, dashx):
    if ballx == dashx:
        input.put(0)
    elif ballx < dashx:
        input.put(-1)
    else:
        input.put(1)

def taskB():
    intcode = readIn()    
    for k in range(len(intcode)):
        intcode.append(0)
    result = []
    gameBoardTable = []
    point = 0
    ballx = 0
    dashx = 0
    inputQueue = queue.Queue()
    intcode[0] = 2
    subTask(result, intcode, inputQueue)
    ballx, dashx = gameBoard(result, gameBoardTable)
    sumOfBlocks = sum([row.count("@") for row in gameBoardTable])
    while sumOfBlocks:
        #for row in gameBoardTable:
        #    print("".join(row))
        #while True:
        #    inp = input()
        #    if inp == "1" or inp == "0" or inp =="-1":
        #        inputQueue.put(int(inp))
        #        break
        result = []
        simulateInput(inputQueue, ballx, dashx)
        subTask(result, intcode, inputQueue)
        print(result)
        print(ballx, " ", dashx)
        for i in range(0, len(result)-2, 3):
            if result[i] == -1:
                point = result[i+2]
                continue        
            if result [i+2] == 0:
                gameBoardTable[result[i+1]][result[i]] = " "
            elif result [i+2] == 1:
                gameBoardTable[result[i+1]][result[i]] = "#"
            elif result [i+2] == 2:
                gameBoardTable[result[i+1]][result[i]] = "@"
            elif result [i+2] == 3:
                gameBoardTable[result[i+1]][result[i]] = "="
                dashx = result[i]
            else:
                gameBoardTable[result[i+1]][result[i]] = "o" 
                ballx = result[i]
        sumOfBlocks = sum([row.count("@") for row in gameBoardTable])
    print(point)

if __name__ == "__main__":
    taskA()
    taskB()