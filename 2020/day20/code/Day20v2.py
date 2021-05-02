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


def checkSide(edge, edgeNum, tiles, currentTileNum, imageFramesPos, x, y, ToCheck, checked):
    for num in list(tiles.keys()):
        if num == currentTileNum: continue
        if (tiles[currentTileNum][edge][edgeNum] == tiles[currentTileNum][edge][(edgeNum + 1)%2] or
            tiles[currentTileNum][edge][edgeNum] == tiles[currentTileNum][edge][edgeNum] or
            tiles[currentTileNum][edge][edgeNum] == list(reversed(tiles[currentTileNum][edge][(edgeNum + 1)%2])) or
            tiles[currentTileNum][edge][edgeNum] == list(reversed(tiles[currentTileNum][edge][edgeNum]))):
            if num not in checked:
                imageFramesPos[num].append((x, y))
                ToCheck.append(num)

def attempt2(tiles, imageFramesPos):
    ToCheck = [list(tiles.keys())[0]]
    checked = []
    imageFramesPos[ToCheck[0]].append((0,0))
    x, y = 0, 0
    while len(ToCheck):
        num = ToCheck.pop(0)
        if num in checked: continue
        x,y = imageFramesPos[num][0]
        checkSide('tbEdge', 0, tiles, num, imageFramesPos, x , y-1, ToCheck, checked)
        checkSide('tbEdge', 1, tiles, num, imageFramesPos, x , y+1, ToCheck, checked)
        checkSide('lrEdge', 0, tiles, num, imageFramesPos, x-1 , y, ToCheck, checked)
        checkSide('lrEdge', 1, tiles, num, imageFramesPos, x+1 , y, ToCheck, checked)
        checked.append(num)

def printImage(tiles, imageFramesPos):
    for item in imageFramesPos.items():
        print(item)


tiles = defaultdict(lambda: {'tbEdge': [], 'lrEdge':[]})
pairs = []
imageFramesPos = defaultdict(lambda: [])
readIn(r'2020\day20\test\input.txt', tiles)
attempt2(tiles, imageFramesPos)
printImage(tiles, imageFramesPos)
