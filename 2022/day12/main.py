"""
--- Day 12: Hill Climbing Algorithm ---
"""

test = '2022/day12/input_test.txt'
data = '2022/day12/input_data.txt'

def get_map(filename):
    m = []
    with open(filename) as file:
        for line in file:
            a = line[:-1]
            m.append(list(a))
    return m

class Graph:
    def __init__(self, map):
        self._map = map
        self._rows = len(map)
        self._columns = len(map[0])
        # create graph
        self.nodes = {}
        for i in range(self._rows):
            for j in range(self._columns):
                neighbors = []
                if self.can_move_down(i, j):
                    neighbors.append((i+1, j))
                if self.can_move_up(i, j):
                    neighbors.append((i-1,j))
                if self.can_move_right(i, j):
                    neighbors.append((i,j+1))
                if self.can_move_left(i, j):
                    neighbors.append((i,j-1))
                self.nodes[(i, j)] = neighbors

    @staticmethod
    def step(end, start):
        if start == 'S': start = 'a'
        if end == 'E': end = 'z'
        value = ord(end) - ord(start)
        return value

    def in_board(self, i, j):
        return 0 <= i < self._rows and 0 <= j < self._columns

    def can_move_up(self, i, j):
        if not self.in_board(i - 1, j):
            return False
        elif (self.step(self._map[i-1][j], self._map[i][j]) < 2):
            return True
        return False

    def can_move_down(self, i, j):
        if not self.in_board(i + 1, j):
            return False
        elif (self.step(self._map[i+1][j], self._map[i][j]) < 2):
            return True
        return False

    def can_move_left(self, i, j):
        if not self.in_board(i, j-1):
            return False
        elif (self.step(self._map[i][j-1], self._map[i][j]) < 2):
            return True
        return False

    def can_move_right(self, i, j):
        if not self.in_board(i, j + 1):
            return False
        elif (self.step(self._map[i][j+1], self._map[i][j]) < 2):
            return True
        return False


def get_start_end(map):
    rows = len(map)
    columns = len(map[0])

    for i in range(rows):
        for j in range(columns):
            if map[i][j] == 'S': s = (i, j)
            if map[i][j] == 'E': e = (i, j)
    return s, e


def get_all_starts_end(map):
    rows = len(map)
    columns = len(map[0])

    s = []
    for i in range(rows):
        for j in range(columns):
            if map[i][j] == 'a':
                s.append((i, j))
            if map[i][j] == 'E':
                e = (i, j)
    return s, e


def shortest_path(graph, start, end):
    """
    Following is the Breath-First Search algorithm
    """
    path_list = [[start]]
    path_index = 0
    # visited nodes
    previous_nodes = {start}
    if start == end:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search end
        if end in next_nodes:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def puzzle1(file):
    m = get_map(data)
    graph = Graph(m)
    start, end = get_start_end(m)
    path = shortest_path(graph.nodes, start, end)
    print(path)
    print(len(path) - 1)


def puzzle2(file):
    all_length = []
    m = get_map(data)
    starts, end = get_all_starts_end(m)
    for start in starts:
        graph = Graph(m)
        paths_length = len(shortest_path(graph.nodes, start, end))
        if paths_length != 0:
            all_length.append(paths_length)

    print(sorted(all_length)[0] -1)


if __name__ == '__main__':
    puzzle1(test)
    puzzle2(test)
