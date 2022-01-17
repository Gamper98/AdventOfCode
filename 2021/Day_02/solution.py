import os
from config.definitions import ROOT_DIR

def read(text):
    with open(text, 'r') as f:
        raw_data = f.read().rstrip('\n').split('\n')
        data = [(item.split(' ')[0], int(item.split(' ')[1])) for item in raw_data]
        return data

def solution_A(data):
    hor = 0
    vert = 0
    for dir, num in data:
        if dir == 'forward':
            hor += num
        elif dir == 'down':
            vert += num
        else:
            vert -= num
    return hor * vert

def solution_B(data):
    hor = 0
    vert = 0
    aim = 0
    for dir, num in data:
        if dir == 'forward':
            hor += num
            vert += aim * num
        elif dir == 'down':
            aim += num
        else:
            aim -= num
    return hor * vert

def main():
    data = read(os.path.join(ROOT_DIR, '2021\Day_02\input', 'input.txt'))
    sol_A = solution_A(data)
    sol_B = solution_B(data)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()