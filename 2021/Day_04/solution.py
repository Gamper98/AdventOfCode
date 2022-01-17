import os
from config.definitions import ROOT_DIR
import re
import numpy as np

def read(text):
    with open(text, 'r') as f:
        draws = f.readline().rstrip('\n').split(',')
        bingo_boards = re.findall(r'(\d+)', f.read())
        bingo_boards = np.array(bingo_boards, dtype=np.int8)
        bingo_boards += 1
        bingo_boards = bingo_boards.reshape(-1,5,5)
        return (np.array(draws, dtype=np.int8), bingo_boards)

def check_boards(bingo_boards):
    column_check = np.count_nonzero(np.count_nonzero(bingo_boards, axis=1), axis=1)
    row_check = np.count_nonzero(np.count_nonzero(bingo_boards, axis=2), axis=1)
    return np.argwhere(column_check + row_check != 10)

def play_bingo(draws, bingo_boards, condition_func):
    idx_save = np.array([], dtype=np.int8)
    for num in draws:
        bingo_boards[bingo_boards == num+1] = 0
        idx = check_boards(bingo_boards).flatten()
        if condition_func(idx, bingo_boards.shape[0]):
            return (np.setdiff1d(idx, idx_save), num)
        idx_save = idx

def board_value(idx, num, bingo_boards):
    return (np.sum(bingo_boards[idx])-np.count_nonzero(bingo_boards[idx])) * num

def solution_A(draws, bingo_boards):
    idx, num = play_bingo(draws, bingo_boards, lambda n,m: n.size > 0)
    return board_value(idx, num, bingo_boards)

def solution_B(draws, bingo_boards):
    idx, num = play_bingo(draws, bingo_boards, lambda n,m: n.size == m)
    return board_value(idx, num, bingo_boards)

def main():
    draws, bingo_boards = read(os.path.join(ROOT_DIR, '2021\Day_04\input', 'input.txt'))
    sol_A = solution_A(draws, bingo_boards)
    sol_B = solution_B(draws, bingo_boards)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()