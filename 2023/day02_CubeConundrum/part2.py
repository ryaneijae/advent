import sys

def analyze_round(text):
    updated_text = text.strip()
    each_color = updated_text.split(',')

    red = 0
    blue = 0
    green = 0

    for each in each_color:
        count = int(each.translate({ord(i): None for i in ' abcdefghijklmnopqrstuvwxyz'}))
        if 'blue' in each:
            blue = count
        if 'red' in each:
            red = count
        if 'green' in each:
            green = count

    return red, green, blue

def analyze_rounds(text):
    updated_text = text.strip()
    rounds = updated_text.split(';')
    max_red = 0
    max_green = 0
    max_blue = 0
    for each in rounds:
        red, green, blue = analyze_round(each)
        if max_red < red: max_red = red
        if max_green < green: max_green = green
        if max_blue < blue: max_blue = blue

    return max_red, max_green, max_blue

def analyze_game(text):
    updated_text = text.strip()
    split_input = updated_text.split(':')
    game_id = int(split_input[0].split(' ')[-1])

    red, green, blue = analyze_rounds(split_input[1])

    return red * green * blue

def main(argv):
    total = 0
    with open(argv[0], 'r') as f:
        for line in f.readlines():
            total = total + analyze_game(line)
    print(total)

if __name__ == '__main__':
    main(sys.argv[1:])
