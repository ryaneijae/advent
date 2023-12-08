import sys

def part1(text):
    plus_one = 0
    minus_one = 0
    for each in text:
        if each == '(':
            plus_one += 1
        else:
            minus_one += 1
    return plus_one - minus_one


def part2(text, target_floor):
    count = 0
    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        else:
            count -= 1

        if count == target_floor:
            return i + 1

def main(argv):
    with open(argv[0], 'r') as f:
        text = f.readline()

    text = text.strip()

    ans = part1(text)
    print(ans)

    ans = part2(text, -1)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])
