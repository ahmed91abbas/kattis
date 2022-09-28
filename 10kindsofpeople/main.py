# https://open.kattis.com/problems/10kindsofpeople
import sys


class Solver:
    def __init__(self, contents, row_count, column_count):
        self.contents = contents
        self.row_count = row_count
        self.column_count = column_count
        self.connections = self.get_all_connections()

    def get_all_connections(self):
        connections = []
        all = set(range(len(self.contents)))
        while all:
            index = all.pop()
            index_connections = self.get_connections(index)
            all -= index_connections
            connections.append(index_connections)
        return connections

    def get_connections(self, source):
        visited = set()
        stack = list()
        stack.append(source)
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack += self.find_neighbors(vertex, visited)
        return visited

    def find_neighbors(self, index, visited):
        index = int(index)
        current = self.contents[index]
        result = list()
        r = index // self.column_count
        c = index - (self.column_count * r)
        new_index = self.column_count * (r - 1) + c
        if r != 0 and current == self.contents[new_index] and new_index not in visited:
            result.append(new_index)
        new_index = self.column_count * (r + 1) + c
        if r < self.row_count - 1 and current == self.contents[new_index] and new_index not in visited:
            result.append(new_index)
        new_index = self.column_count * r + (c - 1)
        if c != 0 and current == self.contents[new_index] and new_index not in visited:
            result.append(new_index)
        new_index = self.column_count * r + (c + 1)
        if c < self.column_count - 1 and current == self.contents[new_index] and new_index not in visited:
            result.append(new_index)
        return result

    def format_result(self, result):
        return '\n'.join(result)

    def solve(self, source, target):
        if self.contents[source] != self.contents[target]:
            return 'neither'
        self.skip = set()
        result_type = ''
        if self.contents[source] == '0':
            result_type = 'binary'
        else:
            result_type = 'decimal'
        path_exist = False
        for group in self.connections:
            if source in group and target in group:
                path_exist = True
                break
        if path_exist:
            return result_type
        else:
            return 'neither'


def run():
    lines = sys.stdin.read().split('\n')
    r, c = map(int, lines[0].split(' '))
    contents = ''.join(lines[1:r+1])
    n = int(lines[r+1])
    locations = [loc.split(' ') for loc in lines[r+2:r+2+n]]
    solver = Solver(contents, r, c)
    results = []
    for loc in locations:
        source = c * (int(loc[0])-1) + (int(loc[1])-1)
        target = c * (int(loc[2])-1) + (int(loc[3])-1)
        results.append(solver.solve(source, target))
    return solver.format_result(results)


if __name__=='__main__':
    print(run())
