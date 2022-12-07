"""
--- Day 6: Tuning Trouble ---
"""


test = '2022/day06/input_test.txt'
data = '2022/day06/input_data.txt'


def get_position(filename, packet_size):
    with open(filename) as file:
        for line in file:
            line = list(line)
            count = packet_size
            length = len(line)
            word = []
            for _ in range(packet_size-1):
                word.append(line.pop(0))

            for _ in range(length):
                word.append(line.pop(0))
                if len(set(word)) == packet_size:
                    return count
                else:
                    word.pop(0)
                    count += 1
            return count

if __name__ == '__main__':
    print('test 1: ', get_position(test, 4))
    print('puzzle 1: ', get_position(data, 4))
    print('test 2: ', get_position(test, 14))
    print('puzzle 2: ', get_position(data, 14))