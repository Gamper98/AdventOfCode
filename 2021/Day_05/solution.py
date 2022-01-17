import os
from config.definitions import ROOT_DIR
import re
import numpy as np

def read(text):
    with open(text, 'r') as f:
        coords = np.array(re.findall(r'(\d+)',f.read()), dtype=np.int32)
        coords = coords.reshape(-1, 2, 2)
        return coords
        
def calc_field(coords, do_diag):
    x_max = np.max(coords[:,:,0])
    y_max = np.max(coords[:,:,1])
    field = np.zeros((x_max+1, y_max+1), dtype=np.int8)
    for p1, p2 in coords:
        if p1[0] == p2[0]:
            field[p1[1]:p2[1]+np.sign(p2[1]-p1[1]):np.sign(p2[1]-p1[1]),p1[0]] += 1
        elif p1[1] == p2[1]: 
            field[p1[1],p1[0]:p2[0]+np.sign(p2[0]-p1[0]):np.sign(p2[0]-p1[0])] += 1
        elif do_diag:
            field[range(p1[1],p2[1]+np.sign(p2[1]-p1[1]),np.sign(p2[1]-p1[1])),
            range(p1[0],p2[0]+np.sign(p2[0]-p1[0]),np.sign(p2[0]-p1[0]))] += 1
    return np.count_nonzero(field >= 2)

def solution_A(coords):
    return calc_field(coords, False)
    
def solution_B(coords):
    return calc_field(coords, True)

def main():
    coords = read(os.path.join(ROOT_DIR, '2021\Day_05\input', 'input.txt'))
    sol_A = solution_A(coords)
    sol_B = solution_B(coords)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()