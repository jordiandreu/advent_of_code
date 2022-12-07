"""
--- Day 4: Camp Cleanup ---
"""

data = '2022/day04/input_data.txt'
test = '2022/day04/input_test.txt'

def get_set(str_range):
    a, b = str_range.split('-')
    return set(range(int(a), int(b) + 1))

def do_overlap(a, b, all=True):
    if all:
        return a.intersection(b) == a or a.intersection(b) == b
    else:
        return len(a.intersection(b)) != 0

def puzzle(filename=test, all=True):
    with open(filename) as file:
        overlap = 0
        for line in file:
            sa, sb = line.split(',')
            a = get_set(sa)
            b = get_set(sb)
            if do_overlap(a, b, all):
                overlap += 1
    return overlap


if __name__ == '__main__':
    print('test: ', puzzle(test))
    print('puzzle: ', puzzle(data))
    print('test: ', puzzle(test, all=False))
    print('puzzle: ', puzzle(data, all=False))
