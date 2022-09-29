# https://open.kattis.com/problems/birthdayboy
import sys
from datetime import date


class Solver:
    def __init__(self, dates):
        self.dates = dates

    def format_result(self, result):
        return result

    def solve(self):
        d0, m0 = (19, 9)
        d1, m1 = self.dates[0]
        d2, m2 = self.dates[1]
        d3, m3 = self.dates[2]
        d = self.get_days_diff(d0, m0, d1, m1)
        print(d)
        d = self.get_days_diff(d0, m0, d2, m2)
        print(d)
        d = self.get_days_diff(d0, m0, d3, m3)
        print(d)

    def get_days_diff(self, d1, m1, d2, m2):
        d1 = date(2022, m1, d1)
        d2 = date(2022, m2, d2)
        delta = d2 - d1
        return abs(delta.days)


def run():
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    dates = []
    for line in lines[1:]:
        m, d = line.split(' ')[1].split('-')
        dates.append((int(d), int(m)))
    solver = Solver(dates)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    print(run())
