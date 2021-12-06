# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 12:41:29 2021

@author: jonathan.berry
"""

import numpy as np

if __name__ == '__main__':
    filename = 'aoc_day1_input.txt'
    data = np.genfromtxt(filename)

    # part 1
    total_increases = np.sum(data[1:] > data[:-1])
    print(f'Found {total_increases} of {len(data)} raw measurements')

    # part 2
    moving_avg = np.convolve(data, np.ones(3), 'valid')
    avg_increases = np.sum(moving_avg[1:] > moving_avg[:-1])
    print(f'Found {avg_increases} of {len(moving_avg)} smoothed measurements')
