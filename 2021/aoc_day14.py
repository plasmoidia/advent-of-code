#! python

import sys
from collections import Counter

if __name__ == '__main__':
    filename = 'aoc_day14_input.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    with open(filename) as f:
        poly = f.readline().strip()
        inserts = {}
        for l in f:
            line = l.strip()
            if not len(line):
                continue
            key, val = line.split(' -> ')
            inserts[key] = val
    
    steps = 10
    for step in range(steps):
        new_poly = poly[0]
        for c1, c2 in zip(poly[:-1], poly[1:]):
            pair = c1 + c2
            ins = inserts[pair]
            new_poly += ins + c2
        poly = new_poly
        
    cnt = Counter(poly)
    print(cnt)
    res = cnt.most_common()
    diff = res[0][1] - res[-1][1]
    print(f'Found difference of {diff}')
