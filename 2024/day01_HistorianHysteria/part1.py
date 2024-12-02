import sys
import re


pattern = r"(\d+)\s+(\d+)"

class HistorianHysteria:
    def __init__(self, filepath):
        self.left = []
        self.right = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                match = re.search(pattern, line)
                self.left.append(int(match.group(1)))
                self.right.append(int(match.group(2)))
        
        self.left.sort()
        self.right.sort()

    def part1(self):
        total = 0
        for i in range(len(self.left)):
            total += abs(self.left[i] - self.right[i])
        return total


def main(argv):
    h = HistorianHysteria(argv[0])
    print(h.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
