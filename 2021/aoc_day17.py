#! python

import sys
import numpy as np

class probe(object):
    def __init__(self, x_vel=0, y_vel=0):
        self.loc = np.zeros(2, dtype=int)
        self.vel = np.array([x_vel, y_vel], dtype=int)
        self.vel0 = self.vel.copy()
        self.max_height = 0

    def step(self):
        self.loc += self.vel
        self.vel[0] = self.vel[0] - np.sign(self.vel[0])
        self.vel[1] -= 1
        self.max_height = max(self.max_height, self.loc[1])

    def inside(self, target):
        return target[0][0] <= self.loc[0] <= target[1][0] and \
               target[0][1] <= self.loc[1] <= target[1][1]

    def past(self, target):
        return self.loc[0] > target[1][0] or self.loc[1] < target[0][1]

def parse_target_area(line):
    sep = ': '
    idx = line.find(sep)
    loc_str = line[idx+len(sep):]
    x_str, y_str = loc_str.split(', ')
    xs = x_str.split('=')[1].split('..')
    ys = y_str.split('=')[1].split('..')
    return ((int(xs[0]), int(ys[0])), (int(xs[1]), int(ys[1])))

def sim_probe(target):
    max_height = 0
    max_vel0 = None
    max_velx = target[1][0]+1
    max_vely = np.max(np.abs([target[0][1], target[1][1]]))+1
    success_vels = []
    for v_x in range(1, max_velx+1):
        for v_y in range(-max_vely, max_vely+1):
            p = probe(v_x, v_y)
            while not p.past(target):
                p.step()
                if p.inside(target):
                    success_vels.append(p.vel0)
                    if p.max_height > max_height:
                        max_height = p.max_height
                        max_vel0 = p.vel0
                    break
    return max_height, max_vel0, success_vels

if __name__ == '__main__':
    filename = 'aoc_day17_input.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as f:
        line = f.read().strip()
    target = parse_target_area(line)
    max_h, vel0, success = sim_probe(target)
    num_success = len(success)
    print(f'Max height of {max_h} with init vel of {vel0[0]}, {vel0[1]}')
    print(f'Found {num_success} successful init vels')
