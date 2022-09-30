# https://open.kattis.com/problems/birthdayboy
import sys
import datetime


class Solver:
    def __init__(self, dates):
        self.dates = sorted(dates, key=lambda tup: (tup[1], tup[0]))

    def format_result(self, result):
        return result.strftime('%m-%d')

    def consider_current_date(self, date1, date2):
        dates = [date1, date2, (27, 10)]
        dates = sorted(dates, key=lambda tup: (tup[1], tup[0]))
        in_middle = dates[1] == (27, 10)
        if in_middle:
            diff1 = self.get_days_diff(date1[0], date1[1], 27, 10)
            diff2 = self.get_days_diff(27, 10, date2[0], date2[1])
            if diff1 > diff2:
                return (date1, (27, 10))
            else:
                return ((27, 10), date2)
        return (date1, date2)

    def solve(self):
        d1, m1 = self.dates[len(self.dates) - 1]
        d2, m2 = self.dates[0]
        diff = self.get_days_diff(d1, m1, d2, m2)
        longest = diff
        dates_with_longest_diff = [(self.dates[len(self.dates) - 1], self.dates[0])]
        for i in range(1, len(self.dates)):
            date1 = self.dates[i-1]
            date2 = self.dates[i]
            date1, date2 = self.consider_current_date(date1, date2)
            diff = self.get_days_diff(date1[0], date1[1], date2[0], date2[1])
            if diff > longest:
                dates_with_longest_diff = [(date1, date2)]
                longest = diff
            elif diff == longest:
                dates_with_longest_diff.append((date1, date2))
        shortest_diff_to_27_oct = 365
        ans_d, ans_m = dates_with_longest_diff[0][0]
        for date in dates_with_longest_diff:
            date = sorted(date, key=lambda tup: (tup[1], tup[0]))
            d, m = date[1] if date[1] != (28, 10) else date[0]
            diff =self.get_days_diff(27, 10, d, m)
            if diff <= shortest_diff_to_27_oct:
                shortest_diff_to_27_oct = diff
                ans_d = d
                ans_m = m
        return self.get_previous_date(ans_d, ans_m)

    def get_days_diff(self, d1, m1, d2, m2):
        year1 = 2022
        # TODO consider day?
        year2 = year1 if m1 <= m2 else year1 + 1
        d1 = datetime.date(year1, m1, d1)
        d2 = datetime.date(year2, m2, d2)
        delta = d2 - d1
        return delta.days

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
