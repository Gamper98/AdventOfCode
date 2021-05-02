#%%
import re
from collections import defaultdict
import numpy as np


def read_In(text, tiles):
    with open(text, 'r') as f:
        rawTiles = f.read().rstrip('\n').split('\n\n')
        for tile in rawTiles:
            rows = tile.rstrip('\n').split('\n')
            TileNum = int(re.search(r'\d+', rows[0]).group())
            rows_np = np.array([list(x) for x in rows[1:]], dtype=str)
            to_append = [rows_np[0], rows_np[:,-1], rows_np[-1], rows_np[:,0], rows_np[1:-1,1:-1]]
            [tiles[TileNum].append(x) for x in to_append]

def check_Sides(num_s, num_r, tiles):
    for side_s in tiles[num_s][:-1]:
        for side_r in tiles[num_r][:-1]:
            if (np.all(side_s == side_r) or
                np.all(side_s == side_r[::-1])
                ):
                return True
    return False

def find_Pairs(tiles, pairs):
    nums = list(tiles.keys())
    for ns_i, num_static in enumerate(nums):
        for num_rotated in nums[ns_i+1:]:
            if check_Sides(num_static,num_rotated, tiles):
                pairs.append((num_static, num_rotated))

def calc_Num__Occurance(pairs, nums):
    corners = 1
    for num in nums:
        i = 0
        for x in pairs:
            if num in x:
                i+=1
        if i == 2: 
            #print(num, i)
            corners *= num
    print(corners)


##1. Part
tiles = defaultdict(lambda: [])
pairs = []
read_In(r'..\test\input.txt', tiles)
find_Pairs(tiles, pairs)
calc_Num__Occurance(pairs, list(tiles.keys()))
## 2. Part
tiles_pos = defaultdict(lambda: tuple)

def rotate_Tile(tiles, angle):
    return
def flip_Tile(tileNum, tiles, axis):
    return


def find_Tile_Positions(tiles, tiles_pos, pairs):
    pos = [0, 0]
    tiles_pos[pairs[0][0]] = pos
    q = [pairs[0][0]]
    while len(q) != 0:
        num = q.pop(0)
        for pair in pairs:
            if (pair[1] in tiles_pos.keys() or 
                pair[0] != num): continue
            pos = tiles_pos[pair[0]]
            for ce, ci in enumerate(tiles[pair[0]][:-1]):
                for oe, oi in enumerate(tiles[pair[1]][:-1]):
                    if ce == oe: 
                        rotate_Tile(tiles[pair[1]], oi*90)
                        tile
                    elif ce == oe[::-1]:
                        flip_Tile((tiles[pair[1]], oi))
                        flip_Tile((tiles[pair[1]], oi))
        


# %%
