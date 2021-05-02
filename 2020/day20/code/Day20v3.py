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
            tiles[TileNum] = np.array([rows_np[0], rows_np[:,-1], rows_np[-1], rows_np[:,0]])

def check_Sides(num_s, num_r, tiles):
    for side_s in tiles[num_s]:
        for side_r in tiles[num_r]:
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
            print(num, i)
            corners *= num
    print(corners)


tiles = defaultdict(lambda: np.array)
pairs = []
read_In(r'..\input\input.txt', tiles)
find_Pairs(tiles, pairs)
calc_Num__Occurance(pairs, list(tiles.keys()))


# %%
