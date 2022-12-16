"""
--- Day 15: Beacon Exclusion Zone ---
"""

"""
1) Get input
2) Determine the size of the board
2) Get list of source points
3) get list of Beacon points
for all S:
4) Calculate the MD from S to all B and determine minimum mMD
5) pop B from list
6) draw '#' by calculating the distance between all matrix points and S if MD < mMD and empty
"""

"""
https://calculators-math.com/graphers/point-grapher.html

"""
from scipy.spatial.distance import cityblock


test = '2022/day15/input_test.txt'
data = '2022/day15/input_data.txt'




class Point:
    def __init__(self, x, y):
        self.p = [x,y]

    def __repr__(self):
        return(f'{self.p}')

    def __eq__(self, other):
        return self.p[0] == other.p[0] and self.p[1] == other.p[1]

    def dist(self, other):
        """ Manhattan distance """
        return cityblock(self.p, other.p)

class Board:
    def __init__(self, filename, skip=False):

        self._skip = skip
        self.m = []
        s, b = self.get_input(filename)
        self._source = s
        self._beacon = b
        self.xmin, self.xmax, self.ymin, self.ymax = self.board_dims()
        print(self.xmin, self.xmax, self.ymin, self.ymax)
        self.nrow = self.ymax - self.ymin + 1
        self.ncol = self.xmax - self.xmin + 1
        self.init()


    @staticmethod
    def get_input(filename):
        s_list = []
        b_list = []
        with open(filename) as file:
            for line in file:
                s, b = Board.parse(''.join(line[:-1]))
                s_list.append(s)
                b_list.append(b)
        return s_list, b_list

    @staticmethod
    def parse(line):
        xs, ys = line.split('Sensor at ')[-1].split(':')[0].split(',')
        xb, yb = line.split('is at ')[-1].split(':')[0].split(',')
        s = Point(int(xs.split('=')[-1]), int(ys.split('=')[-1]))
        b = Point(int(xb.split('=')[-1]), int(yb.split('=')[-1]))
        return s, b

    def board_dims(self):
        x = []
        y = []
        for s, b in zip(self._source, self._beacon):
            x.append(s.p[0])
            x.append(b.p[0])
            y.append(s.p[1])
            y.append(b.p[1])

        return min(x), max(x), min(y), max(y)

    def apply_offset(self, points):
        # correct points offset
        for p in points:
            p.p[0] -= self.xmin
            p.p[1] -= self.ymin

    def draw_points(self, points, char):
        for p in points:
            self.m[p.p[1]][p.p[0]] = str(char)

    def init(self):
        if not self._skip:
            for _ in range(self.nrow):
                self.m.append(['.']*(self.ncol))
            print(len(self.m[0]))
            print(len(self.m))

        #self.apply_offset(self._source)
        #self.apply_offset(self._beacon)
        if not self._skip:
            self.draw_points(self._source, 'S')
            self.draw_points(self._beacon, 'B')

    def __repr__(self):
        if not self._skip:
            b = []
            for l in self.m:
                b.append(''.join(l))
            return '\n'.join(b)
        else:
            return 'Visualization not available'

    def scan(self, row):
        if not self._skip:
            for i in range(self.nrow):
                for j in range(self.ncol):
                    if self.m[i][j] not in ['S', 'B', '#']:
                        all_d = []
                        for s, b in zip(self._source,self._beacon):
                            all_d.append(s.dist(Point(j,i)) <= s.dist(b))
                        if any(all_d):
                            self.draw_points([Point(j,i)],'#')
            return self.get_forbidden_positions(row)
        else:
            print('Scan aborted: only allowed with visual board (skip=False)')
            return

    def scan2(self, row):
        count = 0
        y = row
        i_list = []
        sb_list = []
        d_list = []
        seg = []
        # calculate all distances SB
        for s, b in zip(self._source, self._beacon):

            i = Point(s.p[0], y)
            sb = (s.dist(b))
            d = sb - i.dist(s)
            if d >= 0:
                _s = set(range(s.p[0] - d, s.p[0] + d + 1))
                seg.append(_s)
        r = set().union(*seg)

        # remove current Source/Beacons present in row (location is occupied)
        present = 0
        visited = []
        for b in self._beacon:
            if b.p[1] == row and b not in visited:
                visited.append(b)
                present += 1
        visited = []
        for s in self._source:
            if s.p[1] == row and s not in visited:
                visited.append(s)
                present += 1

        return len(r) - present


    def scan3(self):
        sb_list = []
        print('be patient here...')

        # calculate all distances SB
        for s, b in zip(self._source, self._beacon):
            sb = (s.dist(b))
            sb_list.append(sb)

        for s, b, sb in zip(self._source, self._beacon, sb_list):
            for d in range(sb + 2):
                sx = s.p[0]
                sy = s.p[1]
                left_up = (sx - d, sy - sb - 1 + d)
                right_up = (sx + d, sy - sb + d -1)
                left_down = (sx - sb - 1 + d , sy + d)
                right_down = (sx + sb + 1 - d, sy + d)
                for x, y in [left_up, left_down, right_up, right_down]:
                    if not (0<=x<=4_000_000 and 0<=y<=4_000_000):
                        continue
                    if self.check_point(x, y, self._source, sb_list):
                        return 4_000_000 * x + y

    def check_point(self, x, y, sensors, sb):
        for s, d in zip(sensors, sb):
            if s.dist(Point(x, y)) <= d:
                return False
        return True

    def get_forbidden_positions(self, row):
        return self.m[row][:].count('#')


if __name__ == '__main__':

    # Naive attempt for test 1
    # board = Board(test)
    # print(board)
    # result = board.scan(row=10)
    # print('')
    # print(board)
    # print(result)
    # print(board.get_forbidden_positions(10))

    board = Board(test, skip=True)
    result = board.scan2(row=10)
    print(f'Test1: {result}')
    assert result == 26

    board = Board(data, skip=True)
    result = board.scan2(row=2000000)
    print(f'Puzzle1: {result}')
    assert result == 4907780

    result = board.scan3()
    print(f'Puzzle2: {result}')
    assert result == 13639962836448
