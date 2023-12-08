import sys

def find_calibration_value(text):
    stripped_text = text.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
    stripped_text = stripped_text.strip()
    value = int(stripped_text[0]) * 10 + int(stripped_text[-1])
    return value

def main(argv):
    total = 0

    with open(argv[0], 'r') as f:
        for line in f.readlines():
            total = total + find_calibration_value(line)

    print(total)

if __name__ == '__main__':
    main(sys.argv[1:])
