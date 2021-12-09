#! python

if __name__ == '__main__':
    filename = 'aoc_day8_input.txt'

    num_1478 = 0
    total = 0
    with open(filename) as f:
        for line in f:
            (sigs, outs) = line.split('|')
            sigs = sigs.strip().split()
            outs = outs.strip().split()

            display = {}
            sigs_left = []
            for s in sigs:
                l = len(s)
                if l == 2: # 1
                    display[1] = s
                elif l == 4: # 4
                    display[4] = s
                elif l == 3: # 7
                    display[7] = s
                elif l == 7: # 8
                    display[8] = s
                else:
                    sigs_left.append(s)

            # found 1, 4, 7, 8; left 0, 2, 3, 5, 6, 9
            sigs = sigs_left
            sigs_left = []
            for s in sigs:
                l = len(s)
                if l == 5: # 2, 3, 5
                    if all([c in s for c in display[1]]): # 3
                        display[3] = s
                    else:
                        sigs_left.append(s)
                elif l == 6: # 0, 6, 9
                    if all([c in s for c in display[4]]): # 9
                        display[9] = s
                    else:
                        sigs_left.append(s)

            # found 1, 3, 4, 7, 8, 9; left 0, 2, 5, 6
            sigs = sigs_left
            for s in sigs:
                l = len(s)
                if l == 5: # 2, 5
                    if all([c in display[9] for c in s]): # 5
                        display[5] = s
                    else:
                        display[2] = s
                elif l == 6: # 0, 6
                    if all([c in s for c in display[1]]): # 0
                        display[0] = s
                    else:
                        display[6] = s

            value = 0
            place = 1000
            for out in outs:
                for d in display:
                    if set(out) == set(display[d]):
                        digit = d
                        break
                value += digit * place
                place = place // 10

                if digit == 1 or digit == 4 or digit == 7 or digit == 8:
                    num_1478 += 1

            total += value

    print(f'Found {num_1478} instances of 1, 4, 7, 8')
    print(f'Total of outputs {total}')
