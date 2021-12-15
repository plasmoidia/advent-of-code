#! python

import sys
from collections import Counter

def get_element_counts(poly_cnt):
    cnt = Counter()
    for pair in poly_cnt:
        count = poly_cnt[pair]
        for c in pair:
            cnt[c] += count

    # de-duplicate counts
    for elem in cnt:
        cnt[elem] = (cnt[elem] + 1) // 2

    return cnt

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

    pairs = iter(c1 + c2 for c1, c2 in zip(poly[:-1], poly[1:]))
    poly_cnt = Counter(pairs)

    steps = 40
    for step in range(steps):
        if step == 10:
            cnt10 = get_element_counts(poly_cnt)
        new_poly = Counter()
        for pair in poly_cnt:
            count = poly_cnt[pair]
            ins = inserts[pair]
            pair_a = pair[0] + ins
            pair_b = ins + pair[1]
            new_poly[pair_a] += count
            new_poly[pair_b] += count
        poly_cnt = new_poly

    cnt = get_element_counts(poly_cnt)

    res10 = cnt10.most_common()
    res = cnt.most_common()
    diff10 = res10[0][1] - res10[-1][1]
    diff = res[0][1] - res[-1][1]
    print(f'Found difference of {diff10} after 10 steps')
    print(f'Found difference of {diff} after {steps} steps')
