import os
from config.definitions import ROOT_DIR
import re
from collections import Counter, defaultdict

def read(text):
    with open(text, 'r') as f:
        poly_temp = [letter for letter in f.readline().rstrip('\n')]
        pair_insert = dict(re.findall(r'(\w+) -> (\w)', f.read()))
        return poly_temp, pair_insert

def solution_A(poly_temp, pair_insert, steps):
    current_poly = poly_temp.copy()
    for _ in range(steps):
        new_poly = current_poly.copy()
        for k in range(len(current_poly)-1):
            new_poly.insert(k+k+1, pair_insert[''.join([current_poly[k],current_poly[k+1]])])
        current_poly = new_poly.copy()
    count = Counter(''.join(current_poly))
    return max(count.values()) - min(count.values())

def solution_B(poly_temp, pair_insert, steps):
    current_pair_count = defaultdict(lambda: 0)
    for i in range(len(poly_temp)-1):
        current_pair_count[tuple(poly_temp[i:i+2])] = 1
    for _ in range(steps):
        new_pair_count = defaultdict(lambda: 0)
        for key in current_pair_count.keys():
            insert = pair_insert[''.join(key)]
            new_pair_count[(key[0], insert)] += current_pair_count[key]
            new_pair_count[(insert, key[1])] += current_pair_count[key]
        current_pair_count = new_pair_count.copy()
    count = defaultdict(lambda: 0)
    count[poly_temp[0]] += 1
    count[poly_temp[-1]] += 1
    for k_1, k_2 in current_pair_count.keys():
        count[k_1] += current_pair_count[(k_1,k_2)]
        count[k_2] += current_pair_count[(k_1,k_2)]
    return (max(count.values()) - min(count.values()))/2

def main():
    poly_temp, pair_insert = read(os.path.join(ROOT_DIR, '2021\Day_14\input', 'input.txt'))
    sol_A = solution_A(poly_temp, pair_insert, 10)
    sol_B = solution_B(poly_temp, pair_insert, 40)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()