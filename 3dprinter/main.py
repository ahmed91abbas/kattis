# https://open.kattis.com/problems/3dprinter
import sys


class Solver:
    def __init__(self, nbr_statues):
        self.nbr_statues = nbr_statues

    def format_result(self, result):
        return str(result)

    def solve(self):
        if self.nbr_statues < 3:
            return self.format_result(self.nbr_statues)
        else:
            days = 0
            printers = 1
            while printers < self.nbr_statues:
                days += 1
                printers *= 2
            days += 1
            return self.format_result(days)


def run():
    nbr_statues = int(sys.stdin.readline())
    solver = Solver(nbr_statues)
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    run()
