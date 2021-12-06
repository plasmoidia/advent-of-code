# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:21:49 2021

@author: jonathan.berry
"""

if __name__ == '__main__':
    # part 1
    position = {'forward': 0, 'up': 0, 'down': 0}
    with open('aoc_day2_input.txt') as f:
        for line in f:
            move = line.strip().split(' ')
            position[move[0]] += int(move[1])
    
    depth = position['down'] - position['up']
    horiz = position['forward']
    print(f'Moved {horiz} horizontally, {depth} in depth, product {depth*horiz}')

    # part 2
    position = {'forward': 0, 'depth': 0, 'aim': 0}
    with open('aoc_day2_input.txt') as f:
        for line in f:
            move = line.strip().split(' ')
            value = int(move[1])
            if move[0] == 'forward':
                position['forward'] += value
                position['depth'] += value * position['aim']
            elif move[0] == 'down':
                position['aim'] += value
            elif move[0] == 'up':
                position['aim'] -= value

    depth = position['depth']
    horiz = position['forward']
    print(f'Moved {horiz} horizontally, {depth} in depth, product {depth*horiz}')
