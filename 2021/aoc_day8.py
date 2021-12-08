#! python

if __name__ == '__main__':
    filename = 'aoc_day8_input.txt'

    num = 0
    with open(filename) as f:
        for line in f:
            (sigs, outs) = line.strip().split('|')
            for out in outs.split():
                l = len(out)
                if l == 2: # 1
                    num += 1
                elif l == 4: # 4
                    num += 1
                elif l == 3: # 7
                    num += 1
                elif l == 7: # 8
                    num += 1

    print(f'Found {num} instances of 1, 4, 7, 8')
