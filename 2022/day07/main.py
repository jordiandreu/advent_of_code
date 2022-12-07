"""
--- Day 7: No Space Left On Device ---
"""
import os

test = '2022/day07/input_test.txt'
data = '2022/day07/input_data.txt'


def get_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line[:-1])
    return lines


def create_tree(lines):
    current_dir = ''
    contents = {}
    for c in lines:
        if c[0] == '$':
            if c[2:4] == 'cd':
                if c[5:] == '..':
                    current_dir, _ = os.path.split(current_dir)
                else:
                    current_dir = os.path.join(current_dir, c[5:])
                    contents[current_dir] = []
            elif c[2:3] == 'ls':
                pass
        else:
            if c[:3] == 'dir':
                new_element = os.path.join(current_dir, c[4:])
            else:
                new_element = int(c.split(' ')[0])
            contents[current_dir].append(new_element)
    return contents


def get_dir_size(dir):
    total = 0
    for elem in dir:
        if isinstance(elem, int):
            total += elem
        else:
            total += get_dir_size(contents[elem])
    return total


def puzzle(filename, capacity=70000000, maximum=100000, minimum_to_update=30000000):

    global contents
    total = 0
    values = []

    contents = create_tree(get_input(filename))
    for dir, content in contents.items():
        value = get_dir_size(content)
        values.append(value)
        # print(f'{dir}: {value}' )
        # Get total disc space for folders smaller than maximum
        if value < 100000:
            total += value

    print(f'size: {total}')

    s_values = sorted(values)
    free= int(capacity - s_values[-1])
    target = int(minimum_to_update - free)

    for v in s_values:
        if v > (target):
            # Size for the smallest dir to delete
            print(f'minimum: {v}')
            break


if __name__ == '__main__':

    puzzle(test)
    puzzle(data)
