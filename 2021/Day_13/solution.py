import os
from config.definitions import ROOT_DIR
import re
import numpy as np

def read(text):
    with open(text, 'r') as f:
        coords, folds = f.read().rstrip('\n').split('\n\n')
        coords = np.array([pos.split(',') for pos in coords.rstrip('\n').split('\n')],dtype=np.int32)
        folds = re.findall(r'([xy])=(\d+)',folds)
        return coords, folds

def fold_paper(folds, paper):
    axc = {'x': 1, 'y':0}
    for ax, v in folds:
        p1, p2 = np.array_split(paper, 2, axis=axc[ax])
        paper = np.delete(p1, int(v), axis=axc[ax]) + np.flip(p2, axis=axc[ax])
    return paper

def make_paper(coords):
    max_y = np.max(coords[:,1]) + 1
    max_x = np.max(coords[:,0]) + 1
    paper = np.zeros((max_y, max_x), dtype=np.bool8)
    paper[coords[:,1],coords[:,0]] = True
    return paper

def solution_A(coords, folds):
    paper = make_paper(coords)
    paper = fold_paper([folds[0]], paper)
    return np.count_nonzero(paper)

def solution_B(coords, folds):
    paper = make_paper(coords)
    paper = fold_paper(folds, paper)
    with open(os.path.join(ROOT_DIR, '2021\Day_13\input', 'input.txt'), 'w') as w:
        for line in paper:
            out_str = ''.join((~line).astype(np.int32).astype(np.unicode_))
            w.write(f'{out_str}\n')        
    return 0

def main():
    coords, folds = read(os.path.join(ROOT_DIR, '2021\Day_13\input', 'input.txt'))
    sol_A = solution_A(coords, folds)
    sol_B = solution_B(coords, folds)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()