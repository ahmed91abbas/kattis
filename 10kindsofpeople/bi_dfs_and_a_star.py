# https://open.kattis.com/problems/10kindsofpeople
import sys
import heapq


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

    def a_star(self, start_node, end_node):
        f_distance = {node:float('inf') for node in range(len(self.contents))}
        f_distance[start_node] = 0

        g_distance = {node:float('inf') for node in range(len(self.contents))}
        g_distance[start_node] = 0

        came_from = {node:None for node in range(len(self.contents))}
        came_from[start_node] = start_node

        queue = [(0,start_node)]
        while queue:
            current_f_distance, current_node = heapq.heappop(queue)
            if current_node == end_node:
                return True
            neighbors = self.find_neighbors(current_node)
            for next_node in neighbors:
                temp_g_distance = g_distance[current_node] + 1
                if temp_g_distance < g_distance[next_node]:
                    g_distance[next_node] = temp_g_distance
                    heuristic = self.get_heuristic(next_node, end_node)
                    f_distance[next_node] = temp_g_distance + heuristic
                    came_from[next_node] = current_node
                    heapq.heappush(queue,(f_distance[next_node], next_node))
        return False

    def get_row_col(self, index):
        r = index // self.column_count
        c = index - (self.column_count * r)
        return r, c

    def get_heuristic(self, source, target):
        r1 = source // self.column_count
        c1 = source - (self.column_count * r1)
        r2 = target // self.column_count
        c2 = target - (self.column_count * r2)
        return abs(r1 - r2) + abs(c1 - c2)

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
        r1, c1 = self.get_row_col(source)
        r2, c2 = self.get_row_col(target)
        use_a_star = abs(r1 - r2) < self.row_count / 2 and abs(c1 - c2) > self.row_count / 3
        if use_a_star:
            path_exist = self.a_star(source, target)
        else:
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
