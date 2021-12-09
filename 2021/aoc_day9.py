#! python

import numpy as np

if __name__ == '__main__':
    filename = 'aoc_day9_input.txt'
    height = np.genfromtxt(filename, delimiter=1, dtype=int)
    padded = np.ones((height.shape[0]+2, height.shape[1]+2), dtype=height.dtype) * 9
    padded[1:-1, 1:-1] = height
    shift_up = np.roll(padded, -1, axis=0)
    shift_down = np.roll(padded, 1, axis=0)
    shift_left = np.roll(padded, -1, axis=1)
    shift_right = np.roll(padded, 1, axis=1)

    minima_ud = np.logical_and(padded < shift_up, padded < shift_down)
    minima_lr = np.logical_and(padded < shift_left, padded < shift_right)
    minima_loc = np.logical_and(minima_ud, minima_lr)

    minima = padded[minima_loc]
    total = np.sum(minima) + len(minima)

    print(f'Found {total} risk')
