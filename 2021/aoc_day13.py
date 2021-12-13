#! python

import sys
import numpy as np
import matplotlib
import matplotlib.pyplot

if __name__ == '__main__':
    filename = 'aoc_day13_input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    pre = 'fold along '
    pre_len = len(pre)
    with open(filename) as f:
        points = []
        folds = []
        for l in f:
            line = l.strip()
            if len(line) == 0:
                break
            points.append([int(n) for n in line.split(',')])
        for l in f:
            line = l.strip()
            folds.append(line[pre_len:].split('='))
    points = np.fliplr(np.array(points))

    sz = np.max(points, axis=0)+1
    paper = np.zeros(sz, dtype=bool)
    for x, y in points:
        paper[x, y] = True

    first = True
    for f in folds:
        if f[0] == 'x':
            pos = int(f[1])
            left = paper[:, :pos]
            right = paper[:, pos+1:]
            if left.shape[1] > right.shape[1]:
                tmp = np.zeros(left.shape, dtype=int)
                tmp[:, :right.shape[1]] = right
                right = tmp
            elif left.shape[1] < right.shape[1]:
                tmp = np.zeros(right.shape, dtype=int)
                tmp[:, tmp.shape[1]-right.shape[1]:] = left
                left = tmp
            paper = np.logical_or(left, np.fliplr(right))
        elif f[0] == 'y':
            pos = int(f[1])
            top = paper[:pos, :]
            btm = paper[pos+1:, :]
            if top.shape[0] > btm.shape[0]:
                tmp = np.zeros(top.shape, dtype=int)
                tmp[:btm.shape[0], :] = btm
                btm = tmp
            elif top.shape[0] < btm.shape[0]:
                tmp = np.zeros(btm.shape, dtype=int)
                tmp[tmp.shape[0]-top.shape[0]:, :] = top
                top = tmp
            paper = np.logical_or(top, np.flipud(btm))

        if first:
            dots = np.sum(paper[:])
            print(f'{dots} after first fold')
            first = False

    matplotlib.pyplot.imsave('aoc_day13_paper.png', paper)


