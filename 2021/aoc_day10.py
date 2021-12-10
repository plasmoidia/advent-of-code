#! python

def check_for_corruption(line):
    chunks = {'(': ')', '[': ']', '{': '}', '<': '>'}
    corrupt = None
    stack = []
    for c in line:
        if c in chunks:
            stack.append(chunks[c])
        else:
            match = stack.pop()
            if c != match:
                corrupt = c
                break
    return corrupt, stack

if __name__ == '__main__':
    filename = 'aoc_day10_input.txt'
    stx_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    cmp_scores = {')': 1, ']': 2, '}': 3, '>': 4}

    stx_score = 0
    cmp_list = []
    with open(filename) as f:
        for line in f:
            c, s = check_for_corruption(line.strip())
            if c in stx_scores:
                stx_score += stx_scores[c]
            else:
                cmp = 0
                s.reverse()
                for match in s:
                    cmp *= 5
                    cmp += cmp_scores[match]
                cmp_list.append(cmp)

    print(f'Syntax error score {stx_score}')

    cmp_list.sort()
    mid_idx = len(cmp_list) // 2
    cmp_score = cmp_list[mid_idx]
    print(f'Auto-complete score {cmp_score}')

