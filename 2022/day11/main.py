"""
--- Day 11: Monkey in the Middle ---
"""

test = '2022/day11/input_test.txt'
data = '2022/day11/input_data.txt'


def read_input(filename):
    monkeys = []
    with open(filename) as file:
        try:
            while True:
                _ = int(file.readline()[:-2].split('Monkey ')[-1])
                items = list(map(int, file.readline()[:-1].split('  Starting items: ')[-1].split(',')))
                operation = file.readline()[:-1].split('  Operation: new = ')[-1]
                divisor = int(file.readline()[:-1].split(' ')[-1])
                t = int(file.readline()[:-1].split(' ')[-1])
                f = int(file.readline()[:-1].split(' ')[-1])
                monkeys.append(Monkey(items, operation, divisor, t, f))
                file.readline()
        except:
            pass
    return monkeys

class Monkey():
    def __init__(self, items, operation, divisor, t, f):
        self._items = items
        self._operation = operation
        self._divisor = divisor
        self._true = t
        self._false = f
        self._counter = 0

    def inspect(self, monkey_list, factor=1):
        for item in self._items:
            old = item  # old is a string found in eval expression
            if factor == 1: # puzzle 1
                new = eval(self._operation) // 3
            else:   # puzzle 2
                new = eval(self._operation) % factor

            if new % self._divisor == 0:
                monkey_list[self._true].receive(new)
            else:
                monkey_list[self._false].receive(new)
            self._counter += 1
        self._items = []

    def receive(self, item):
        self._items.append(item)

def puzzle(file, rounds, case):
    monkeys = read_input(file)

    factor = 1
    if case == 2:
        for m in monkeys:
            factor *= m._divisor

    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys, factor=factor)
    counts = []
    for m in monkeys:
        # print(f'counter: {m._counter}')
        counts.append(m._counter)

    total = sorted(counts)[-1]*sorted(counts)[-2]
    print(total)

    if case == 1:
        assert total == 55216 #puzzle 1 (20 rounds)
    else:
        assert total == 12848882750 # puzzle 2 (10000 rounds)


if __name__ == '__main__':
    puzzle(data, 20, 1)
    puzzle(data, 10000, 2)