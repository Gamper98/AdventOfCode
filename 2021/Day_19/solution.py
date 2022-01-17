import os
from config.definitions import ROOT_DIR
import numpy as np
from collections import defaultdict

def read(text):
    with open(text, 'r') as f:
        return [np.array([row.split(',') for row in data.split('\n')[1:]], dtype=np.int32) for data in f.read().split('\n\n')]

def solution_A(scanners, scanner_pos):
    scanner_pos[0] = np.array([0,0,0], dtype=np.int32)
    beacons = scanners[0].copy()
    pos = {0}
    visited = set()
    while pos:
        fst = pos.pop()
        for snd in range(0,len(scanners)):
            if fst == snd or fst in visited: continue
            #[0,1,2]#+++[2,0,1]#+++[1,2,0]#+++[ 1, 1, 1]
            #[1,0,2]#+-+[0,2,1]#+-+[2,1,0]#+-+[ 1,-1, 1]
            #[0,1,2]#--+[2,0,1]#--+[1,2,0]#--+[-1,-1, 1]
            #[1,0,2]#-++[0,2,1]#-++[2,1,0]#-++[-1, 1, 1]
            #[0,1,2]#-+-[2,0,1]#-+-[1,2,0]#-+-[-1, 1,-1]
            #[1,0,2]#++-[0,2,1]#++-[2,1,0]#++-[ 1, 1,-1]
            #[0,1,2]#+--[2,0,1]#+--[1,2,0]#+--[ 1,-1,-1]
            #[1,0,2]#---[0,2,1]#---[2,1,0]#---[-1,-1,-1]
            s0 = np.repeat(np.repeat(scanners[fst][None], len(scanners[snd]), axis=0)[None], 24, axis=0)
            s1_1 = np.repeat(scanners[snd][:,None], len(scanners[fst]), axis=1)
            s1_1s = s1_1.copy()
            s1_1s[:,:,[0,1]] = s1_1[:,:,[1,0]] 
            s1_2 = np.roll(s1_1, 1, 2)
            s1_2s = s1_2.copy()
            s1_2s[:,:,[0,1]] = s1_2[:,:,[1,0]] 
            s1_3 = np.roll(s1_2, 1, 2)
            s1_3s = s1_3.copy()
            s1_3s[:,:,[0,1]] = s1_3[:,:,[1,0]] 
            s1__1 = np.tile(np.array([s1_1,s1_1s]), (4,1,1,1))
            s1__2 = np.tile(np.array([s1_2,s1_2s]), (4,1,1,1))
            s1__3 = np.tile(np.array([s1_3,s1_3s]), (4,1,1,1))
            direct = np.array(
            [[ 1, 1, 1],
            [ 1,-1, 1],
            [-1,-1, 1],
            [-1, 1, 1],
            [-1, 1,-1],
            [ 1, 1,-1],
            [ 1,-1,-1],
            [-1,-1,-1]], dtype=np.int32)
            s1__1 = s1__1 * direct[:,None,None]
            s1__2 = s1__2 * direct[:,None,None]
            s1__3 = s1__3 * direct[:,None,None]
            s1 = np.concatenate((s1__1, s1__2, s1__3))
            diff = (s0-s1).reshape(24,-1,3)
            for ori in range(24):
                uniques , count = np.unique(diff[ori], return_counts=True, axis=0)
                more_than_12 = count >= 12
                #print(f'{fst=},{snd=}{np.any(more_than_12)}')
                if np.any(more_than_12):
                    scanner_pos[snd] = uniques[more_than_12][0] + scanner_pos[fst]
                    scanners[snd] = s1[ori,:,0]
                    pos.add(snd)
                    beacons = np.concatenate((beacons, (scanners[snd] + scanner_pos[snd])))
                    break
        visited.add(fst)
    return len(np.unique(beacons, axis=0))

def solution_B(scanner_pos):
    scan_pos = np.array(list(scanner_pos.values()))
    scan_pos_r = np.repeat(scan_pos[None], len(scanner_pos), axis = 0)
    scan_pos_r = scan_pos_r - scan_pos[:,None]
    return np.max(np.sum(scan_pos_r, axis=2))

def main():
    scanners = read(os.path.join(ROOT_DIR, '2021\Day_19\input', 'input.txt'))
    scanner_pos = defaultdict(lambda: tuple)
    scanner_pos
    sol_A = solution_A(scanners, scanner_pos)
    sol_B = solution_B(scanner_pos)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()
# %%
