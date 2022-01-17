import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        raw_data = f.read().rstrip('\n').split('\n')
        split_data = [[int(d) for d in str(item)]for item in raw_data]
        return np.array(split_data, dtype=np.int8)

def byte_to_int(num):
    return num.dot(2**np.arange(num.size)[::-1])

def solution_A(data):
    count_ones = np.count_nonzero(data, axis=0)
    gamma = count_ones > data.shape[0]/2
    gamma = byte_to_int(gamma)
    eps = 2**data.shape[1] - 1 - gamma
    return eps * gamma

def find_rating(data, func):
    for i in range(data.shape[1]):
        one_or_zero = func(np.count_nonzero(data[:,i]), data.shape[0]/2)
        mask = data[:, i] == int(one_or_zero)
        data = data[mask]
        if data.shape[0] == 1:
            return data[0]

def solution_B(data):
    oxygen = find_rating(data, lambda n,m: n < m)
    co2 = find_rating(data, lambda n,m: n >= m)
    oxygen_int = byte_to_int(oxygen)
    co2_int = byte_to_int(co2)
    return oxygen_int * co2_int

def main():
    data = read(os.path.join(ROOT_DIR, '2021\Day_03\input', 'input.txt'))
    sol_A = solution_A(data)
    sol_B = solution_B(data)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()