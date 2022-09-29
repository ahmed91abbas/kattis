# https://open.kattis.com/problems/birthdayboy
import sys
import datetime


class Solver:
    def __init__(self, dates):
        self.dates = sorted(dates, key=lambda tup: (tup[1], tup[0]) )

    def format_result(self, result):
        return result.strftime('%m-%d')

    def solve(self):
        d1, m1 = self.dates[len(self.dates) - 1]
        d2, m2 = self.dates[0]
        diff = self.get_days_diff(d1, m1, d2, m2)
        longest = diff
        dates_with_longest_diff = [(self.dates[len(self.dates) - 1], self.dates[0])]
        for i in range(1, len(self.dates)):
            d1, m1 = self.dates[i-1]
            d2, m2 = self.dates[i]
            diff = self.get_days_diff(d1, m1, d2, m2)
            if diff > longest:
                dates_with_longest_diff = [(self.dates[i-1], self.dates[i])]
                longest = diff
            elif diff == longest:
                dates_with_longest_diff.append((self.dates[i-1], self.dates[i]))
        shortest_diff_to_27_oct = 356
        ans_d = ans_m = None
        for date in dates_with_longest_diff:
            d, m = date[1]
            diff =self.get_days_diff(27, 10, d, m)
            if diff < shortest_diff_to_27_oct and date[1] != (28, 10):
                shortest_diff_to_27_oct = diff
                ans_d = d
                ans_m = m
        return self.get_previous_date(ans_d, ans_m)

    def get_days_diff(self, d1, m1, d2, m2):
        year1 = 2022
        year2 = year1 if m1 <= m2 else year1 + 1
        d1 = datetime.date(year1, m1, d1)
        d2 = datetime.date(year2, m2, d2)
        delta = d2 - d1
        return abs(delta.days)

    def get_previous_date(self, d, m):
        current = datetime.date(2022, m, d)
        return current - datetime.timedelta(days=1)


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
