import sys

class GardenGroups:
    def __init__(self, filepath):
        self.garden = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.garden.append(line.strip())
        self.rowc = len(self.garden)
        self.colc = len(self.garden[0])
        self.print()

    def print(self):
        for line in self.garden:
            print(' '.join(line))
        print(f'{self.rowc} rows x {self.colc} cols')

    def possible(self, r, c):
        possible = []
        if r > 0: possible.append((r - 1, c))
        if c > 0: possible.append((r, c - 1))
        if r < self.rowc - 1: possible.append((r + 1, c))
        if c < self.colc - 1: possible.append((r, c + 1))
        return possible

    def find_current_region(self, startx, starty):
        val = self.garden[startx][starty]
        region = set([(startx, starty)])
        exploring = self.possible(startx, starty)
        while exploring: 
            current = []
            for explorex, explorey in exploring:
                if self.garden[explorex][explorey] == val:
                    current.append((explorex, explorey))
            region.update(current)
            possible = []
            for currentx, currenty in current:
                possible += self.possible(currentx, currenty)
            possible = set(possible)
            exploring = []
            for possiblex, possibley in possible:
                if (possiblex, possibley) not in region:
                    exploring.append((possiblex, possibley))
        return [x for x in region]

    def regions(self):
        regions = [] # (type, [location tuples])
        unassigned = []
        for i in range(self.rowc):
            for j in range(self.colc):
                unassigned.append((i, j))
        while unassigned:
            r, c = unassigned[0]
            val = self.garden[r][c]
            region = self.find_current_region(r, c)
            unassigned = [i for i in unassigned if i not in region]
            regions.append((val, region))
        return regions

    def is_touching(self, one, two):
        x1, y1 = one
        x2, y2 = two
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False

    def get_cost(self, region):
        area = len(region)
        fence = 0
        for i in range(len(region)):
            fence += 4
            for j in range(len(region)):
                if i != j:
                    if self.is_touching(region[i], region[j]):
                        fence += -1
        return area * fence

    def part1(self):
        regions = self.regions()
        total = 0
        for val, region in regions:
            total += self.get_cost(region)
        return total


def main(argv):
    g = GardenGroups(argv[0])
    print(g.part1())


if __name__ == '__main__':
    main(sys.argv[1:])
