import numpy
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import euclidean

def upV(y):
    return (0, y)

def downV(y):
    return (0, -y)

def leftV(x):
    return (-x, 0)

def rightV(x):
    return (x, 0)

option = { 'U': upV, 'D': downV , 'L': leftV, 'R': rightV}

def vectorArith(wirePoints, value, direction):
    wirePoints.append(tuple(numpy.add(wirePoints[-1], option[direction](value))))

def isIntersect(p,q,r,s):
    rs = int(numpy.cross(r, s))
    pq = tuple(numpy.subtract(q, p))
    if rs:
        t = int(numpy.cross(pq, s))/rs
        u = int(numpy.cross(pq, r))/rs
        if t >= 0 and t <= 1 and u >= 0 and u <= 1:
            return tuple([int(x) for x in tuple(numpy.add(p, tuple(numpy.multiply(t, r))))])
    return 0

def intersections(intersects, wires, wirePoints):
    i, j = 0, 0
    for vecA in wires[0]:
        for vecB in wires[1]:
            interpoints = isIntersect(wirePoints[0][i], wirePoints[1][j], option[vecA[0]](int(vecA[1:])), option[vecB[0]](int(vecB[1:])))
            if interpoints:
                intersects.append(interpoints)
            j += 1
        i += 1
        j = 0

def lowManhDis(intersects):
    return min(cityblock(intersect, (0,0)) for intersect in intersects)

wires, wirePoints, intersects = [], [[(0,0)], [(0,0)]], []
def taskA():
    with open(r"2019\input\input3.txt", "r") as f:
        for line in f:
            wires.append(line.rstrip('\n').split(','))
    i = 0
    for wire in wires:
        for point in wire:
            vectorArith(wirePoints[i], int(point[1:]), point[0])
        i += 1

    intersections(intersects,wires,wirePoints)
    if (0,0) in intersects:
        intersects.remove((0,0))
    print(lowManhDis(intersects))

def isBetween(a, b, c):
    crossproduct = int(numpy.cross(numpy.subtract(b,a),numpy.subtract(c,a)))
    if abs(crossproduct) != 0:
        return False
    dotproduct = int(numpy.dot(numpy.subtract(b,a),numpy.subtract(c,a)))
    if dotproduct < 0:
        return False
    squaredlengthba = int(pow(euclidean(a,b), 2))
    if dotproduct > squaredlengthba:
        return False
    return True

def lenghtToIntersection(wirePoints, intersect, steps):
    posBefore = (0, 0)
    for (x3, y3) in wirePoints:
        if isBetween(posBefore, (x3,y3), intersect):
            steps[-1] += euclidean(posBefore, intersect)
            return
        else:
            steps[-1] += euclidean(posBefore, (x3, y3))
        posBefore = (x3, y3)
        
def shortetsPathToIntersection():
    steps = [] 
    wirePoints[0].remove(((0,0)))
    wirePoints[1].remove(((0,0)))
    for (x2, y2) in intersects:
        steps.append(0)
        lenghtToIntersection(wirePoints[0], (x2, y2), steps)        
        lenghtToIntersection(wirePoints[1], (x2, y2), steps)
    return min(steps)

def taskB():
    print(shortetsPathToIntersection())

taskA()
taskB()



