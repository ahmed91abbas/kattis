# https://open.kattis.com/problems/different
import sys


class Solver:
    def __init__(self, data):
        self.data = data

    def format_result(self, result):
        return '\n'.join(result)

    def solve(self):
        result = []
        for x in self.data:
            a, b = [int(x) for x in x.rstrip().split(' ')]
            result.append(str(abs(a-b)))
        return result


def run():
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    solver = Solver(lines)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    run()
