# https://open.kattis.com/problems/2048
import sys


class Solver:
    def __init__(self, puzzle, move):
        self.puzzle = puzzle
        self.move = move

    def move_left(self, row):
        index = 0
        tainted_indexes = []
        while index < 3:
            pairs = [[row[i], row[i + 1]] for i in range(len(row) - 1)]
            x, y = pairs[index]
            if x == 0 and y > 0:
                row[index] = y
                row[index+1] = x
                index = 0
            elif x > 0 and x == y and index not in tainted_indexes and index + 1 not in tainted_indexes:
                row[index] = x + y
                row[index+1] = 0
                tainted_indexes.append(index)
                index = 0
            else:
                index += 1
        return row

    def rotate_puzzle(self, puzzle):
        return [list(x) for x in list(zip(*puzzle[::-1]))]

    def format_result(self, result):
        return '\n'.join([' '.join(map(str, x)) for x in result])

    def solve(self):
        new_puzzle = []
        if self.move == 0:
            for i in range(4):
                new_puzzle.append(self.move_left(self.puzzle[i]))
        if self.move == 1:
            self.puzzle = self.rotate_puzzle(self.puzzle)
            for i in range(4):
                new_row = self.move_left(list(reversed(self.puzzle[i])))
                new_puzzle.append(list(reversed(new_row)))
            new_puzzle = self.rotate_puzzle(new_puzzle)
            new_puzzle = self.rotate_puzzle(new_puzzle)
            new_puzzle = self.rotate_puzzle(new_puzzle)
        if self.move == 2:
            for i in range(4):
                new_row = self.move_left(list(reversed(self.puzzle[i])))
                new_puzzle.append(list(reversed(new_row)))
        if self.move == 3:
            self.puzzle = self.rotate_puzzle(self.puzzle)
            for i in range(4):
                new_puzzle.append(self.move_left(self.puzzle[i]))
            new_puzzle = self.rotate_puzzle(new_puzzle)
            new_puzzle = self.rotate_puzzle(new_puzzle)
            new_puzzle = self.rotate_puzzle(new_puzzle)
        return new_puzzle


def run():
    puzzle = [[int(x) for x in sys.stdin.readline().rstrip().split(' ')] for _ in range(4)]
    move = int(sys.stdin.readline().rstrip())
    solver = Solver(puzzle, move)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    print(run())
