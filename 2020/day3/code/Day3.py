import numpy as np

def readIn(text, trees):
    with open(text, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    trees.append([j, i])
        trees.append([len(lines[-1]), len(lines)])

def toTheBottom(left, down, trees, width, height):
    pos = [0, 0]
    tree = 0
    while True:
        pos[0] = (pos[0] + left) % width
        pos[1] += down
        if pos in trees:
            tree += 1
        if pos[1] >= height:
            return tree

trees = []
readIn(r'2020\day3\input\input.txt', trees)
treesEnc = []
wh = trees.pop()
treesEnc.append(toTheBottom(3, 1, trees, wh[0], wh[1]))
treesEnc.append(toTheBottom(1, 1, trees, wh[0], wh[1]))
treesEnc.append(toTheBottom(5, 1, trees, wh[0], wh[1]))
treesEnc.append(toTheBottom(7, 1, trees, wh[0], wh[1]))
treesEnc.append(toTheBottom(1, 2, trees, wh[0], wh[1]))
print(np.prod(treesEnc))

