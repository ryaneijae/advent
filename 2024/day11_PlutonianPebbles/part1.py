import sys

class PlutonianPebbles:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            line = f.readlines()[0].strip()
        self.stones = {}
        for e in line.split(' '):
            if e in self.stones:
                self.stones[e] += 1
            else:
                self.stones[e] = 1
        print(self.stones)
        
    def add_to(self, d, x, c):
        x = str(int(x))
        if x in d:
            d[x] += c
        else:
            d[x] = c

    def blink(self):
        new_stones = {}
        for e, c in self.stones.items():
            if int(e) == 0:
                self.add_to(new_stones, 1, c)
            elif len(e) % 2 == 0:
                left = e[: len(e) // 2]
                right = e[len(e) // 2 :]
                self.add_to(new_stones, left, c)
                self.add_to(new_stones, right, c)
            else:
                self.add_to(new_stones, 2024 * int(e), c)
        self.stones = new_stones

    def count_stones(self):
        total = 0
        for e, c in self.stones.items():
            total += c
        return total

    def part1(self):
        for i in range(25):
            self.blink()
        return self.count_stones()

def main(argv):
    p = PlutonianPebbles(argv[0])
    print(f'part1: {p.part1()}')

if __name__ == '__main__':
    main(sys.argv[1:])
