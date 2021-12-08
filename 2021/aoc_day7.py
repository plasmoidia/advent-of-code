#! python

import numpy as np

if __name__ == '__main__':
    filename = 'aoc_day7_input.txt'

    pos = np.genfromtxt(filename, delimiter=',', dtype=int)
    crabs = pos.shape[0]
    max_pos = np.max(pos)
    print(f'There are {crabs} crabs spread out to {max_pos}')

    min_fuel = 1000000000
    min_align = None
    for align in range(max_pos):
        fuel = np.sum(np.abs(pos - align))
        if fuel < min_fuel:
            min_align = align
            min_fuel = fuel

    print(f'Min fuel {min_fuel} used to align at {min_align} at 1 fuel per step')

    min_fuel = 100000000000
    min_align = None
    for align in range(max_pos):
        diff = np.abs(pos - align)
        per_fuel = (diff * (diff + 1)) // 2
        fuel = np.sum(per_fuel)
        if fuel < min_fuel:
            min_align = align
            min_fuel = fuel

    print(f'Min fuel {min_fuel} used to align at {min_align} at linear fuel per step')
