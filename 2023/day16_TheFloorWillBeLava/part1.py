import sys
import numpy as np


beam_map = {
    '.': {
        'n': ['s'],
        'w': ['e'],
        's': ['n'],
        'e': ['w']
    },
    '/': {
        'n': ['w'],
        'w': ['n'],
        's': ['e'],
        'e': ['s']
    },
    '\\': {
        'n': ['e'],
        'w': ['s'],
        's': ['w'],
        'e': ['n']
    },
    '|': {
        'n': ['s'],
        'w': ['n', 's'],
        's': ['n'],
        'e': ['n', 's']
    },
    '-': {
        'n': ['w', 'e'],
        'w': ['e'],
        's': ['w', 'e'],
        'e': ['w']
    },
}


class Floor:
    def __init__(self, filepath):
        floor = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                floor.append([x for x in line.strip()])
    
        self.floor = np.array(floor)
        self.row_len, self.col_len = self.floor.shape

        self._print_floor()

    def _print_floor(self):
        for row in self.floor:
            print(row)
        print(f'({self.row_len} x {self.col_len})')

    def sim_light(self, head):
        next_head = []
        for head_x, head_y, direction in head:
            next_dir = beam_map[self.floor[head_x, head_y]][direction]
            for each in next_dir:
                if each == 'n':
                    next_row = head_x - 1
                    next_col = head_y
                    next_dir = 's'
                elif each == 'w':
                    next_row = head_x
                    next_col = head_y - 1
                    next_dir = 'e'
                elif each == 's':
                    next_row = head_x + 1
                    next_col = head_y
                    next_dir = 'n'
                elif each == 'e':
                    next_row = head_x
                    next_col = head_y + 1
                    next_dir = 'w'
                else:
                    sys.exit('Unexpected Direction')
                if next_row < 0 or next_col < 0: continue
                if next_row >= self.row_len or next_col >= self.col_len: continue
                next_head.append((next_row, next_col, next_dir))
        return next_head

    def get_energized(self):
        energized = set()
        for x, y, d in self.light_path:
            energized.add((x, y))
        return energized

    def part1(self):
        head = [(0, 0, 'w')]
        self.light_path = [(0, 0, 'w')]
        while True:
            head = self.sim_light(head)
            if set(head).issubset(set(self.light_path)): break
            head = list(set(head))
            self.light_path += head
            self.light_path = list(set(self.light_path))

        return len(self.get_energized())


def main(argv):
    f = Floor(argv[0])
    ans = f.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
