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
    with np.errstate(invalid='ignore'):
        unvisit_dist = dist + np.inf*visit
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

if __name__ == '__main__':
    filename = 'aoc_day15_input.txt'

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    cave = np.genfromtxt(filename, delimiter=1, dtype=int)

    start = (0, 0)
    end = (cave.shape[0] - 1, cave.shape[1] - 1)

    min_risk, dist, visit, path = find_min_path(cave, start, end)

    print(f'Path with min risk {min_risk}')
