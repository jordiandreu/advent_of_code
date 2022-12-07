"""
--- Day 2: Rock Paper Scissors ---
"""

data = '2022/day02/input_data.txt'
test = '2022/day02/input_test.txt'

mapp = {'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
        }

map_to_win = {'A': 'Y',
              'B': 'Z',
              'C': 'X'
              }

map_to_draw = {'A': 'X',
               'B': 'Y',
               'C': 'Z'
               }

map_to_lose = {'A': 'Z',
               'B': 'X',
               'C': 'Y'
               }

map_to_game = {'X': map_to_lose,
               'Y': map_to_draw,
               'Z': map_to_win
               }

def get_total_score(filename, indirect=True):
    with open(filename) as file:
        my_score = 0
        for line in file:
            a, b = line.split()
            if indirect:
                a, b = get_my_game(a, b)
            my_score += get_my_score(a, b)
    return my_score

def get_my_score(a, b):
    result=0
    game=a+b
    if game in ['AY', 'BZ', 'CX']:
        result+=6
    elif game in ['AX', 'BY', 'CZ']:
        result+=3
    result += mapp[b]
    return result

def get_my_game(a, b):
    return a, map_to_game[b][a]

if __name__ == '__main__':
    print(f'test: ', get_total_score(test, False))
    print(f'puzzle: ', get_total_score(data, False))
    print(f'test: ', get_total_score(test, True))
    print(f'puzzle: ', get_total_score(data, True))
