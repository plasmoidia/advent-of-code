#! python

import numpy as np

def spread_energy(octos, pos):
    sz = octos.shape
    ul = (max(pos[0]-1, 0), max(pos[1]-1, 0))
    lr = (min(pos[0]+2, sz[0]), min(pos[1]+2, sz[1]))
    patch = octos[ul[0]:lr[0], ul[1]:lr[1]]
    patch[patch > 0] += 1

def process_flashes(octos):
    while True:
        num = 0
        for row in range(octos.shape[0]):
            for col in range(octos.shape[1]):
                pos = (row, col)
                val = octos[row, col]
                if val and val > 9:
                    num += 1
                    octos[row, col] = 0
                    spread_energy(octos, pos)
        if not num:
            break
    return np.sum(octos[:] == 0)

if __name__ == '__main__':
    filename = 'aoc_day11_input.txt'
    octos = np.genfromtxt(filename, delimiter=1, dtype=int)

    step = 0
    num_steps = 100
    total_flashes = 0
    while True:
        octos += 1
        flashes = process_flashes(octos)
        if step < num_steps:
            total_flashes += flashes
        step += 1
        if flashes == np.prod(octos.shape):
            sync_step = step
            break

    print(f'After {num_steps} steps, {total_flashes} flashes')
    print(f'First sync on step {sync_step}')

