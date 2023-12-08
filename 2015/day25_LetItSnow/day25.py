import sys


def transpose(x):
    return x * 252533 % 33554393


def find_pattern(x):
    arr = [x]
    i = 0
    while True:
        i += 1
        output = transpose(arr[i - 1])
        if output == arr[0]:
            return arr
        arr.append(output)


def find_n(x, y):
    return (x + y - 2) * (x + y - 1) // 2 + y


def part1():
    start = 20151125
    row = 2978
    col = 3083
    arr = find_pattern(start)
    n = find_n(row, col)

    return arr[(n % len(arr)) - 1]

def main(argv):
    ans = part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
