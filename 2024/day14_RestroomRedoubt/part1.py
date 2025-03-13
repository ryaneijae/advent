import sys
import re

class RestroomRedoubt:
    def __init__(self, filepath):
        self.robots = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                n = re.findall(r'-?\d+', line)
                self.robots.append((int(n[1]), int(n[0]), int(n[3]), int(n[2])))
        self.rowc = 103
        self.colc = 101
        self.seconds = 100
    
    def print(self):
        for e in self.robots:
            print(e)
        print(f'Total of {len(self.robots)}')

    def teleport(self, x, y):
        return x % self.rowc, y % self.colc

    def tick(self):
        for i in range(len(self.robots)):
            x, y, dx, dy = self.robots[i]
            x += dx
            y += dy
            x, y = self.teleport(x, y)
            self.robots[i] = (x, y, dx, dy)

    def draw(self):
        room = []
        for i in range(self.rowc):
            room.append(['.' for j in range(self.colc)])

        for i in range(len(self.robots)):
            x, y, dx, dy = self.robots[i]
            if room[x][y] == '.':
                room[x][y] = '1'
            else:
                room[x][y] = str(int(room[x][y]) + 1)

        for i in range(self.rowc):
            print(' '.join(room[i]))

    def count(self):
        q1 = q2 = q3 = q4 = 0
        for i in range(len(self.robots)):
            x, y, dx, dy = self.robots[i]
            # quad 1
            if x < (self.rowc // 2) and y < (self.colc // 2):
                q1 += 1
            elif x < (self.rowc // 2) and y > (self.colc // 2):
                q2 += 1
            elif x > (self.rowc // 2) and y < (self.colc // 2):
                q3 += 1
            elif x > (self.rowc // 2) and y > (self.colc // 2):
                q4 += 1
        return q1 * q2 * q3 * q4

    def part1(self):
        for i in range(self.seconds):
            self.tick()
        return self.count()


def main(argv):
    r = RestroomRedoubt(argv[0])
    print(r.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
