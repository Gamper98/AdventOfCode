import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        raw_data = f.read().rstrip('\n').replace('| ','').split('\n')
        signals = np.array([item.split(' ') for item in raw_data], dtype=np.unicode_)
        return signals

def solution_A(signals):
    signals_len = np.char.str_len(signals)
    return np.count_nonzero((signals_len[:,-4:] <= 4 ) | (signals_len[:,-4:] == 7))

def solve_doubles(chars_to_chars, five_long):
    set_five_long = set(five_long)
    if len(chars_to_chars['c'] & set_five_long) == 2:
        chars_to_chars['d'] = chars_to_chars['d'] & set_five_long
        chars_to_chars['g'] = chars_to_chars['g'] & set_five_long
        chars_to_chars['b'] -= chars_to_chars['d']
        chars_to_chars['e'] -= chars_to_chars['g']
    elif len(chars_to_chars['b'] & set_five_long) == 2:
        chars_to_chars['f'] = chars_to_chars['f'] & set_five_long
        chars_to_chars['g'] = chars_to_chars['g'] & set_five_long
        chars_to_chars['c'] -= chars_to_chars['f']
        chars_to_chars['e'] -= chars_to_chars['g']
    elif len(chars_to_chars['e'] & set_five_long) == 2:
        chars_to_chars['c'] = chars_to_chars['c'] & set_five_long
        chars_to_chars['d'] = chars_to_chars['d'] & set_five_long
        chars_to_chars['f'] -= chars_to_chars['c']
        chars_to_chars['b'] -= chars_to_chars['d']

def find_last(chars_to_chars, five_long):
    set_five_long = set(five_long)
    if len(chars_to_chars['b']) == 2:
        chars_to_chars['b'] =chars_to_chars['b'] - set_five_long
        chars_to_chars['d'] -= chars_to_chars['b']
    elif len(chars_to_chars['e']) == 2:        
        chars_to_chars['e'] = chars_to_chars['e'] - set_five_long
        chars_to_chars['g'] -= chars_to_chars['e']
    elif len(chars_to_chars['c']) == 2:
        if len((chars_to_chars['e'] | chars_to_chars['g']) & set_five_long) == 2:     
            chars_to_chars['c'] = chars_to_chars['c'] & set_five_long
            chars_to_chars['f'] -= chars_to_chars['c']
        else:
            chars_to_chars['c'] = chars_to_chars['c'] - set_five_long
            chars_to_chars['f'] -= chars_to_chars['c']

def solve_encrypt(entry):
    chars_to_chars = {'a':{},'b':{},'c':{},'d':{},'e':{},'f':{},'g':{}}
    entry_len = np.char.str_len(entry)
    mask_num_1 = entry_len == 2
    mask_num_4 = entry_len == 4
    mask_num_7 = entry_len == 3
    mask_num_8 = entry_len == 7
    mask_5_long = entry_len == 5
    num_1 = set(entry[mask_num_1][0]) 
    num_4 = set(entry[mask_num_4][0]) 
    num_7 = set(entry[mask_num_7][0]) 
    num_8 = set(entry[mask_num_8][0])
    five_long = entry[mask_5_long]
    chars_to_chars['a'] = num_7 - num_1
    chars_to_chars['c'] = chars_to_chars['f'] = num_7 & num_1
    chars_to_chars['b'] = chars_to_chars['d'] = num_4 - num_1
    chars_to_chars['e'] = chars_to_chars['g'] = num_8 - num_4 - chars_to_chars['a']
    solve_doubles(chars_to_chars, five_long[0])
    find_last(chars_to_chars, five_long[1])
    return {i:k.pop() for i,k in chars_to_chars.items()}

def solution_B(signals):
    uniq_sig_patterns, output_values = signals[:,:10], signals[:,10:]
    nums = {0:{'a','b','c','e','f','g'},
        1:{'c','f'},
        2:{'a','c','d','e','g'},
        3:{'a','c','d','f','g'},
        4:{'b','c','d','f'},
        5:{'a','b','d','f','g'},
        6:{'a','b','d','e','f','g'},
        7:{'a','c','f'},
        8:{'a','b','c','d','e','f','g'},
        9:{'a','b','c','d','f','g'}
        }
    output_sum = 0
    for i, entry in enumerate(uniq_sig_patterns):
        c_t_c = solve_encrypt(entry)
        new_nums = {frozenset(c_t_c[letter] for letter in letters): num for num, letters in nums.items()}
        st = new_nums[frozenset(output_values[i,0])]
        nd = new_nums[frozenset(output_values[i,1])]
        rd = new_nums[frozenset(output_values[i,2])]
        th = new_nums[frozenset(output_values[i,3])]
        output_sum += int(str(st) + str(nd) + str(rd) + str(th))
    return output_sum

def main():
    signals = read(os.path.join(ROOT_DIR, '2021\Day_08\input', 'input.txt'))
    sol_A = solution_A(signals)
    sol_B = solution_B(signals)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()