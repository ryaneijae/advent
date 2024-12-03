import sys
import re

class MullItOver:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.matches = re.findall(r"mul\(\d+,\d+\)", f.read())


    def part1(self):
        total = 0
        for e in self.matches:
            num = re.findall(r"\d+", e)
            total += int(num[0]) * int(num[1])
        return total


def main(argv):
    m = MullItOver(argv[0])
    print(m.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
