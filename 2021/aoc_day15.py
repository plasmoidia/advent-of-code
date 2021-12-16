#! python

import sys
import numpy as np

def neighbor_locs(cave, point):
    locs = []
    if point[0] > 0:
        locs.append((point[0]-1, point[1])) # up
    if point[1] > 0:
        locs.append((point[0], point[1]-1)) # left
    if point[0] < cave.shape[0]-1:
        locs.append((point[0]+1, point[1])) # down
    if point[1] < cave.shape[1]-1:
        locs.append((point[0], point[1]+1)) # right
    return locs

def min_dist(dist, visit):
    unvisit_dist = dist.copy()
    unvisit_dist[visit] = np.inf
    return np.unravel_index(unvisit_dist.argmin(), dist.shape)

def find_min_path(cave, start, end):
    prev_points = {}
    visit = np.zeros(cave.shape, dtype=bool)
    visit[start] = True
    dist = np.ones(cave.shape) * np.inf
    dist[start] = 0

    u = start
    while u != end:
        ns = neighbor_locs(cave, u)
        for n in ns:
            n_dist = dist[u] + cave[n]
            if not visit[n] and n_dist < dist[n]:
                dist[n] = n_dist
                prev_points[n] = u

        u = min_dist(dist, visit)
        visit[u] = True

    path = []
    prev = end
    while prev != start:
        path.append(prev)
        prev = prev_points[prev]
    path.append(start)
    path.reverse()

    return int(dist[u]), dist, visit, path

def increment(cave):
    new_cave = cave + 1
    new_cave[new_cave > 9] = 1
    return new_cave

def ceate_full_map(cave, factor=5):
    sz = cave.shape
    big_cave = np.empty((sz[0]*factor, sz[1]*factor), dtype=cave.dtype)
    for shift in range(factor):
        for row in range(shift+1):
            col = shift - row
            r0 = sz[0] * row
            c0 = sz[1] * col
            r1 = r0 + sz[0]
            c1 = c0 + sz[1]
            big_cave[r0:r1, c0:c1] = cave
        cave = increment(cave)
    for shift in range(factor, 2*factor-1):
        sr = shift - factor + 1
        er = factor
        for row in range(sr, er):
            col = shift - row
            r0 = sz[0] * row
            c0 = sz[1] * col
            r1 = r0 + sz[0]
            c1 = c0 + sz[1]
            big_cave[r0:r1, c0:c1] = cave
        cave = increment(cave)
    return big_cave

if __name__ == '__main__':
    filename = 'aoc_day15_input.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    cave = np.genfromtxt(filename, delimiter=1, dtype=int)

    start = (0, 0)
    end = (cave.shape[0] - 1, cave.shape[1] - 1)

    min_risk, dist, visit, path = find_min_path(cave, start, end)
    print(f'Path with min risk {min_risk}')

    big_cave = ceate_full_map(cave)
    end = (big_cave.shape[0] - 1, big_cave.shape[1] - 1)
    min_risk, dist, visit, path = find_min_path(big_cave, start, end)
    print(f'Path with min risk {min_risk}')
