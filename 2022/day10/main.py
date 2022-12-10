"""
--- Day 10: Cathode-Ray Tube ---
"""
from collections import deque

test0 = '2022/day10/input_test_0.txt'
test = '2022/day10/input_test.txt'
data = '2022/day10/input_data.txt'

def get_operations_list(filename):
    operations = []
    with open(filename) as file:
        for line in file:
            o = line[:-1].split(' ')
            if o[0] == 'noop':
                operations.append(0)
            else:
                operations.append(0)
                operations.append(int(o[-1]))
    return operations


def register(op):
    reg=[1]
    for o in op:
        reg.append(reg[-1]+o)
    return reg


def draw(cycle, reg):
    column = (cycle-1)%40
    if column in [reg-1, reg, reg+1]:
        return '#'
    return '.'


if __name__ == '__main__':
    total=0
    crt=[]

    op = get_operations_list(data)
    r=register(op)

    for cycle in range(20,260,40):
        total+=r[cycle-1]*(cycle)

    print(total)

    for i, v in enumerate(r,1):
        crt.append(draw(i, v))

    print(' '.join(crt[0:40]))
    print(' '.join(crt[40:80]))
    print(' '.join(crt[80:120]))
    print(' '.join(crt[120:160]))
    print(' '.join(crt[160:200]))
    print(' '.join(crt[200:240]))
