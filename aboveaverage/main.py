# https://open.kattis.com/problems/aboveaverage
import sys


class Solver:
    def __init__(self, data):
        self.data = data

    def format_result(self, result):
        return '\n'.join([f'{x:.3f}%' for x in result])

    def solve(self):
        result = []
        for line in self.data:
            grades = [int(x) for x in line.rstrip().split(' ')][1:]
            average = sum(grades)/len(grades)
            above_average_count = len([x for x in grades if x > average])
            ans = above_average_count/len(grades)*100
            result.append(ans)
        return result


def run():
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    solver = Solver(lines[1:])
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    run()
