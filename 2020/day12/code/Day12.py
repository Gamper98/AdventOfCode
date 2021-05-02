from copy import deepcopy
import re
import math

def readIn(text, moves):
    with open(text, 'r') as f:
        i = 0
        for line in f.readlines():
            move = re.findall(r'(\w)(\d+)', line.rstrip('\n'))[0]
            moves.append((move[0], int(move[1])))

def north(pos, num):
    pos[1] -= num

def east(pos, num):
    pos[0] += num

def south(pos, num):
    pos[1] += num

def west(pos, num):
    pos[0] -= num

dirChar = {'N': north , 'E': east, 'S': south, 'W': west}
dirNum = {0: 'N' , 1: 'E', 2: 'S', 3: 'W'}

def moveShip1(moves):
    facing = 1
    pos = [0,0]
    for (code, num) in moves:
        if code == 'R':
            facing = (facing + num // 90) % 4
        elif code == 'L':            
            facing = (facing - num // 90) % 4
        elif code == 'F':
            dirChar[dirNum[facing]](pos, num)
        else:
            dirChar[code](pos, num)
    print(abs(pos[0]) + abs(pos[1]))

def calcRotation(waypoint, num):
    tmp = [0,0]
    tmp[0] = waypoint[0] * int(math.cos(math.radians(num))) - waypoint[1] * int(math.sin(math.radians(num)))
    tmp[1] = waypoint[1] * int(math.cos(math.radians(num))) + waypoint[0] * int(math.sin(math.radians(num)))
    waypoint[:] = tmp


def moveShip2(moves, waypoint):
    pos = [0,0]
    for (code, num) in moves:
        if code == 'R':
            calcRotation(waypoint, num)
        elif code == 'L': 
            calcRotation(waypoint, -num)
        elif code == 'F':
            pos[0] += num * waypoint[0]
            pos[1] += num * waypoint[1]
        else:
            dirChar[code](waypoint, num)
    print(pos)
    print(abs(pos[0]) + abs(pos[1]))

moves = []
readIn(r'2020\day12\input\input.txt', moves)
moveShip1(moves)
moveShip2(moves, [10, -1])