import sys

step = {
        'N': (-1, 0),
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1)
        }

change_dir = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
        }

class GuardGallivant:
    def __init__(self, filepath):
        self.grid = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.grid.append(line.strip())

        self.rowc = len(self.grid)
        self.colc = len(self.grid[0])
        self._print_grid()
        x, y = self.find_start()
        self.start = ('N', x, y)
        self.current = self.start
        self.positions = set()
        self.positions.add(self.current)

    def _print_grid(self):
        for line in self.grid:
            print(' '.join(line))
        print(f'{self.rowc} rows x {self.colc} cols')

    def _print_status(self):
        print(f'current: {self.current}')
        print(f'positions: {self.positions}')
        print()

    def find_start(self):
        for i in range(len(self.grid)):
            if '^' in self.grid[i]:
                return i, self.grid[i].index('^')
        return None, None

    def is_out(self, d, x, y):
        if x < 0 or x >= self.colc: return True
        if y < 0 or y >= self.rowc: return True
        return False

    def loc_count(self):
        temp_set = set()
        for d, x, y in self.positions:
            temp_set.add((x, y))
        return len(temp_set)

    def check_blocked(self):
        d, x, y= self.current
        dx, dy = step[d]
        if not self.is_out(d, x + dx, y + dy):
            if self.grid[x + dx][y + dy] == '#':
                d = change_dir[d]
        self.current = (d, x, y)
        self.positions.add(self.current)

    def a_step(self):
        d, x, y = self.current
        dx , dy = step[d]
        self.current = (d, x + dx, y + dy)
        self.positions.add(self.current)
        self.check_blocked()
        
    def part1(self):
        while not self.is_out(*self.current):
            self.a_step()
        return self.loc_count() - 1


def main(argv):
    g = GuardGallivant(argv[0])
    print(g.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
