"""
--- Day 5: Supply Stacks ---
"""
from copy import deepcopy


test = '2022/day05/input_test.txt'
data = '2022/day05/input_data.txt'


def get_code(filename, header, puzzle):
    h = deepcopy(header)
    with open(filename) as file:

        for line in file:
            if line == '\n':
                break

        for line in file:
            times, source, origin = line.split()[1::2]
            if puzzle == 2:
                # insert crates as a single block
                temp = []
                for _ in range(int(times)):
                    temp.insert(0,h[source].pop())
                h[origin].extend(temp)
            else:
                # insert crate one by one
                for _ in range(int(times)):
                    h[origin].append(h[source].pop())

    result = []
    for k, v in h.items():
        result.append(h[k][-1])
    return ''.join(result)


def get_header(filename):
    values = []
    header = {}
    with open(filename) as file:
        line = file.readline()
        while line != '\n':
            values.append(line)
            line = file.readline()
        values.reverse()

    # extract array of keys, values are the stack to move
    keys = values.pop(0)

    # construct header as dictionary
    for i in keys[:-1]:
        if i != ' ':
            idx = keys.index(i)
            a = []
            for v in values:
                try:
                    if v[idx] != ' ':
                        a.append(v[idx])
                except:
                    pass
            header[i] = a
    return header


if __name__ == '__main__':
    header = get_header(filename=test)
    print('test 1: ', get_code(test, header, 1))
    print('test 2: ', get_code(test, header, 2))

    header = get_header(filename=data)
    print('puzzle 1: ', get_code(data, header, 1))
    print('puzzle 2: ', get_code(data, header, 2))
