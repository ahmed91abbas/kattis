# https://open.kattis.com/problems/birthdayboy
import sys
import datetime


class Solver:
    def __init__(self, dates):
        self.dates = sorted(dates, key=lambda tup: (tup[1], tup[0]))

    def format_result(self, result):
        return result.strftime('%m-%d')

    def solve(self):
        d1, m1 = self.dates[len(self.dates) - 1]
        d2, m2 = self.dates[0]
        diff = self.get_days_diff(d1, m1, d2, m2)
        longest = diff
        dates_with_longest_diff = [(self.dates[len(self.dates) - 1], self.dates[0])]
        # print((self.dates[len(self.dates) - 1], self.dates[0]), diff)
        for i in range(1, len(self.dates)):
            date1 = self.dates[i-1]
            date2 = self.dates[i]
            diff = self.get_days_diff(date1[0], date1[1], date2[0], date2[1])
            # print(date1, date2, diff)
            if diff > longest:
                dates_with_longest_diff = [(date1, date2)]
                longest = diff
            elif diff == longest:
                dates_with_longest_diff.append((date1, date2))
        shortest_diff_to_27_oct = 365
        # print(dates_with_longest_diff)
        ans_d, ans_m = dates_with_longest_diff[0][1]
        for date in dates_with_longest_diff:
            should_compare = sorted(date, key=lambda tup: (tup[1], tup[0]))[0] == date[0]
            diff = 400
            for tuple in reversed(date):
                d, m = tuple
                prev = self.get_previous_date(d, m)
                if tuple != (28, 10) and (prev.day, prev.month) not in self.dates:
                    diff = self.get_days_diff(27, 10, d, m)
                    break
            if diff <= shortest_diff_to_27_oct and should_compare:
                shortest_diff_to_27_oct = diff
                ans_d = d
                ans_m = m
        return self.get_previous_date(ans_d, ans_m)

    def get_days_diff(self, d1, m1, d2, m2):
        year = 2022
        d1 = datetime.date(year, m1, d1)
        d2 = datetime.date(year, m2, d2)
        delta = d2 - d1
        return delta.days if delta.days >= 0 else 365 + delta.days

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
