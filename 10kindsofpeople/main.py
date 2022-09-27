# https://open.kattis.com/problems/10kindsofpeople
import sys


class Solver:
    def __init__(self, contents, row_count, column_count):
        self.contents = contents
        self.row_count = row_count
        self.column_count = column_count
        self.neighbors = dict()

    def bi_dfs(self, source, target):
        visited = set()
        stack = []
        stack.append(source)
        backward_visited = set()
        backward_stack = []
        backward_stack.append(target)
        while stack and backward_stack:
            vertex = stack.pop()
            backward_vertex = backward_stack.pop()
            if vertex == target or backward_vertex == source or vertex == backward_vertex:
                return True
            if vertex not in visited:
                visited.add(vertex)
                for i in self.find_neighbors(vertex):
                    stack.append(i)
            if backward_vertex not in backward_visited:
                backward_visited.add(backward_vertex)
                for j in self.find_neighbors(backward_vertex):
                    backward_stack.append(j)

    def find_neighbors(self, index):
        if index in self.neighbors:
            return self.neighbors[index]
        result = set()
        r = index // self.column_count
        c = index - (self.column_count * r)
        indices = []
        if r != 0:
            indices.append(self.column_count * (r - 1) + c)
        if r < self.row_count - 1:
            indices.append(self.column_count * (r + 1) + c)
        if c != 0:
            indices.append(self.column_count * r + (c - 1))
        if c < self.column_count - 1:
            indices.append(self.column_count * r + (c + 1))
        for i in indices:
            if self.contents[index] == self.contents[i]:
                result.add(i)
        self.neighbors[index] = result
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
        path_exist = self.bi_dfs(source, target)
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
