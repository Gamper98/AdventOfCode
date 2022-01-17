import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        h_pos = np.array(f.read().rstrip('\n').split(','), dtype=np.int64)
        return h_pos

def solution_A(h_pos):
    d_median = np.median(h_pos)
    h_pos = h_pos - d_median.astype(np.int64)
    sum_fuel = np.sum(np.absolute(h_pos))
    return sum_fuel

#Assume the ideal position is near to the mean, check to -3 to 3 from mean
def solution_B(h_pos):
    d_mean = np.rint(np.mean(h_pos)) #484.512
    d_mean_close = np.array([d_mean + i for i in range(-3,4)], dtype=np.int32)
    h_pos = h_pos[:,None]*np.ones(7, dtype=np.int32) - d_mean_close
    abs_fuel = np.absolute(h_pos)
    sum_fuel = np.sum(abs_fuel * (abs_fuel + 1) // 2, axis=0)
    return np.min(sum_fuel)

def main():
    h_pos = read(os.path.join(ROOT_DIR, '2021\Day_07\input', 'input.txt'))
    sol_A = solution_A(h_pos)
    sol_B = solution_B(h_pos)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()