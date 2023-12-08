import sys

maximum = {
    'red': 12,
    'green': 13,
    'blue': 14,
        }

def analyze_round(text):
    updated_text = text.strip()
    each_color = updated_text.split(',')

    for each in each_color:
        count = int(each.translate({ord(i): None for i in ' abcdefghijklmnopqrstuvwxyz'}))
        if 'blue' in each:
            if maximum['blue'] < count: return False
        if 'red' in each:
            if maximum['red'] < count: return False
        if 'green' in each:
            if maximum['green'] < count: return False
    
    return True

def analyze_rounds(text):
    updated_text = text.strip()
    rounds = updated_text.split(';')
    for each in rounds:
        if not analyze_round(each): return False

    return True

def analyze_game(text):
    updated_text = text.strip()
    split_input = updated_text.split(':')
    game_id = int(split_input[0].split(' ')[-1])
    if analyze_rounds(split_input[1]):
        return game_id
    return 0

def main(argv):
    total = 0
    with open(argv[0], 'r') as f:
        for line in f.readlines():
            total = total + analyze_game(line)
    print(total)

if __name__ == '__main__':
    main(sys.argv[1:])
