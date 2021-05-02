from copy import deepcopy

def readIn(text, seats):
    with open(text, 'r') as f:
        i = 0
        for line in f.readlines():
            seats.append([x for x in line.rstrip('\n')])
            i += 1

def checkSeatValue(nextStage, seats, starti, startj, endi, endj, i, j, maxW, maxH):
    posToCheck = [(x, y) for x in range(starti, endi+1) for y in range(startj, endj+1)]
    countOccupied = 0
    for (x, y) in posToCheck:
        if not(x == i and y == j):
            istep = x - i
            jstep = y - j
            xx = x
            yy = y
            while True:
                if xx == maxW+1 or yy == maxH+1 or xx == -1 or yy == -1:
                    break
                elif seats[yy][xx] == 'L':
                    break
                elif seats[yy][xx] == '.':
                    xx += istep
                    yy += jstep
                    continue
                elif seats[yy][xx] == '#':
                    countOccupied += 1
                    break
    if seats[j][i] == 'L' and countOccupied == 0:
        nextStage[j][i] = '#'
    elif seats[j][i] == '#' and countOccupied >= 5:
        nextStage[j][i] = 'L'

def printSeats(seats):
    for x in range(len(seats)):
        print(seats[x])
    print()

def checkCorner(nextstage, seats, i, j, maxW, maxH):
    if i == 0 and j == 0:
        checkSeatValue(nextstage, seats, i, j, i+1, j+1, i, j, maxW, maxH)
    elif i == 0 and j == maxH:
        checkSeatValue(nextstage, seats, i, j-1, i+1, j, i, j, maxW, maxH)
    elif i == maxW and j == 0:
        checkSeatValue(nextstage, seats, i-1, j, i, j+1, i, j, maxW, maxH)
    elif i == maxW and j == maxH:
        checkSeatValue(nextstage, seats, i-1, j-1, i, j, i, j, maxW, maxH)

def checkTopBottom(nextstage, seats, i, j, maxW, maxH):
    if i == 0:
        checkSeatValue(nextstage, seats, i, j-1, i+1, j+1, i, j, maxW, maxH)
    else:        
        checkSeatValue(nextstage, seats, i-1, j-1, i, j+1, i, j, maxW, maxH)

def checkLeftRight(nextstage, seats, i, j, maxW, maxH):
    if j == 0:
        checkSeatValue(nextstage, seats, i-1, j, i+1, j+1, i, j, maxW, maxH)
    else:        
        checkSeatValue(nextstage, seats, i-1, j-1, i+1, j, i, j, maxW, maxH)

def checkSeatPos(nextstage, seats, i, j, maxW, maxH):
    if i % maxW== 0 and j % maxH == 0:
        checkCorner(nextstage, seats, i, j, maxW, maxH)
    elif i % maxW == 0 and j % maxH != 0:
        checkTopBottom(nextstage, seats, i, j, maxW, maxH)
    elif i % maxW != 0 and j % maxH == 0:
        checkLeftRight(nextstage, seats, i, j, maxW, maxH)
    else:
        checkSeatValue(nextstage, seats, i-1, j-1, i+1, j+1, i, j, maxW, maxH)

def changeState(seats):
    maxW = len(seats[0]) - 1
    maxH = len(seats) - 1
    nextStage = deepcopy(seats)
    while True:
        for j in range(len(nextStage)):
            for i in range(len(nextStage[0])):
                if nextStage[j][i] == '.':
                    continue
                checkSeatPos(nextStage, seats, i , j, maxW, maxH)
        #printSeats(nextStage)
        if nextStage == seats:
            break
        seats = deepcopy(nextStage)
    occupied = sum([x.count('#') for x in seats])
    print(occupied)
                


seats = []
readIn(r'2020\day11\input\input.txt',seats)
#printSeats(seats)
changeState(seats)