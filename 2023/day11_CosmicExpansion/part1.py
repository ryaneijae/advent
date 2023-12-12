import sys
import numpy as np


def in_between(x, y, t):
    if x < y:
        if x <= t <= y: return True
    if y <= t <= x: return True
    return False

class Universe:
    def __init__(self, filepath):
        universe = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                universe.append([x for x in line.strip()])
        
        self.universe = np.array(universe)
        self.row_len, self.col_len = self.universe.shape
        
        self._print_universe()
        self._get_expanded()
        self._get_galaxies()

    def _print_universe(self):
        for row in self.universe:
            print(row)
        print(f'({self.row_len} x {self.col_len})')

    def _get_expanded(self):
        self.expanded_row = []
        for row_index in range(self.row_len):
            if '#' not in self.universe[row_index]: self.expanded_row.append(row_index)

        self.expanded_col = []
        for col_index in range(self.col_len):
            placeholder = self.universe[0:self.row_len, col_index]
            if '#' not in placeholder: self.expanded_col.append(col_index)

    def _get_galaxies(self):
        self.galaxies = []
        for row_index in range(self.row_len):
            for col_index in range(self.col_len):
                if self.universe[row_index, col_index] == '#':
                    self.galaxies.append((row_index, col_index))
        self.num_galaxies = len(self.galaxies)

    def get_galaxy_pairs(self):
        galaxy_pairs = []
        for i in range(self.num_galaxies):
            for j in range(self.num_galaxies):
                if i != j:
                    if i < j:
                        pair = [self.galaxies[i], self.galaxies[j]]
                    else:
                        pair = [self.galaxies[j], self.galaxies[i]]
                    if pair not in galaxy_pairs: galaxy_pairs.append(pair)
        print(len(galaxy_pairs))
        return galaxy_pairs

    def get_distance(self, gal1, gal2):
        row1, col1 = gal1
        row2, col2 = gal2

        distance_wo_expansion = abs(row1 - row2) + abs(col1 - col2)
        distance = distance_wo_expansion
        for e in self.expanded_row:
            if in_between(row1, row2, e): distance += 1
        for e in self.expanded_col:
            if in_between(col1, col2, e): distance += 1
        return distance

    def part1(self):
        galaxy_pairs = self.get_galaxy_pairs()
        total = 0
        for gal1, gal2 in galaxy_pairs:
            value = self.get_distance(gal1, gal2)
            total = total + value
        return total

def main(argv):
    universe = Universe(argv[0])
    ans = universe.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
