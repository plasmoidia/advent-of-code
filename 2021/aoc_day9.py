#! python

import numpy as np

def flood_fill(img, start, count=0):
    up = (start[0]-1, start[1])
    down = (start[0]+1, start[1])
    left = (start[0], start[1]-1)
    right = (start[0], start[1]+1)
    img[start] = False
    count += 1
    if not img[up] and not img[down] and not img[left] and not img[right]:
        return count
    if img[up]:
        count = flood_fill(img, up, count)
    if img[down]:
        count = flood_fill(img, down, count)
    if img[left]:
        count = flood_fill(img, left, count)
    if img[right]:
        count = flood_fill(img, right, count)
    return count

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
    num = len(minima)
    total = np.sum(minima) + num

    print(f'Found {num} minima with total {total} risk')

    sz = padded.shape
    rows = np.repeat([np.arange(sz[0], dtype=int)], sz[1], axis=0).transpose()
    cols = np.repeat([np.arange(sz[1], dtype=int)], sz[0], axis=0)
    minima_pts = zip(rows[minima_loc], cols[minima_loc])

    basins = padded < 9
    basin_szs = np.zeros(num, dtype=int)
    for basin, pt in enumerate(minima_pts):
        basin_szs[basin] = flood_fill(basins, pt)

    basin_szs.sort()
    big_three = basin_szs[-3:]
    product = np.prod(big_three)

    sz_str = ', '.join([str(s) for s in big_three])
    print(f'Found largest three basins {sz_str} with product {product}')

