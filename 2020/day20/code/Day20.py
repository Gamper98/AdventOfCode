import re
from collections import defaultdict
from typing import DefaultDict

def readIn(text, tiles):
    with open(text, 'r') as f:
        rawTiles = f.read().rstrip('\n').split('\n\n')
        for tile in rawTiles:
            rows = tile.rstrip('\n').split('\n')
            TileNum = int(re.search(r'\d+', rows[0]).group())
            tiles[TileNum]['tbEdge'][:] = [list(rows[1]), list(rows[-1])]
            tiles[TileNum]['lrEdge'][:] = [[x[0] for x in rows[1:]],[x[-1] for x in rows[1:]]]

def checkNormal(num1, num2, pairs):
    if(tiles[num1]['tbEdge'][0] == tiles[num2]['tbEdge'][1]):
        pairs.append((num1, num2, 't b'))    
    if(tiles[num1]['tbEdge'][1] == tiles[num2]['tbEdge'][0]):
        pairs.append((num1, num2, 'b t'))    
    if(tiles[num1]['lrEdge'][0] == tiles[num2]['lrEdge'][1]):
        pairs.append((num1, num2, 'l r'))    
    if(tiles[num1]['lrEdge'][1] == tiles[num2]['lrEdge'][0]):
        pairs.append((num1, num2, 'r l'))   

def checkRotated(num1, num2, pairs):
    if(tiles[num1]['tbEdge'][0] == list(reversed(tiles[num2]['tbEdge'][0]))):
        pairs.append((num1, num2, 't tr'))    
    if(tiles[num1]['tbEdge'][1] == list(reversed(tiles[num2]['tbEdge'][1]))):
        pairs.append((num1, num2, 'b br'))    
    if(tiles[num1]['lrEdge'][0] == list(reversed(tiles[num2]['lrEdge'][0]))):
        pairs.append((num1, num2, 'l lr'))    
    if(tiles[num1]['lrEdge'][1] == list(reversed(tiles[num2]['lrEdge'][1]))):
        pairs.append((num1, num2, 'r rr'))    

def checkFlippedLR(num1, num2, pairs):
    if(tiles[num1]['tbEdge'][0] == list(reversed(tiles[num2]['tbEdge'][1]))):
        pairs.append((num1, num2, 't bfr'))    
    if(tiles[num1]['tbEdge'][1] == list(reversed(tiles[num2]['tbEdge'][0]))):
        pairs.append((num1, num2, 'b tfr'))    
    if(tiles[num1]['lrEdge'][0] == tiles[num2]['lrEdge'][0]):
        pairs.append((num1, num2, 'l lf'))    
    if(tiles[num1]['lrEdge'][1] == tiles[num2]['lrEdge'][1]):
        pairs.append((num1, num2, 'r rf'))   

def checkFlippedTB(num1, num2, pairs):
    if(tiles[num1]['tbEdge'][0] == tiles[num2]['tbEdge'][0]):
        pairs.append((num1, num2, 't tf'))    
    if(tiles[num1]['tbEdge'][1] == tiles[num2]['tbEdge'][1]):
        pairs.append((num1, num2, 'b bf'))    
    if(tiles[num1]['lrEdge'][0] == list(reversed(tiles[num2]['lrEdge'][1]))):
        pairs.append((num1, num2, 'l rfr'))    
    if(tiles[num1]['lrEdge'][1] == list(reversed(tiles[num2]['lrEdge'][0]))):
        pairs.append((num1, num2, 'r lfr'))    
              


def findPairs(tiles, pairs):
    for i, num1 in enumerate(list(tiles.keys())):
        for num2 in list(tiles.keys())[i+1:]:
            checkNormal(num1, num2, pairs)
            checkFlippedLR(num1, num2, pairs)
            checkRotated(num1, num2, pairs)
            checkFlippedTB(num1, num2, pairs)

def findTwoOccurance(pairs, nums):
    for num in nums:
        i = 0
        for pair in pairs:
            if num in pair:
                print(pair)
                i += 1
        print("{} {}".format(num, i))
        if i == 2:
            print(num)

def attempt2(tiles):
    checked = []
    imageFramesPos = {}
    i, j = 0, 0
    for num in list(tiles.keys()):
        imageFramesPos[num] = (i,j)


tiles = defaultdict(lambda: {'tbEdge': [], 'lrEdge':[]})
pairs = []
readIn(r'2020\day20\input\input.txt', tiles)
findPairs(tiles, pairs)
findTwoOccurance(set(pairs), list(tiles.keys()))
#print(pairs)
#print(list(tiles.keys()))