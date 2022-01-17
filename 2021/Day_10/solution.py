import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        syntax = f.read().rstrip('\n').split('\n')
        return syntax

def calc_syntax_error(syntax):
    scoring = {')': 3, ']':57, '}': 1197, '>': 25137}
    bracket_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for bracket in syntax:
        if bracket in ('(', '[', '{', '<'):
            stack.append(bracket)
        else:
            if bracket_pairs[stack.pop()] != bracket:
                return scoring[bracket]
    return 0

def calc_auto_comp_score(syntax):
    comp_score = {')': 1, ']': 2, '}': 3, '>': 4}
    bracket_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    stack = []
    for bracket in syntax:
        if bracket in ('(', '[', '{', '<'):
            stack.append(bracket)
        else:
            if bracket_pairs[stack.pop()] != bracket:
                return 0
    auto_comp_score = 0
    for bracket in stack[::-1]:
        auto_comp_score = auto_comp_score * 5 + comp_score[bracket_pairs[bracket]]
    return auto_comp_score

def solution_A(syntax):
    error_sum = 0
    for item in syntax:
        error_sum += calc_syntax_error(item)
    return error_sum

def solution_B(syntax):
    auto_comp_scores = []
    for item in syntax:
        comp_score = calc_auto_comp_score(item)
        if comp_score != 0:
            auto_comp_scores.append(comp_score)
    auto_comp_scores = np.array(auto_comp_scores, dtype=np.float64)
    return np.median(auto_comp_scores)

def main():
    syntax = read(os.path.join(ROOT_DIR, '2021\Day_10\input', 'input.txt'))
    sol_A = solution_A(syntax)
    sol_B = solution_B(syntax)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()