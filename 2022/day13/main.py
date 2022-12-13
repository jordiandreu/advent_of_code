"""
--- Day 13: Distress Signal ---
"""
from copy import deepcopy

test = '2022/day13/input_test.txt'
data = '2022/day13/input_data.txt'

def read_input(filename):
    signal = []
    with open(filename) as file:
        try:
            while True:
                left = eval(file.readline()[:-1])
                right = eval(file.readline()[:-1])
                signal.append((left, right))
                line = file.readline()
                if not line.endswith("\n"): break
        except:
            pass
    return signal

def read_input2(filename):
    signal = []
    with open(filename) as file:
        try:
            while True:
                left = Packet(file.readline()[:-1])
                right = Packet(file.readline()[:-1])
                signal.append(left)
                signal.append(right)
                line = file.readline()
                if not line.endswith("\n"): break
        except:
            pass
    return signal


def compare(a, b):
    """
    Define that a > b is the correct order for packets
    """
    # print(f'comparing {a} and {b}')
    if isinstance(a, list) and isinstance(b, list):
        result = 'Tie'
        la = len(a)
        lb = len(b)
        for i in range(max(la, lb)):
            try:
                aa = a.pop(0)
                bb = b.pop(0)
                result = compare(aa, bb)
                while result == 'Tie':
                    aa = a.pop(0)
                    bb = b.pop(0)
                    result = compare(aa, bb)
            except:
                if la < lb:
                    return 1
                elif lb < la:
                    return 0
                else:
                    return 'Tie'
            return result
        return result
    elif isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return 0
        else:
            return 'Tie'
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)


def puzzle1(file):
    """
    Using the compare function
    """
    signal = read_input(file)
    results = []

    for s in signal:
        results.append(compare(*s))
    idx = list(range(1, len(results) + 1))
    print(sum([i*j for (i, j) in zip(results, idx)]))


class Packet:
    def __init__(self, value):
        self._value = eval(value)

    def __gt__(self, other):
        _old = deepcopy(self._value)
        _other = deepcopy(other._value)
        result = not bool(compare(self._value, other._value))
        self._value = _old
        other._value = _other
        return result

    def __lt__(self, other):
        _old = deepcopy(self._value)
        _other = deepcopy(other._value)
        result = bool(compare(self._value, other._value))
        self._value = _old
        other._value = _other
        return result

    def __eq__(self, other):
        return not self.__lt__(other) and not self.__gt__(other)

    def __repr__(self):
        return f'{self._value}'


def puzzle2(file):
    """
    Using the Packet class with overwritten operators
    """
    signal = read_input2(file)
    # Add markers
    signal.append(Packet("[[2]]"))
    signal.append(Packet("[[6]]"))

    s = sorted(signal)
    count6 = 0
    count2 = 0
    for e in s:
        count2 += 1
        count6 += 1
        if str(e) == "[[2]]": c2 = count2
        if str(e) == "[[6]]": c6 = count6
    print(c2 * c6)


if __name__ == '__main__':
    puzzle1(test)
    puzzle1(data)
    puzzle2(test)
    puzzle2(data)

    #a = Packet("[[6],[10,[[2,7,3,8],[5],8,9],[0],10],[[[1,5],[1,4,0,2],[10,8,9]]],[2]]")
    #b = Packet("[[10,[],[5,[1,4,1],6],[[8,3,0,8],[2]]],[1,[[],[8],[]],10,9,10],[]]")
    #print(compare(a, b))
    #print(a < b)
    #print(a > b)
