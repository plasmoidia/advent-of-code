# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 10:46:04 2021

@author: jonathan.berry
"""

import numpy as np

def simulate(school, days, spawn_time=7, spawn_age=8):
    cur_school = school
    for day in range(1, days+1):
        next_school = {}
        for age in cur_school:
            next_school[age] = 0
        for age in cur_school:
            spawn = False
            next_age = age - 1
            if next_age < 0:
                next_age = spawn_time-1
                spawn = True
            next_school[next_age] += cur_school[age]
            if spawn:
                next_school[spawn_age] += cur_school[age]
        cur_school = next_school
    return sum([cur_school[age] for age in next_school])

if __name__ == '__main__':
    filename = 'aoc_day6_input.txt'
    fish = np.genfromtxt(filename, delimiter=',')
    school = {}
    for age in range(9):
        school[age] = 0
    for f in fish:
        school[f] += 1

    print(f'{len(fish)} lanternfish on day 0')
    days = 80
    num = simulate(school, days)
    print(f'{num} lanternfish after {days} days')

    days = 256
    num = simulate(school, days)
    print(f'{num} lanternfish after {days} days')
