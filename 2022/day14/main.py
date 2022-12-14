"""
--- Day 14: Regolith Reservoir ---
"""

test = '2022/day14/input_test.txt'
data = '2022/day14/input_data.txt'
test2 = '2022/day14/tmp.txt'

def get_input(filename):
    rocks = []
    with open(filename) as file:
        for line in file:
            rocks.append(Rock(line))
    return rocks

def get_segments(rock):
    s = []
    for i in range(len(rock.vertexes) - 1):
        s.append(Segment(rock.vertexes[i], rock.vertexes[i+1]))
    return(s)


class Board:
    def __init__(self, rock_list, extra_rows_bottom=0, extra_cols=0):
        row_min_list = []
        row_max_list = []
        col_min_list = []
        col_max_list = []
        self.m = []

        # search board limits
        for rock in rock_list:
            _rock_rows = [vertex[0] for vertex in rock.vertexes]
            row_min_list.append(min(_rock_rows))
            row_max_list.append(max(_rock_rows))
            _rock_cols = [vertex[1] for vertex in rock.vertexes]
            col_min_list.append(min(_rock_cols))
            col_max_list.append(max(_rock_cols))

        self.col_min = 0#min(col_min_list)
        self.col_max = max(col_max_list)
        self.row_min = min(row_min_list)
        self.row_max = max(row_max_list)

        self.init_board(extra_rows_bottom, extra_cols)

    def init_board(self, extra_rows_bottom, extra_cols):
        self.col_max += extra_rows_bottom
        self.row_min -= extra_cols
        self.row_max += extra_cols
        # print(self.row_min, self.row_max, self.col_min, self.col_max)

        self.ncol = self.row_max-self.row_min + 1
        self.nrow = self.col_max-self.col_min + 1

        for r in range(self.nrow):
            if extra_rows_bottom != 0:
                if r < self.nrow - 1:
                    self.m.append(['.']*(self.ncol))
                else:
                    self.m.append(['#']*(self.ncol))
            else:
                self.m.append(['.']*(self.ncol))

    def __repr__(self):
        b = []
        for l in self.m:
            b.append(''.join(l))
        return '\n'.join(b)

    def scale_coef(self):
        return (self.row_min, self.col_min)

    def draw_segment(self, segment):
        if segment.dx != 0:
            row = segment.p0[1]
            for _x in range(segment.dx + 1):
                x = segment.p0[0] + _x
                self.m[row][x] = '#'
        if segment.dy != 0:
            col = segment.p0[0]
            for _y in range(segment.dy + 1):
                y = segment.p0[1] + _y
                self.m[y][col] = '#'

class Rock:
    def __init__(self, line):
        self.vertexes = [[int(a), int(b)] for a, b in [x.split(',') for x in line[:-1].split(' -> ')]]

    def scale(self, x_min, y_min):
        for pos in self.vertexes:
            pos[0] -= x_min
            pos[1] -= y_min

    def __repr__(self):
        return str(self.vertexes)

class Segment:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.dx = p1[0] - p0[0]
        self.dy = p1[1] - p0[1]

        # correct segment orientation
        if self.dx < 0:
            self.dx *= -1
            self.p0 = p1
            self.p1 = p0

        if self.dy < 0:
            self.dy *= -1
            self.p0 = p1
            self.p1 = p0

    def __repr__(self):
        return(f'({self.p0}, {self.p1}, {self.dx}, {self.dy})')


def drop_sand(board, row, col):
    stop = False
    board.m[row][col] = '+'
    row = row + 1
    col = col

    while not stop:
        try:
            current = board.m[row-1][col]
            next = board.m[row][col]
            next_left = board.m[row][col-1]
            next_right = board.m[row][col+1]
        except IndexError:
            return True, 0
        if next == '.':
            row +=1
        elif (next == 'o' or next == '#') and next_left == '.':
            col -= 1
            row += 1
        elif (next == 'o' or next == '#') and next_right == '.':
            col += 1
            row += 1
        elif next == next_left == next_right == 'o' and current == '+':
            return True, 1
        else:
            board.m[row-1][col] = 'o'
            stop=True
    return False, 0


def puzzle(file, extra_rows_bottom=0, extra_cols=0):
    rocks = get_input(file)
    board = Board(rocks, extra_rows_bottom, extra_cols)

    # Fill board with rocks
    for rock in rocks:
        rock.scale(*board.scale_coef())
        segments= get_segments(rock)
        for segment in segments:
            board.draw_segment(segment)

    nsand = -1
    stop = False
    start = [0,500]
    start[0] -= board.scale_coef()[1]
    start[1] -= board.scale_coef()[0]

    while not stop:
        # print(board)
        nsand += 1
        stop, last = drop_sand(board, *start)
        nsand += last  # last sand on puzzle 2

#    print(board)
    print(nsand)

if __name__ == '__main__':
    puzzle(test)
    puzzle(data)
    puzzle(test, 2, 200)
    puzzle(data, 2, 200)
