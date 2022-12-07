"""
--- Day 1: Calorie Counting ---
"""

data='2022/day01/input_data.txt'
test='2022/day01/input_test.txt'


def get_calories_list(filename=test):
    with open(filename) as file:
        total = []
        partial = 0
        for line in file:
            if line != "\n":
                partial+=int(line)
            else:
                total.append(partial)
                partial=0
        total.append(partial) # append last value
    return list(zip(total, [x + 1 for x in range(len(total))]))


def get_top_calories_and_elf(total, top=1):
    top_elfs = sorted(total, reverse=True)[:top]
    return top_elfs


def puzzle01(file):
    print(get_top_calories_and_elf(get_calories_list(filename=file)))


def puzzle02(file):
    top3 = get_top_calories_and_elf(get_calories_list(filename=file), top=3)
    total_cal = sum(x[0] for x in top3), top3
    print(total_cal)


if __name__ == "__main__":
    puzzle01(data)
    puzzle02(data)
