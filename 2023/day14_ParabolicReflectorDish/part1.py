import sys
import numpy as np


class Rocks:
    def __init__(self, filepath):
        r = []    
        with open(filepath, 'r') as f:
            for line in f.readlines():
                r.append([x for x in line.strip()])
        self.grid = np.array(r)
        self.row_len, self.col_len = self.grid.shape

        self._print_grid()

    def _print_grid(self):
        for row in self.grid:
            print(row)
        print(f'({self.row_len} x {self.col_len})')

    def adjust(self, arr):
        base = -1
        for i in range(len(arr)):
            if arr[i] == '#':
                base = i
            elif arr[i] == 'O':
                if base + 1 == i:
                    base += 1
                else:
                    arr[base + 1] = 'O'
                    base += 1
                    arr[i] = '.'

    def tilt(self, direction):
        if direction == 'n':
            for i in range(self.col_len):
                target = self.grid[:, i]
                self.adjust(target)
                self.grid[:, i] = target
            return
        elif direction == 'w':
            for i in range(self.row_len):
                self.adjust(self.grid[i])
            return
        elif direction == 's':
            for i in range(self.col_len):
                target_reverse = self.grid[:, i][::-1]
                self.adjust(target_reverse)
                self.grid[:, i] = target_reverse[::-1]
            return
        elif direction == 'e':
            for i in range(self.row_len):
                reverse = self.grid[i][::-1]
                self.adjust(reverse)
                self.grid[i] = reverse[::-1]
            return
        sys.exit('Tilted Received unexpected direction')

    def part1(self):
        self.tilt('n')
        total = 0
        for i in range(self.row_len):
            count = 0
            for j in range(self.col_len):
                if self.grid[i, j] == 'O': count += 1
            total += (self.row_len - i) * count
        return total


def main(argv):
    rock = Rocks(argv[0])
    ans = rock.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
