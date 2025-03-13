import sys

class HoofIt:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.topo_map = []
            for line in f.readlines():
                self.topo_map.append(line.strip())

            self.rowc = len(self.topo_map)
            self.colc = len(self.topo_map[0])
            self.print()

    def find_trailhead(self):
        trailhead = []
        for r in range(self.rowc):
            for c in range(self.colc):
                if self.topo_map[r][c] == '0':
                    trailhead.append((r, c))
        return trailhead

    def print(self):
        for line in self.topo_map:
            print(' '.join(line))
        print(f'{self.rowc} rows x {self.colc} colc')

    def possible_step(self, r, c):
        possible = []
        if r > 0: possible.append((r - 1, c))
        if c > 0: possible.append((r, c - 1))
        if r < self.rowc - 1: possible.append((r + 1, c))
        if c < self.colc - 1: possible.append((r, c + 1))
        return possible

    def next_step(self, current_r, current_c):
        nextstep = []
        val = int(self.topo_map[current_r][current_c])
        for r, c in self.possible_step(current_r, current_c):
            if int(self.topo_map[r][c]) == val + 1:
                nextstep.append((r, c))
        return nextstep

    def part1(self):
        trailheads = self.find_trailhead()
        total = 0
        for t in trailheads:
            current = [t]
            for i in range(9):
                next_step = []
                for x, y in current:
                    next_step += self.next_step(x, y)
                if len(next_step) == 0:
                    break
                current = next_step
            total += len(set(next_step))
        return total

    def part2(self):
        trailheads = self.find_trailhead()
        total = 0
        for t in trailheads:
            current = [t]
            for i in range(9):
                next_step = []
                for x, y in current:
                    next_step += self.next_step(x, y)
                if len(next_step) == 0:
                    break
                current = next_step
            total += len(next_step)
        return total


def main(argv):
    h = HoofIt(argv[0])
    print(f'part1: {h.part1()}')
    print(f'part2: {h.part2()}')

if __name__ == '__main__':
    main(sys.argv[1:])
