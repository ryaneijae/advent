import sys

class ResonantCollinearity:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.scan = []
            for line in f.readlines():
                self.scan.append(line.strip())
        self.rowc = len(self.scan)
        self.colc = len(self.scan[0])
        self._print()
        self.frequency = self.find_frequency()

    def _print(self):
        for line in self.scan:
            print(' '.join(line))
        print(f'{self.rowc} rows x {self.colc} cols')

    def find_frequency(self):
        frequency = {}
        for r in range(self.rowc):
            for c in range(self.colc):
                char = self.scan[r][c]
                if char != '.':
                    if char in frequency:
                        frequency[char].append((r, c))
                    else:
                        frequency[char] = [(r, c)]
        return frequency

    def find_antinodes(self, l):
        # Assumes all listed are same type
        antinode = []
        for i in range(len(l)):
            for j in range(len(l)):
                if i != j:
                    xi, yi = l[i]
                    xj, yj = l[j]
                    dx = xi - xj
                    dy = yi - yj
                    antinode.append((xi + dx, yi + dy))
        return antinode

    def count_in_scan(self, l):
        total = 0
        for e in l:
            r, c = e
            if (r >= 0
                and r < self.rowc
                and c >= 0
                and c < self.colc
                ): 
                total += 1
        return total

    def part1(self):
        all_antinodes = set()
        for e in self.frequency:
            node = self.find_antinodes(self.frequency[e])
            all_antinodes.update(node)
        return self.count_in_scan(all_antinodes)


if __name__ == '__main__':
    r = ResonantCollinearity(sys.argv[1])
    print(r.part1())