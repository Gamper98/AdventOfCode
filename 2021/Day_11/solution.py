import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        raw_data = f.read().rstrip('\n').split('\n')
        octs = np.array([[int(d) for d in row] for row in raw_data], dtype=np.int8)
        return octs

def calc_energy(octs):
    flashed_octs = np.zeros_like(octs, dtype=np.bool8)
    change_mtx = np.array([[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]], dtype=np.int8)
    octs += 1
    is_flashing = octs >= 10
    while np.any(is_flashing):
        octs[is_flashing] == 0
        flashed_octs += is_flashing
        flash_pos = np.argwhere(is_flashing)
        flash_pos = np.repeat(flash_pos[:,:,None], repeats=8, axis=2)
        flash_pos += change_mtx.swapaxes(0,1)[None]
        flash_pos = flash_pos.swapaxes(1,2).reshape(-1, 2)
        good_pos_mask = (flash_pos[:,0] >= 0) & (flash_pos[:,0] < octs.shape[0]) &\
            (flash_pos[:,1] >= 0) & (flash_pos[:,1] < octs.shape[1])
        flash_pos = flash_pos[good_pos_mask]
        np.add.at(octs, (flash_pos[:,0], flash_pos[:,1]), 1)
        octs[flashed_octs] = 0
        is_flashing = octs >= 10
    return np.count_nonzero(flashed_octs)

def solution_A(octs, steps):
    flashes = 0
    for i in range(steps):
        flashes += calc_energy(octs)
    return flashes

def solution_B(octs):
    step = 0
    while True:
        step += 1
        if calc_energy(octs) == octs.size:
            return step + 100

def main():
    octs = read(os.path.join(ROOT_DIR, '2021\Day_11\input', 'input.txt'))
    sol_A = solution_A(octs, 100)
    sol_B = solution_B(octs)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()