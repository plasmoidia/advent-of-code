# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 16:00:24 2021

@author: jonathan.berry
"""

import numpy as np

def select_nums(data, col, keep_more, tie_val):
    ones_val = np.sum(data[:,col])
    zeros_val = data.shape[0] - ones_val
    if ones_val > zeros_val:
        keep_val = keep_more
    elif ones_val < zeros_val:
        keep_val = 1 - keep_more
    else:
        keep_val = tie_val

    return data[data[:,col] == keep_val,:]

def select_num(data, keep_more, tie_val):
    num_bits = data.shape[1]
    for place in range(num_bits):
        data = select_nums(data, place, keep_more, tie_val)
        if data.shape[0] == 1:
            return data[0,:]
    return None # should not get here

if __name__ == '__main__':
    # part 1
    filename = 'aoc_day3_input.txt'
    data = np.genfromtxt(filename, delimiter=1, dtype=int)

    sums = np.sum(data, axis=0)
    val_bin_arr = (sums > (data.shape[0] // 2)) * 1
    
    gamma = int(''.join([str(a) for a in val_bin_arr]), base=2)
    epsilon = gamma ^ (2**data.shape[1] - 1)
    power = gamma * epsilon

    print(f'Power is {power}, {gamma=} {epsilon=}')

    # part 2
    oxy_gen_arr = select_num(data, 1, 1)
    co2_scrub_arr = select_num(data, 0, 0)

    oxy_gen = int(''.join([str(a) for a in oxy_gen_arr]), base=2)
    co2_scrub = int(''.join([str(a) for a in co2_scrub_arr]), base=2)

    life_support = oxy_gen * co2_scrub

    print(f'Life Support Rating is {life_support}, {oxy_gen=} {co2_scrub=}')
