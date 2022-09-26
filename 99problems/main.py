# https://open.kattis.com/problems/99problems
import sys


class Solver:
    def __init__(self, price):
        self.price = price

    def format_result(self, result):
        return str(result)

    def solve(self):
        if self.price < 100:
            return self.format_result(99)
        else:
            after_second_digit = int(str(self.price)[:-2])
            above = int(f'{after_second_digit}99')
            below = int(f'{after_second_digit - 1}99')
            ans = above if abs(self.price - above) <= abs(self.price - below) else below
            return self.format_result(ans)


def run():
    price = int(sys.stdin.readline())
    solver = Solver(price)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    run()
