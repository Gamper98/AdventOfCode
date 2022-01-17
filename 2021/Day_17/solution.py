import os
from config.definitions import ROOT_DIR
import re
import numpy as np
from itertools import product

def read(text):
    with open(text, 'r') as f:
        data = re.findall(r'([-]*\d+)..([-]*\d+)', f.read())
        return [[int(i) for i in item] for item in data]


def solution_A(nums):
    return (abs(nums[1][0])-1) * abs(nums[1][0]) / 2

def solution_B(nums):
    min_x_vel = np.max(np.round(np.roots([1,1,-nums[0][0]*2]))).astype(np.int32)
    max_x_vel = np.max(np.round(np.roots([1,1,-nums[0][1]*2]))).astype(np.int32)
    init_velocitys = set()
    init_velocitys.update(product(range(nums[0][0], nums[0][1]+1), range(nums[1][0], nums[1][1]+1)))
    for steps in range(2,abs(nums[1][0]*2)+1):
        x_min = nums[0][0] // steps
        while True:
            min_sum = (2*x_min-steps+1)*steps/2
            if steps > min_x_vel:
                x_min = min_x_vel
                break
            if min_sum >= nums[0][0] and min_sum <= nums[0][1] :
                break
            x_min += 1
        x_max = x_min
        while True:
            max_sum = (2*x_max-steps+1)*steps/2
            if steps > min_x_vel:
                x_max = max_x_vel
                break
            if max_sum > nums[0][1]:
                x_max -= 1
                break
            x_max += 1
        out_of_bound = False
        y_min = nums[1][0]
        while True:
            min_sum =  (2*y_min - \
                steps + 1 - (y_min>=0) * (2 * y_min + 1))*\
                    (steps - (y_min>=0) * (2 * y_min + 1))/2
            if min_sum >= nums[1][0]:
                if min_sum > nums[1][1]:
                    out_of_bound = True
                break
            y_min += 1
        y_max = y_min
        while True:
            max_sum = (2*y_max - \
                steps + 1 - (y_max>=0) * (2 * y_max + 1))*\
                    (steps - (y_max>=0) * (2 * y_max + 1))/2
            if max_sum > nums[1][1]:
                y_max -= 1
                break
            y_max += 1
        if out_of_bound: continue
        init_velocitys.update(product(range(x_min, x_max+1), range(y_min, y_max+1)))
    return len(init_velocitys)

def main():
    data = read(os.path.join(ROOT_DIR, '2021\Day_17\input', 'input.txt'))
    sol_A = solution_A(data)
    sol_B = solution_B(data)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()