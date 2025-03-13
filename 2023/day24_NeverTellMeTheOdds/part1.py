import sys
import numpy as np

class HailStorm:
    def __init__(self, filepath):
        floor = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                floor.append([x for x in line.strip()])
    
        self.floor = np.array(floor)
        self.row_len, self.col_len = self.floor.shape

        self._print_floor()

    def part1(self):
        pass

def main(argv):
    h = HailStorm(argv[0])
    ans = h.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
