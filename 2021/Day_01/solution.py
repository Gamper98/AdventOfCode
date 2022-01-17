import os
from config.definitions import ROOT_DIR

import numpy as np

def read(text):
    with open(text, 'r') as f:
        data = np.array(f.read().rstrip('\n').split('\n'), dtype=np.int32)
        return data

def count_inc(nums):    
    inc_dec = nums[1:] - nums[:-1]
    return np.count_nonzero(inc_dec > 0)

def solution_A(nums):
    return count_inc(nums)

def solution_B(nums):
    nums_3 = np.zeros((len(nums)-2, 3), dtype=np.int32)
    nums_3[:,0] = nums[0:-2]
    nums_3[:,1] = nums[1:-1]
    nums_3[:,2] = nums[2:]
    return count_inc(np.sum(nums_3, axis=1))

def main():
    data = read(os.path.join(ROOT_DIR, '2021\Day_01\input', 'input.txt'))
    sol_A = solution_A(data)
    sol_B = solution_B(data)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()