#! python

import numpy as np

class bingo_board(object):
    def __init__(self, size=5):
        self.size = size
        self.board = np.zeros((self.size, self.size), dtype=int)
        self.spaces = np.zeros((self.size, self.size), dtype=bool)
        self.winner = False

    def read(self, f):
        complete = False
        row = 0
        for line in f:
            if not line:
                break
            lnum = line.strip().split()
            if len(lnum) == 0:
                continue
            for col, val in enumerate(lnum):
                self.board[row, col] = val
            row += 1
            if row == self.size:
                complete = True
                break
        return complete

    def won(self):
        result = False
        for row in range(self.size):
            if np.all(self.spaces[row,:]):
                result = True
                break
        for col in range(self.size):
            if np.all(self.spaces[:,col]):
                result = True
                break
        self.winner = result
        return result

    def mark(self, num):
        if self.winner:
            return False
        if num in self.board:
            self.spaces[self.board == num] = True
        return self.won()

    def sum_unmarked(self):
        return np.sum(self.board[np.logical_not(self.spaces)])

def run(boards, numbers):
    first = None
    last = None
    last_w = None
    winner = np.zeros(len(boards), dtype=bool)
    for num in numbers:
        for idx, b in enumerate(boards):
            if b.mark(num):
                if first is None:
                    first = {'num': num, 'board': b}
                winner[idx] = True
                if np.all(winner) and last is None:
                    last = {'num': num, 'board': b}
                last_w = {'num': num, 'board': b}
        if first is not None and last is not None:
            break

    if first is not None:
        s = first['board'].sum_unmarked()
        n = first['num']
        p = n*s
        print(f'First winning board: num {n} sum {s} prod {p}')
    if last is None:
        last = last_w
    if last is not None:
        s = last['board'].sum_unmarked()
        n = last['num']
        p = n*s
        print(f'Last winning board: num {n} sum {s} prod {p}')

if __name__ == '__main__':
    filename = 'aoc_day4_input.txt'

    with open(filename) as f:
        numbers = [int(num) for num in f.readline().split(',')]
        boards = []
        while True:
            board = bingo_board()
            if board.read(f):
                boards.append(board)
            else:
                break

        run(boards, numbers)

