"""
--- Day 3: Rucksack Reorganization ---
"""

data = 'day03/input_data.txt'
test = 'day03/input_test.txt'

def numeric(c):
    # a-z: 1-26
    # A-Z: 27 - 52
    value = ord(c) - 96
    if value < 0:
        value = ord(c) - 38
    return value


def puzzle01(filename=test):
    with open(filename) as file:
        value = 0
        for line in file:
            l = len(line)
            a = set(line[:l//2])
            b = set(line[l//2:-1])
            ruck = a.intersection(b).pop()
            value += numeric(ruck)
    return value

def process(g):
    a = set(g[0])
    b = set(g[1])
    c = set(g[2])
    d = a.intersection(b).intersection(c)
    return numeric(d.pop())

def puzzle02(filename=test):
    value = 0
    with open(filename) as file:
        c = file.read().split('\n')
    groups = list(zip(*(iter(c),) * 3))
    for g in groups:
        value += process(g)
    return value

if __name__ == "__main__":
    print('test 01: ', puzzle01(test))
    print('puzzle 01: ', puzzle01(data))
    print('test 02: ', puzzle02(test))
    print('puzzle 02: ', puzzle02(data))
