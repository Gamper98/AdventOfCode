import itertools
import re
from copy import deepcopy
from itertools import combinations
from math import gcd
zeroState = []
moonsCoords = []
moonsVelocity = []

def readIn():
    with open(r"2019\input\input12.txt", "r") as file_in:
        for line in file_in.readlines():
            moonsCoords.append([int(s) for s in re.findall(r'-?\d+\d*', line)])
            moonsVelocity.append([0,0,0])

def velCalc():
    for moon1 in range(4):
        for moon2 in range(4):
            if moon1 != moon2:
                for i in range(3):
                    if moonsCoords[moon1][i] < moonsCoords[moon2][i]:
                        moonsVelocity[moon1][i] += 1
                    elif moonsCoords[moon1][i] > moonsCoords[moon2][i]:
                        moonsVelocity[moon1][i] -= 1

def changePos(moon):
    difference = []
    zip_object = zip(moonsCoords[moon], moonsVelocity[moon])
    for list1_i, list2_i in zip_object:
        difference.append(list1_i+list2_i)
    moonsCoords[moon] = difference

def stepMoon():
    velCalc()
    for moon in range(4):
        changePos(moon)
    
def taskA(steps):
    readIn()
    for i in range(steps):
        stepMoon()
    total = 0
    for moon in range(4):
        pot, kin = 0, 0
        for i in range(3):
            pot += abs(moonsCoords[moon][i])
            kin += abs(moonsVelocity[moon][i])
        total += pot * kin
    print(total)

def x(combination, i, zeroState, moonsCoords, moonsVelocity, periods):
    steps = 0
    while True:

        for x1, x2 in combination:
            if moonsCoords[x1][i] < moonsCoords[x2][i]:
                moonsVelocity[x1][i] += 1
                moonsVelocity[x2][i] -= 1
            elif moonsCoords[x1][i] > moonsCoords[x2][i]:
                moonsVelocity[x1][i] -= 1
                moonsVelocity[x2][i] += 1
        
        for k in range(4):
            moonsCoords[k][i] += moonsVelocity[k][i]
        

        steps += 1
        #print(moonsCoords)
        #print(moonsVelocity)

        isHalfway = True
        for k in range(4):
            if moonsVelocity[k][i] != zeroState[k][i]:
                isHalfway = False
                break
        
        if isHalfway:
            periods[i] = steps
            break

def lcm(a, b):
    return int(abs(a*b) / gcd(a, b))

def taskB():
    readIn()
    combination = list(combinations([0,1,2,3], 2))
    zeroState = deepcopy(moonsVelocity)
    periods = [0,0,0]

    x(combination, 0, zeroState, moonsCoords, moonsVelocity, periods)
    x(combination, 1, zeroState, moonsCoords, moonsVelocity, periods)
    x(combination, 2, zeroState, moonsCoords, moonsVelocity, periods)

    print(periods)
    answer = lcm(periods[0], periods[1])
    answer = lcm(answer, periods[2])
    print(answer*2)

#taskA(1000)
taskB()