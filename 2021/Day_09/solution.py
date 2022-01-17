import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        heights = [[int(digit) for digit in row] for row in f.read().rstrip('\n').split('\n')]
        return np.array(heights, dtype=np.int8)

def find_lowest_points(heights):
    is_lowest = np.full_like(heights, fill_value=True, dtype=np.bool8)
    is_lowest[1:] = is_lowest[1:] & (heights[1:] - heights[:-1] < 0) 
    is_lowest[:-1] = is_lowest[:-1] & (heights[:-1] - heights[1:] < 0) 
    is_lowest[:,1:] = is_lowest[:,1:] & (heights[:,1:] - heights[:,:-1] < 0) 
    is_lowest[:,:-1] = is_lowest[:,:-1] & (heights[:,:-1] - heights[:,1:] < 0)
    return is_lowest

def solution_A(heights):
    lows = heights[find_lowest_points(heights)]
    return np.sum(lows+1)

def flood_fill(heights, x_s, y_s):
    seen = set()
    is_basin = [(x_s, y_s)]
    while is_basin:
        x, y = is_basin.pop()
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < heights.shape[0] and  0 <= y2 < heights.shape[1] and \
                heights[x2,y2] != 9 and (x2,y2) not in seen:
                is_basin.append((x2,y2))
                seen.add((x2,y2))
    return len(seen)
    
def solution_B(heights):
    is_lowest = find_lowest_points(heights)
    heights_copy = heights.copy()
    heights_copy[~is_lowest] = -1
    coords = np.argwhere(heights_copy != -1)
    basin_sizes = np.zeros(coords.shape[0], dtype=np.int32)
    for i, (x_s, y_s) in enumerate(coords):
        basin_sizes[i] += flood_fill(heights, x_s, y_s)
    basin_sizes = np.sort(basin_sizes)[::-1]
    return np.product(basin_sizes[:3])

def main():
    heights = read(os.path.join(ROOT_DIR, '2021\Day_09\input', 'input.txt'))
    sol_A = solution_A(heights)
    sol_B = solution_B(heights)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()