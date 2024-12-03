import sys
import re

class MullItOver:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.instructions = f.read()

    def find_mul(self):
        pattern = r"mul\(\d+,\d+\)"
        return re.findall(pattern, self.instructions)

    def find_instructions(self):
        pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
        return re.findall(pattern, self.instructions)
        
    def part1(self):
        matches = self.find_mul()
        total = 0
        for e in matches:
            num = re.findall(r"\d+", e)
            total += int(num[0]) * int(num[1])
        return total

    def part2(self):
        matches = self.find_instructions()
        total = 0
        active = True
        for i in range(len(matches)):
            if matches[i] == 'do()':
                active = True
            elif matches[i] == "don't()":
                active = False
            else:
                if active:
                    num = re.findall(r"\d+", matches[i])
                    total += int(num[0]) * int(num[1])
        return total


def main(argv):
    m = MullItOver(argv[0])
    print(m.part1())
    print(m.part2())

if __name__ == '__main__':
    main(sys.argv[1:])
