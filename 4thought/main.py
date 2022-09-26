# https://open.kattis.com/problems/4thought
import sys


class Solver:
    def __init__(self, data):
        self.data = data
        self.db = self.get_all_combinations()

    def get_all_combinations(self):
        combinations = []
        db = dict()
        ops = ['+', '-', '*', '//']
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    combinations.append([ops[x], ops[y], ops[z]])
        for op in combinations:
            expression = f"4{'4'.join(op)}4"
            result = str(self.eval_expression(expression))
            db[result] = expression
        return db

    def eval_expression(self, expression):
        return eval(expression)

    def format_result(self, result):
        formatted = []
        for x in result:
            if type(x) == str:
                formatted.append(x)
            else:
                res, ob  = x
                formatted.append(f"{ob.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('//', ' / ')} = {res}")
        return '\n'.join(formatted)

    def solve(self):
        result = []
        for n in self.data:
            if n in self.db:
                result.append((n, self.db[n]))
            else:
                result.append('no solution')
        return result


def run():
    lines = [x.rstrip() for x in sys.stdin.readlines()]
    solver = Solver(lines[1:])
    solver.get_all_combinations()
    result = solver.solve()
    return solver.format_result(result)


if __name__=='__main__':
    print(run())
