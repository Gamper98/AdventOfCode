import os
from config.definitions import ROOT_DIR
import numpy as np

def read(text):
    with open(text, 'r') as f:
        img_ench_alg = f.readline().rstrip('\n').replace('.', '0').replace('#','1')
        img_ench_alg = [int(d) for d in img_ench_alg]
        input_image = f.read().rstrip('\n').lstrip('\n').replace('.', '0').replace('#','1').split('\n')
        input_image = [[int(d) for d in item] for item in input_image]
        return np.array(img_ench_alg), np.array(input_image)

def enhance_image(img_ench_alg, input_image, n):
    tmp = np.zeros((input_image.shape[0] + n*2+6, input_image.shape[0] + n*2+6), dtype=np.int32)
    tmp[n+3:-(n+3),n+3:-(n+3)] = input_image
    input_image = tmp
    for _ in range(n):
        new_image = np.zeros(input_image.shape, dtype=np.int32)
        new_image = np.repeat(new_image[None], 9, axis=0)
        extended_img = np.full((input_image.shape[0] + 3, input_image.shape[0] + 3),\
             fill_value=input_image[0,0], dtype=np.int32)
        extended_img[1:-2,1:-2] = input_image
        for i in range(9):
            new_image[i] = extended_img[i//3:-3+i//3, i%3:-3+i%3]
        poses = np.sum(new_image*2**np.arange(8,-1,-1,dtype='int64')[:,None,None], axis=0)
        not_zeros_pos = np.argwhere(poses != -1)
        not_zeros = poses[not_zeros_pos[:,0],not_zeros_pos[:,1]]
        values = img_ench_alg[not_zeros]
        input_image = np.zeros_like(poses)
        input_image[not_zeros_pos[:,0],not_zeros_pos[:,1]] = values
    return np.count_nonzero(input_image)

def solution_A(img_ench_alg, input_image, n):
    return enhance_image(img_ench_alg, input_image, n)

def solution_B(img_ench_alg, input_image, n):
    return enhance_image(img_ench_alg, input_image, n)


def main():
    img_ench_alg, input_image = read(os.path.join(ROOT_DIR, '2021\Day_20\input', 'input.txt'))
    sol_A = solution_A(img_ench_alg, input_image, 2)
    sol_B = solution_B(img_ench_alg, input_image, 50)
    print(f'{sol_A=}')
    print(f'{sol_B=}')

if __name__ == "__main__":
    main()