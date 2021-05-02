import re
import math

def readIn(text, timestamp):
    with open(text, 'r') as f:
        timestamp.append(int(f.readline()))
        for line in f.readlines():
            x = re.findall(r'(\d+)([,x]*)',line.rstrip('\n'))
            timestamp.append([(int(item[0]), item[1].count('x')+1) for item in x])

def ExtendedEuclideanAlgorithmPartial(a, b):

    x1 = y2 = 1
    y1 = x2 = 0
    while b != 0:
        qi = a // b
        a, b = b, a % b
        x1, x2 = x2, x1 - qi * x2
        y1, y2 = y2, y1 - qi * y2

    return {"x": x1, "y": y1}

def calcNextArrive(timestamp):
    earliestA = []
    earliestD = timestamp[0]
    for (id, _) in timestamp[1]:
        earliest = earliestD//id * id + id - earliestD
        earliestA.append(earliest)
    i = earliestA.index(min(earliestA))
    print(earliestA[i] * timestamp[1][i][0])

def chineseReminder(timestamp):
    product = math.prod([id for (id, _) in timestamp])
    crt = {'bi':[], 'ni':[], 'xi':[]}
    bi = 0
    for (id, skip) in timestamp:
        crt['bi'].append(-bi)
        bi += skip
        crt['ni'].append(product//id)
        crt['xi'].append(ExtendedEuclideanAlgorithmPartial(id, crt['ni'][-1])['y'])
    end = sum([crt['bi'][i] * crt['ni'][i] * crt['xi'][i] for i in range(len(crt['bi']))])
    print(end % product)

timestamp = []
readIn(r'2020\day13\input\input.txt', timestamp)
calcNextArrive(timestamp)
chineseReminder(timestamp[1])