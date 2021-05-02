import itertools

def readIn(text, activeCells,dims):
    activeCells.clear()
    with open(text, 'r') as f:
        lines = f.read().rstrip('\n').split('\n')
        for rc, r in enumerate(lines):
            for cc, c in enumerate(r):
                if c == '#':
                    activeCells.add((cc,rc, *(tuple(0 for i in range(dims-2)))))

def cycles(activeCells, dims):
    cycles = 0
    activeCellsCopy = activeCells.copy()
    while cycles < 6:
        x_min, x_max = min(activeCells, key=lambda x:x[0])[0], max(activeCells, key=lambda x:x[0])[0]
        y_min, y_max = min(activeCells, key=lambda x:x[1])[1], max(activeCells, key=lambda x:x[1])[1]
        z_min, z_max = min(activeCells, key=lambda x:x[2])[2], max(activeCells, key=lambda x:x[2])[2]
        for x in range(x_min-1, x_max+2):
            for y in range(y_min-1, y_max+2):
                for z in range(z_min-1, z_max+2):
                    neigbours = set(itertools.product([x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1], [0]))
                    if (x,y,z,0) in activeCells:
                        if not (2 <= len(activeCells.intersection(neigbours))-1 <= 3):
                            activeCellsCopy.remove((x,y,z,0))
                    else:
                        if len(activeCells.intersection(neigbours)) == 3:
                            activeCellsCopy.add((x,y,z,0))
        activeCells = activeCellsCopy.copy()
        cycles+=1
    print(len(activeCells))
                    
def cycles2(activeCells, dims):
    cycles = 0
    activeCellsCopy = activeCells.copy()
    while cycles < 6:
        x_min, x_max = min(activeCells, key=lambda x:x[0])[0], max(activeCells, key=lambda x:x[0])[0]
        y_min, y_max = min(activeCells, key=lambda x:x[1])[1], max(activeCells, key=lambda x:x[1])[1]
        z_min, z_max = min(activeCells, key=lambda x:x[2])[2], max(activeCells, key=lambda x:x[2])[2]
        w_min, w_max = min(activeCells, key=lambda x:x[3])[3], max(activeCells, key=lambda x:x[3])[3]
        for x in range(x_min-1, x_max+2):
            for y in range(y_min-1, y_max+2):
                for z in range(z_min-1, z_max+2):
                    for w in range(w_min-1, z_max+2):
                        neigbours = set(itertools.product([x-1,x,x+1], [y-1,y,y+1], [z-1,z,z+1], [w-1, w, w+1]))
                        if (x,y,z,w) in activeCells:
                            if not (2 <= len(activeCells.intersection(neigbours))-1 <= 3):
                                activeCellsCopy.remove((x,y,z,w))
                        else:
                            if len(activeCells.intersection(neigbours)) == 3:
                                activeCellsCopy.add( (x,y,z,w))
        activeCells = activeCellsCopy.copy()
        cycles+=1
    print(len(activeCells))

def cyclesGeneral(activeCells, dims):
    cycle = 0
    activeCellsCopy = activeCells.copy()
    while cycle < 6:
        minmax = []
        for i in range(0, dims):
            minmax.append([x for x in range(min(activeCells, key=lambda x:x[i])[i]-1, max(activeCells, key=lambda x:x[i])[i]+2)])
        coords = set(itertools.product(*minmax))
        for item in coords:
            neigbours = set(itertools.product(*[[x-1,x,x+1] for x in item]))
            if item in activeCells:
                if not (2 <= len(activeCells.intersection(neigbours))-1 <= 3):
                    activeCellsCopy.remove(item)
            else:
                if len(activeCells.intersection(neigbours)) == 3:
                    activeCellsCopy.add(item)        
        activeCells = activeCellsCopy.copy()
        cycle += 1
    print(len(activeCells))

activeCells = set()
readIn(r'2020\day17\input\input.txt', activeCells, 3)
cyclesGeneral(activeCells, 3)
readIn(r'2020\day17\input\input.txt', activeCells, 4)
cyclesGeneral(activeCells, 4)