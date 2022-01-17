import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        timers = np.array(f.read().rstrip('\n').split(','),dtype=np.int8)
        return timers

#too slow
def calc_lfish_prod_brute_force(timers, days):
    timers_c = np.sort(timers.copy())
    for i in range(days):
        print(f'{i=} {timers_c.size=}')
        timers_c -= 1
        mask = timers_c == -1
        timers_c[mask] = 6
        timers_c = np.append(timers_c, [8]*np.count_nonzero(mask))
    return timers_c.size

def calc_lfish_prod_shift(timers, days):
    timer_count = np.zeros(9, dtype=np.int64)
    np.add.at(timer_count, timers, 1)
    for i in range(days):
        new_lf = timer_count[0]
        timer_count = np.roll(timer_count, -1)
        timer_count[6] += new_lf
    return np.sum(timer_count)

def solution_A(timers, days):
    return calc_lfish_prod_shift(timers, days)

def solution_B(timers, days):
    return calc_lfish_prod_shift(timers, days)
    
def main():
    timers = read(os.path.join(ROOT_DIR, '2021\Day_06\input', 'input.txt'))
    sol_A = solution_A(timers,80)
    sol_B = solution_B(timers, 256)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()