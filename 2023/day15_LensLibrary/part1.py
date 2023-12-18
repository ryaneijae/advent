import sys
import numpy as np


class LensLibrary:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.lens = line.strip().split(',')

        print(self.lens)

    def hash_algorithm(self, arr):
        current = 0
        for i in range(len(arr)):
            current = ((current + ord(arr[i])) * 17) % 256
        return current

    def part1(self):
        total = 0
        for each in self.lens:
            ans = self.hash_algorithm(each)
            total = total + ans
        return total

def main(argv):
    lens = LensLibrary(argv[0])
    ans = lens.part1()
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])
