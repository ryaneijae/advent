import sys
import numpy as np


def custom_diff(a, b):
    if len(a) != len(b):
        sys.exit('Function offby received 2 arrays of different size {a} {b}')
    offby = 0
    for i in range(len(a)):
        if a[i] != b[i]: offby += 1
    return offby

    
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

    def overlap_off1(self, a, b):
        min_size = min(len(a), len(b))
        if min_size == 0: return False
        offby = 0
        for i in range(min_size):
            offby += custom_diff(a[i], b[i])
            if offby >= 2: return False
        if offby == 1: return True
        return False

    def find_mirror(self, mirror, direction):
        if direction == 'row':
            current = mirror.copy()
        else:
            current = np.rot90(mirror.copy(), k=3)
        reverse = []
        i = 0
        while len(current):
            target = np.array(current[0])
            reverse.insert(0, target)
            current = current[1:]
            if self.overlap(np.array(reverse), current):
                return i + 1
            i += 1
        return 0
    
    def find_mirror_off1(self, mirror, direction):
        if direction == 'row':
            current = mirror.copy()
        else:
            current = np.rot90(mirror.copy(), k=3)

        print(f'Looking at {current} for {direction}')
        reverse = []
        i = 0
        while len(current):
            target = np.array(current[0])
            reverse.insert(0, target)
            current = current[1:]
            if self.overlap_off1(np.array(reverse), current):
                return i + 1
            i += 1
        return 0

    def part1(self):
        total = 0
        for mirror in self.mirrors:
            ans = (100 * self.find_mirror(mirror, 'row')
                   + self.find_mirror(mirror, 'col'))
            total += ans
        return total

    def part2(self):
        total = 0
        for mirror in self.mirrors:
            print(f'Checking {mirror}')
            ans = (100 * self.find_mirror_off1(mirror, 'row')
                   + self.find_mirror_off1(mirror, 'col'))
            total += ans
        return total

def main(argv):
    mirrors = Mirrors(argv[0])
    ans = mirrors.part2()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
