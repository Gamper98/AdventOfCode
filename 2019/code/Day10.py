from math import degrees, gcd, atan2
from copy import deepcopy
def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
 
    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = dx / 2.0
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    '''for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        if dx == 0 or dy == 0:
            points.append(coord)
            continue
        error -= float(abs(dy))
        if error < 0:
            if abs(abs(error) - abs(round(error))) < 0.1:
                points.append(coord)
            y += ystep
            error += float(dx)
    '''
    for x in range(x1, x2 + 1, int(dx/gcd(dx, dy))):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        y += int(dy/gcd(dx,dy))

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points

asteroids = []
maxPos = 0
angleToX = []
asteroidDestroyedInOrder = []

def asteroidsPos():
    with open(r"2019\input\input10.txt", "r") as f:
        lines = [x for x in f.readlines()]
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == '#':
                    asteroids.append((x,y))

def angleOf(center, asteroid):
    center_x, center_y = center
    asteroid_x, asteroid_y = asteroid
    delta_x = asteroid_x - center_x
    delta_y = center_y - asteroid_y
    return atan2(-delta_y, delta_x)

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def destroyAsteroid(startAngle, EndAngle, center):
    partialAngles = []
    global angleToX, asteroids, asteroidDestroyedInOrder
    for angle in angleToX:
        #print(angle)
        if angle[0] >= startAngle and angle[0] < EndAngle:
            partialAngles.append(deepcopy(angle))
        elif angle[0] >= startAngle and angle[0] <= EndAngle and EndAngle == 360:
            partialAngles.append(deepcopy(angle))
    partialAsteroidsDestroyed = []
    anglesToRemove = []
    partialAngles.sort(key=lambda x:x[0])
    for angle in partialAngles:
        maybeCollide = get_line(center, asteroids[angle[1]])
        isCollide = False
        for i in range(1, len(maybeCollide)-1):
            if maybeCollide[i] in asteroids:
                isCollide = True
        if not isCollide:
            partialAsteroidsDestroyed.append(asteroids[angle[1]])
            anglesToRemove.append(angle)
    asteroidDestroyedInOrder += deepcopy(partialAsteroidsDestroyed)
    asteroids = Diff(asteroids, partialAsteroidsDestroyed)
      
def taskA():
    global maxPos
    asteroidsPos()
    asteroidInView = []
    maxPos = 0
    for aster1 in asteroids:
        asteroidInView.append(0)
        for aster2 in asteroids:
            if aster1 != aster2:
                lineOfSight = True
                maybeCollide = get_line(aster1, aster2)                
                for x in range(1, len(maybeCollide)-1):
                    if maybeCollide[x] in asteroids:
                        lineOfSight = False
                if lineOfSight:
                    asteroidInView[-1] += 1
                #print("asteroid 1: {}\nasteroid 2: {} \n LineOfSight: {} \n PointsInLine: {}\n".format(aster1, aster2, lineOfSight, maybeCollide))
        if asteroidInView[maxPos] < asteroidInView[-1]:
            maxPos = len(asteroidInView) - 1

    #print(asteroids[maxPos])
    print(asteroidInView[maxPos])

def taskB():
    global maxPos, asteroids, angleToX
    center = asteroids[maxPos]
    asteroids.remove(center)
    #print(center)
    k = 1
    while len(asteroids):
        i = 0
        angleToX = []
        for aster in asteroids:
            angleToX.append((degrees(angleOf(center,aster))+180, i))
            i += 1
        #print(angleToX)
        destroyAsteroid(0 + k*90, 90 + k*90, center)
        k = (k + 1)%4
    '''    
    for x in range(len(asteroidDestroyedInOrder)):
        print("{}. asteroid:{}".format(x,asteroidDestroyedInOrder[x]))
    '''
    print(asteroidDestroyedInOrder[199][0] * 100 + asteroidDestroyedInOrder[199][1])

taskA()
taskB()