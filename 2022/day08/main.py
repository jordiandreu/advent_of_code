"""
--- Day 8: Treetop Tree House ---
"""

test = '2022/day08/input_test.txt'
data = '2022/day08/input_data.txt'


def get_matrix(filename):
    matrix = []
    with open(filename) as file:
        values = file.read().split('\n')
        for v in values:
            matrix.append(list(map(int, v)))
    return matrix


def get_tree_shape(tree):
    return len(tree), len(tree[0])


def from_top(i, j, tree):
    for ii in range(0, i):
        if tree[i][j] <= tree[ii][j]:
            return 0
    return 1

def from_bottom(i, j, tree):
    m, _ = get_tree_shape(tree)
    for ii in range(i+1, m):
        if tree[i][j] <= tree[ii][j]:
            return 0
    return 1

def from_left(i, j, tree):
    for jj in range(0, j):
        if tree[i][j] <= tree[i][jj]:
            return 0
    return 1

def from_right(i, j, tree):
    _, n = get_tree_shape(tree)
    for jj in range(j+1, n):
        if tree[i][j] <= tree[i][jj]:
            return 0
    return 1

def is_visible(i, j, tree):
    visible = (from_top(i, j, tree) + from_bottom(i, j, tree) + from_left(i, j, tree) + from_right(i, j, tree))
    if visible != 0:
        return 1
    return 0


def forest(filename):
    tree = get_matrix(filename)
    m, n = get_tree_shape(tree)
    total = 0
    for i in range(0,m):
        for j in range(0, n):
            total += is_visible(i, j, tree)

    print(f'total: {total}')

def view_top(i, j, tree):
    view = 0
    for ii in range(i-1, -1, -1):
        view += 1
        if tree[i][j] <= tree[ii][j]:
            return view
    return view

def view_bottom(i, j, tree):
    m, _ = get_tree_shape(tree)
    view = 0
    for ii in range(i+1, m):
        view += 1
        if tree[i][j] <= tree[ii][j]:
            return view
    return view

def view_left(i, j, tree):
    view = 0
    for jj in range(j-1, -1, -1):
        view += 1
        if tree[i][j] <= tree[i][jj]:
            return view
    return view

def view_right(i, j, tree):
    _, n = get_tree_shape(tree)
    view = 0
    for jj in range(j+1, n):
        view += 1
        if tree[i][j] <= tree[i][jj]:
            return view
    return view


def scene(filename):
    tree = get_matrix(filename)
    m, n = get_tree_shape(tree)
    total = []
    for i in range(0,m):
        for j in range(0, n):
            total.append(scenic_score(i, j, tree))
    print('max: ', max(total))

def scenic_score(i, j, tree):
    return view_top(i, j, tree) * view_bottom(i, j, tree) * view_left(i, j, tree) * view_right(i, j, tree)


if __name__ == '__main__':
    forest(test)
    forest(data)
    scene(test)
    scene(data)
