# https://open.kattis.com/problems/10kindsofpeople
import sys
import os


class Solver:
    def __init__(self, data):
        self.data = data

    def format_result(self, result):
        return '\n'.join(result)

    def solve(self):
        return list(reversed(self.data))


def run():
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    solver = Solver(lines)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    run()
