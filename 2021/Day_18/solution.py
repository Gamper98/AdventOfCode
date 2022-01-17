import os
from config.definitions import ROOT_DIR
import json
from collections import defaultdict
from copy import deepcopy

def read(text):
    with open(text, 'r') as f:        
        return [json.loads(line) for line in f.readlines()]

def magnitude(final_sum):
    if isinstance(final_sum, int):
        return final_sum
    left = 3 * magnitude(final_sum[0])        
    right = 2 * magnitude(final_sum[1])
    return left + right

def add_to_side(full_add, idx, num):
    if not idx:
        return 0
    sub_list = full_add
    for i in idx[:-1]:
        sub_list = sub_list[i]
    sub_list[idx[-1]] += num
    return sub_list[idx[-1]]

def find_nearest_side_idx(full_add, idx, side):
    nearest_left_int = []
    if (not side) not in idx:
        return nearest_left_int
    last_one_pos = idx[::-1].index(int(not side))
    last_one_pos = len(idx) - 1 - last_one_pos
    is_int = full_add.copy()
    i = 0
    while True:
        if isinstance(is_int, int):
            return nearest_left_int
        if i < last_one_pos:
            nearest_left_int.append(idx[i])
        elif i == last_one_pos:
            nearest_left_int.append(side)
        else:
            nearest_left_int.append(int(not side))
        is_int = is_int[nearest_left_int[-1]]
        i += 1

def find_num(full_add, idx, side):
    sub_list = full_add
    for i in idx:
        sub_list = sub_list[i]
    return sub_list[side]

def explode(full_add, idx, op_order):
    left_nearest = find_nearest_side_idx(full_add, idx, 0)
    right_nearest = find_nearest_side_idx(full_add, idx, 1)
    num_left = add_to_side(full_add, left_nearest, find_num(full_add, idx, 0))
    num_right = add_to_side(full_add, right_nearest, find_num(full_add, idx, 1))
    sub_list = full_add
    for i in idx[:-1]:
        sub_list = sub_list[i]
    sub_list[idx[-1]] = 0
    if num_left >= 10:
        op_order['sp'].append(tuple(left_nearest))
    if num_right >= 10:
        op_order['sp'].append(tuple(right_nearest))

def split(full_add, idx, op_order):
    sub_list = full_add
    for i in idx[:-1]:
        sub_list = sub_list[i]
        if isinstance(sub_list, int): return
    if not isinstance(sub_list[idx[-1]], int): return
    num = sub_list[idx[-1]]
    sub_list[idx[-1]] = [num//2, (num+1)//2]
    if len(idx) >= 4:
        op_order['ex'].append(idx)
    idx = list(idx)
    idx.append(0)
    if num // 2 >= 10:
        op_order['sp'].append(tuple(idx))
    if (num+1) // 2 >= 10:
        idx[-1] = 1
        op_order['sp'].append(tuple(idx))

def reduce_sum(add, op_order):
    while True:
        if op_order['ex']:
            op_order['ex'] = sorted(list(set(op_order['ex'])))
            idx = op_order['ex'].pop(0)
            explode(add, idx, op_order)
        elif op_order['sp']:
            op_order['sp'] = sorted(list(set(op_order['sp'])))
            idx = op_order['sp'].pop(0)
            split(add, idx, op_order)
        else:
            return

def find_exp(full_add, add, layer, idx, op_order):
    if isinstance(add, int):
        return True
    idx.append(0)
    is_left_int = find_exp(full_add, add[0], layer+1, idx.copy(), op_order)
    idx[-1] = 1
    is_right_int = find_exp(full_add, add[1], layer+1, idx.copy(), op_order)
    if layer > 4 and is_left_int and is_right_int:
        op_order['ex'].append(tuple(idx[:-1]))
    return False

def solution_A(homework):
    add = deepcopy(homework[0])
    for item in homework[1:]:
        op_order = defaultdict(lambda: [])
        add = [add, deepcopy(item)]
        find_exp(add, add, 1, [], op_order)
        reduce_sum(add, op_order)
    return magnitude(add)

def solution_B(homework):
    sums_of_two = []
    for left in homework:
        for right in homework:
            if left == right: continue
            op_order = defaultdict(lambda: [])
            add = [deepcopy(left), deepcopy(right)]
            find_exp(add, add, 1, [], op_order)
            reduce_sum(add, op_order)
            sums_of_two.append(magnitude(add))
    return max(sums_of_two)

def main():
    homework = read(os.path.join(ROOT_DIR, '2021\Day_18\input', 'input.txt'))
    sol_A = solution_A(homework)
    sol_B = solution_B(homework)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()