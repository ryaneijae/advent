import sys
import numpy as np


class Mirrors:
    def __init__(self, filepath):
        ash_rock = []    
        with open(filepath, 'r') as f:
            for line in f.readlines():
                ash_rock.append([x for x in line.strip()])

        self.mirrors = []
        i = 0
        current = []
        while i < len(ash_rock):
            if ash_rock[i] == []:
                self.mirrors.append(np.array(current))
                current = []
            else:
                current.append(ash_rock[i])
            i += 1
        
        self.mirrors.append(np.array(current))

    def _print_mirrors(self):
        for mirror in self.mirrors:
            for row in mirror:
                print(row)
            print()

    def overlap(self, a, b):
        min_size = min(len(a), len(b))
        if min_size == 0: return False
        for i in range(min_size):
            if not np.array_equal(a[i], b[i]): return False
        return True

    def mirror_location(self, mirror):
        row_value = 0
        col_value = 0

        current = mirror.copy()
        reverse = []
        i = 0
        while len(current):
            target = np.array(current[0])
            reverse.insert(0, target)
            current = current[1:]
            if self.overlap(np.array(reverse), current):
                row_value = i + 1
            i += 1
        
        current = np.rot90(mirror.copy(), k=3)
        reverse = []
        j = 0
        while len(current):
            target = np.array(current[0])
            reverse.insert(0, target)
            current = current[1:]
            if self.overlap(np.array(reverse), current):
                col_value = j + 1
            j += 1

        return 100 * row_value + col_value

    def part1(self):
        total = 0
        for mirror in self.mirrors:
            ans = self.mirror_location(mirror)
            total += ans
        return total

def main(argv):
    mirrors = Mirrors(argv[0])
    ans = mirrors.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
