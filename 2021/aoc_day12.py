#! python

import sys
import copy as cp

def add_path(cave, n0, n1):
    if n0 not in cave:
        cave[n0] = []
    cave[n0].append(n1)

def small_cave(node):
    return node.islower()

def can_visit(path, node):
    res = False
    small = small_cave(node)
    if not small:
        res = True
    elif node not in path:
        res = True
    return res

def find_path(paths, cave, path, start, end):
    path.append(start)
    if start == end:
        paths.append(cp.deepcopy(path))
    else:
        for node in cave[start]:
            if can_visit(path, node):
                find_path(paths, cave, path, node, end)
    path.pop()

def find_paths(cave, start='start', end='end'):
    paths = []
    path = []
    find_path(paths, cave, path, start, end)
    return paths

if __name__ == '__main__':
    filename = 'aoc_day12_input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as f:
        cave = {}
        for line in f:
            nodes = line.strip().split('-')
            add_path(cave, nodes[0], nodes[1])
            add_path(cave, nodes[1], nodes[0])

    paths = find_paths(cave)
    num = len(paths)
    print(f'Found {num} paths')
