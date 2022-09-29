# https://open.kattis.com/problems/birthdayboy
import sys
import datetime


class Solver:
    def __init__(self, dates):
        self.dates = sorted(dates, key=lambda tup: (tup[1], tup[0]) )
        print(self.dates)

    def format_result(self, result):
        return result.strftime('%m-%d')

    def solve(self):
        d1, m1 = self.dates[len(self.dates) - 1]
        d2, m2 = self.dates[0]
        diff = self.get_days_diff(d1, m1, d2, m2)
        longest = diff
        dates_with_longest_diff = [(self.dates[len(self.dates) - 1], self.dates[0])]
        print((self.dates[0], self.dates[len(self.dates) - 1]), diff)
        for i in range(1, len(self.dates)):
            d1, m1 = self.dates[i-1]
            d2, m2 = self.dates[i]
            diff = self.get_days_diff(d1, m1, d2, m2)
            print((self.dates[i-1], self.dates[i]), diff)
            if diff > longest:
                dates_with_longest_diff = [(self.dates[i-1], self.dates[i])]
            elif diff == longest:
                dates_with_longest_diff.append((self.dates[i-1], self.dates[i]))
        # TODO pick nearest 27th of October
        d, m = dates_with_longest_diff[0][1]
        return self.get_previous_date(d, m)

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
