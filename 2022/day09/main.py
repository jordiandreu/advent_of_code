"""
--- Day 9: Rope Bridge ---
"""
from itertools import product

test = '2022/day09/input_test.txt'
test_2 = '2022/day09/input_test_2.txt'
data = '2022/day09/input_data.txt'


def get_operations_list(filename):
    operations = []
    with open(filename) as file:
        for line in file:
            o, t = line.split(' ')
            operations.extend([o]*int(t))
    return operations


move = {'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
        }

def move_h(op, h_pos):
    dx0, dx1 = move[op]
    nh0, nh1 = h_pos[0] + dx0, h_pos[1] + dx1
    return nh0, nh1


def move_t(h_pos, t_pos):
    x0 = h_pos[0] - t_pos[0]
    x1 = h_pos[1] - t_pos[1]

    dx0 = 0
    dx1 = 0

    no_move = list(product([0,1,-1], repeat=2))
    if (x0, x1) in no_move:
        pass

    elif (x0, x1) == (0, 2):
        dx0, dx1 = 0, 1
    elif (x0, x1) == (0, -2):
        dx0, dx1 = 0, - 1
    elif (x0, x1) == (2, 0):
        dx0, dx1 = 1, 0
    elif (x0, x1) == (-2, 0):
        dx0, dx1 = - 1, 0

    elif (x0, x1) == (1, 2):
        dx0, dx1 = 1, 1
    elif (x0, x1) == (2, 1):
        dx0, dx1 = 1, 1
    elif (x0, x1) == (-1, -2):
        dx0, dx1 = -1, -1
    elif (x0, x1) == (-2, -1):
        dx0, dx1 = -1, -1
    elif (x0, x1) == (-1, 2):
        dx0, dx1 = -1, 1
    elif (x0, x1) == (2, -1):
        dx0, dx1 = 1, -1
    elif (x0, x1) == (1, -2):
        dx0, dx1 = 1, -1
    elif (x0, x1) == (-2, 1):
        dx0, dx1 = -1, 1

    elif (x0, x1) == (-2, -2):
        dx0, dx1 = -1, -1
    elif (x0, x1) == (2, 2):
        dx0, dx1 = 1, 1
    elif (x0, x1) == (-2, 2):
        dx0, dx1 = -1, 1
    elif (x0, x1) == (2, -2):
        dx0, dx1 = 1, -1
    else:
        raise Exception(f'x0: {x0}, x1: {x1}')

    nx0, nx1 = t_pos[0] + dx0, t_pos[1] + dx1
    return nx0, nx1


def count(matrix):
    m, n = len(matrix), len(matrix[0])
    total = 0
    for i in range(0,m):
        for j in range(0, n):
            if matrix[i][j] == 'X':
                total += 1
    return total


def pprint(matrix):
    for e in matrix:
        print(f'{e}\n')


def snake(file, num_tails):

    matrix = [ [0] * 500 for _ in range(500)]
    matrix[50][0] = 's'
    h_pos = (50, 0)
    t_pos = [(50, 0)] * num_tails

    # Uncomment the commented lines to print the board
    for op in get_operations_list(file):
        # matrix[h_pos[0]][h_pos[1]] = 0
        h_pos = move_h(op, h_pos)
        # matrix[h_pos[0]][h_pos[1]] = 'H'
        # matrix[t_pos[0][0]][t_pos[0][1]] = 0
        t_pos[0] = move_t(h_pos, t_pos[0])
        # matrix[t_pos[0][0]][t_pos[0][1]] = 1

        for i in range(1,num_tails):
            # matrix[t_pos[i][0]][t_pos[i][1]] = 0
            t_pos[i] = move_t(t_pos[i-1], t_pos[i])
            # matrix[t_pos[i][0]][t_pos[i][1]] = i+1

        # pprint(matrix)
        matrix[t_pos[-1][0]][t_pos[-1][1]] = 'X'  # Comment this line to print the board

    print(count(matrix))


if __name__ == '__main__':

    snake(test, 1)
    snake(test_2, 9)
    snake(data, 9)
