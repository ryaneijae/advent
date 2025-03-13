import sys
import numpy as np

class DigPlan:
    def __init__(self, filepath):
        self.plan = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                placeholder = line.strip().split(' ')
                self.plan.append(
                        (
                        placeholder[0],
                        int(placeholder[1]),
                        placeholder[2].replace('(', '').replace(')', '')
                        )
                )

    def interpret_plan(self):
        self.hole_edge = []
        current_x = 0
        current_y = 0
        row_len = current_x
        col_len = current_y
        for direction, strength, rgb in self.plan:
            if direction == 'U':
                for i in range(strength):
                    self.hole_edge.append((current_x - (i + 1), current_y))
                current_x = current_x - strength
            elif direction == 'D':
                for i in range(strength):
                    self.hole_edge.append((current_x + (i + 1), current_y))
                current_x = current_x + strength
            elif direction == 'L':
                for i in range(strength):
                    self.hole_edge.append((current_x, current_y - (i + 1)))
                current_y = current_y - strength
            elif direction == 'R':
                for i in range(strength):
                    self.hole_edge.append((current_x, current_y + (i + 1)))
                current_y = current_y + strength
            else:
                sys.exit('Something went wrong! Unexpected direction')
            if row_len < current_x: row_len = current_x
            if col_len < current_y: col_len = current_y
        self.row_len = row_len + 1
        self.col_len = col_len + 1
        print(f'({self.row_len} x {self.col_len})')
    
    def is_inside(self, x, y):
        if x <= 0 or y <= 0: return False
        if x >= self.row_len - 1 or y >= self.col_len - 1: return False


    def create_filled_map(self):
        self.interpret_plan()
        self.filled_map = np.array(
                [['#'] * self.col_len for _ in range(self.row_len)]
        )

        for x in range(self.row_len):
            for y in range(self.col_len):
                if (x, y) not in self.hole_edge: self.filled_map[x, y] = '.'
                else: break

            for y in range(self.col_len):
                if (x, self.col_len - y - 1) not in self.hole_edge:
                    self.filled_map[x, self.col_len - y - 1] = '.'
                else: break

        for y in range(self.col_len):
            for x in range(self.row_len):
                if (x, y) not in self.hole_edge: self.filled_map[x, y] = '.'
                else: break

            for x in range(self.row_len):
                if (self.row_len - x - 1, y) not in self.hole_edge:
                    self.filled_map[self.row_len - x - 1, y] = '.'
                else: break


    def part1(self):
        self.create_filled_map()
        count = 0
        for x in range(self.row_len):
            for y in range(self.col_len):
                if self.filled_map[x, y] == '#': count += 1

        return count
        


def main(argv):
    d = DigPlan(argv[0])
    ans = d.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
