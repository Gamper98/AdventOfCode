import os
from config.definitions import ROOT_DIR
import re
import numpy as np

def read(text):
    with open(text, 'r') as f:
        raw_data = np.array(re.findall(r'[-]*\d+', f.read().replace('on', '1').replace('off', '0')), dtype=np.int64)
        raw_data = raw_data.reshape(-1,7)
        onoff = raw_data[:,0]
        reactors = raw_data[:,1:].reshape(-1,3,2).swapaxes(1,2)
        return onoff, reactors

def split_aabb(s_1,s_2, p_1, p_2, to_swap):
    dist = (p_1 - s_1) * to_swap
    dist[dist < 0] = 0
    overlap = np.sort([s_1,s_2, p_1, p_2], axis=0)[[1,2]]
    overlap_size = overlap[1] - overlap[0]
    ols_tri = np.tril(np.repeat(overlap_size[None], 3, axis=0), -1)
    left_idx = np.repeat(s_1[None], 3, axis=0)
    right_idx = np.tril(s_1) + np.triu(s_2, 1)
    dist_tri = np.tril(np.repeat(dist[None], 3, axis=0), -1)
    dist_diag = np.diag(dist - 1)
    left_aabbs_idx = left_idx + to_swap * dist_tri
    right_aabbs_idx = right_idx + to_swap * (dist_diag + dist_tri + ols_tri)
    aabbs = np.concatenate((left_aabbs_idx, right_aabbs_idx), axis=1).reshape(-1,2,3)
    aabbs = aabbs[dist != 0]
    return np.sort(aabbs, axis=1)

def turn_onoff_cube(overlapping_aabbs, p_min, p_max, is_on):
    not_overlapping_aabbs = np.empty((0,2,3), int)
    for (s_min, s_max) in overlapping_aabbs:
        if np.all((p_min <= s_min) & (s_max <= p_max)):
            continue
        left_aabbs = split_aabb(s_min,s_max,p_min,p_max,1)
        right_aabbs = split_aabb(s_max,s_min,p_max,p_min,-1)
        not_overlapping_aabbs = np.concatenate((not_overlapping_aabbs, left_aabbs, right_aabbs), axis=0)
    if is_on:
        not_overlapping_aabbs = np.append(not_overlapping_aabbs, [[p_min,p_max]], axis=0)
    return not_overlapping_aabbs
        #s_min_x,              s_min_y,               s_min_z | s_min_x + leftdist_x,         s_max_y,                      s_max_z
        #s_min_x + leftdist_x, s_min_y,               s_min_z | s_min_x + leftdist_x + ols_x, s_min_y + leftdist_y,         s_max_z
        #s_min_x + leftdist_x, s_min_y + left_dist_y, s_min_z | s_min_x + leftdist_x + ols_x, s_min_y + leftdist_y + ols_y, s_min_z + left_dist_z

        #s_max_x - right_dist_x,         s_min_y,                        s_min_z                | s_max_y               , s_max_y               , s_max_z
        #s_max_x - right_dist_x - ols_x, s_max_y - right_dist_y,         s_min_z                | s_max_y - right_dist_x, s_max_y               , s_max_z
        #s_max_x - right_dist_x - ols_x, s_max_y - right_dist_y - ols_y, s_max_z - right_dist_z | s_max_y - right_dist_x, s_max_y - right_dist_y, s_max_z

def reactor_reboot(onoff, reactors):
    n_ol_aabb = np.array([reactors[0]])
    for is_on, (p_min, p_max) in zip(onoff[1:], reactors[1:]):
        intersect = np.all((n_ol_aabb[:,0] <= p_max) & (n_ol_aabb[:,1] >= p_min), axis=1)
        split_aabbs = turn_onoff_cube(n_ol_aabb[intersect], p_min, p_max, is_on)
        n_ol_aabb = n_ol_aabb[~intersect]
        if split_aabbs.size:
            n_ol_aabb = np.concatenate((n_ol_aabb, split_aabbs), axis=0)
    size_of_cubes = n_ol_aabb[:,1] - n_ol_aabb[:,0] + 1
    size_of_cubes = size_of_cubes
    return np.sum(np.product(size_of_cubes, axis=1))

def solution_A(onoff, reactors):
    mask = (reactors >= -50) & (reactors <= 50)
    mask = np.all(mask, axis=(1,2))
    return reactor_reboot(onoff[mask], reactors[mask])

def solution_B(onoff, reactors):
    return reactor_reboot(onoff, reactors)

def main():
    onoff, reactors = read(os.path.join(ROOT_DIR, '2021\Day_22\input', 'input.txt'))
    sol_A = solution_A(onoff, reactors)
    sol_B = solution_B(onoff, reactors)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()