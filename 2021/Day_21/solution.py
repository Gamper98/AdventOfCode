import os
from config.definitions import ROOT_DIR
import re
import numpy as np
from functools import lru_cache

def read(text):
    with open(text, 'r') as f:
        start_pos = re.findall(r'(\d+)', f.read())
        return np.array([start_pos[1],start_pos[3]], dtype=np.int32)

def solution_A(start_pos):
    start_pos = start_pos.copy()
    scores = np.zeros(2, dtype=np.int32)
    rounds = 0
    dice = 0
    current_pos = start_pos
    while True:
        if np.max(scores) >= 1000:
            break 
        dice_1 = (dice % 100) + 1
        dice_2 = ((dice + 1) % 100) + 1
        dice_3 = ((dice + 2) % 100) + 1
        current_pos[rounds%2] = ((current_pos[rounds%2] + dice_1 + dice_2 + dice_3 - 1)% 10) + 1 
        scores[rounds%2] += current_pos[rounds%2]
        rounds += 1
        dice = dice_3
    return np.min(scores) * rounds * 3

@lru_cache(maxsize=100000)
def game_rounds(player, current_pos, scores):
    if scores[(player+1)%2] >= 21:
        asd = np.array([0,0], dtype=np.int64)
        asd[(player+1)%2] = 1
        return asd
    win = np.array([0,0], dtype=np.int64)
    dice_dict = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}
    for sum_dice, occ in dice_dict.items():
        copy_pos = list(current_pos)
        copy_scores = list(scores)
        copy_pos[player] = ((copy_pos[player] + sum_dice - 1) % 10) + 1
        copy_scores[player] += copy_pos[player]
        win += game_rounds((player+1)%2, tuple(copy_pos), tuple(copy_scores)) * occ
    return win

def solution_B(start_pos):
    return np.max(game_rounds(0, tuple(start_pos), (0,0)))

def main():
    start_pos = read(os.path.join(ROOT_DIR, '2021\Day_21\input', 'input.txt'))
    sol_A = solution_A(start_pos)
    sol_B = solution_B(start_pos)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()