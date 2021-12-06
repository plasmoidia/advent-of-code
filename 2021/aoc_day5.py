#! python

import numpy as np

def draw_line(img, pt1, pt2):
    if pt1[0] == pt2[0]: # horizontal line
        col = pt1[0]
        start = min(pt1[1], pt2[1])
        end = max(pt1[1], pt2[1])+1
        for row in range(start, end):
            img[row, col] += 1
    elif pt1[1] == pt2[1]: # vertical line
        row = pt1[1]
        start = min(pt1[0], pt2[0])
        end = max(pt1[0], pt2[0])+1
        for col in range(start, end):
            img[row, col] += 1

def draw_diag_line(img, pt1, pt2):
    if pt1[0] != pt2[0] and pt1[1] != pt2[1]:
        (cs, ce) = (pt1[0], pt2[0])
        (rs, re) = (pt1[1], pt2[1])
        if rs > re:
            rstep = -1
            re -= 1
        else:
            rstep = 1
            re += 1
        if cs > ce:
            cstep = -1
            ce -=1
        else:
            cstep = 1
            ce += 1
        for row, col in zip(range(rs, re, rstep), range(cs, ce, cstep)):
            img[row, col] += 1

if __name__ == '__main__':
    filename = 'aoc_day5_input.txt'
    with open(filename) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    l_pts = np.zeros((len(lines), 4), dtype=int)
    for row, l in enumerate(lines):
        (pt1, pt2) = l.split(' -> ')
        l_pts[row,:2] = [int(a) for a in pt1.split(',')]
        l_pts[row,2:] = [int(a) for a in pt2.split(',')]

    sz = np.max(l_pts[:])+1
    img = np.zeros((sz, sz), dtype=int)

    for l in l_pts:
        draw_line(img, l[:2], l[2:])

    num = np.sum(img >= 2)
    print(f'Found {num} points')

    for l in l_pts:
        draw_diag_line(img, l[:2], l[2:])

    num = np.sum(img >= 2)
    print(f'Found {num} points')

