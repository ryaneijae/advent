import sys
import numpy as np

class LavaMap:
    def __init__(self, filepath):
        floor = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                floor.append([int(x) for x in line.strip()])
    
        self.lavamap = np.array(floor)
        self.row_len, self.col_len = self.lavamap.shape

        self._print_map()

    def _print_map(self):
        for row in self.lavamap:
            print(row)
        print(f'({self.row_len} x {self.col_len})')

    def min_map_mem(self, x, y):
        if x == 0 and y == 0: return self.lavamap[0, 0]
        elif x < 0 or y < 0: return float('inf')
        elif x >= self.row_len or y >= self.col_len: return float('inf')

        if self.min_map[x, y] != -1: return self.min_map[x, y]

        self.min_map[x, y] = self.lavamap[x, y] + min(
            self.min_map_mem(x - 1, y),
            self.min_map_mem(x, y - 1),
            self.min_map_mem(x + 1, y),
            self.min_map_mem(x, y + 1)
            )
        return self.min_map[x, y]

    def part1(self):
        self.min_map = np.array(
                [[-1] * self.col_len for _ in range(self.row_len)]
            )
        

        return self.min_map_mem(self.row_len - 1, self.col_len - 1)

def main(argv):
    lavamap = LavaMap(argv[0])
    ans = lavamap.part1()
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])
