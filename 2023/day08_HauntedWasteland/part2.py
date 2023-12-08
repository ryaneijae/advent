import sys

class HauntedMap:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.directions = f.readline()
            self.directions = self.directions.strip()
            f.readline()

            self.hauntedmap = {}
            for line in f.readlines():
                broken_line = line.split('=')
                name = broken_line[0].strip()
                placeholder = broken_line[-1].strip().replace('(', '').replace(')', '')
                placeholder = placeholder.split(',')
                left = placeholder[0].strip()
                right = placeholder[-1].strip()
                self.hauntedmap[name] = {
                    'left': left,
                    'right': right
                }

    def find_starts(self):
        starts = []
        for each in self.hauntedmap:
            if each[2] == 'A': starts.append(each)
        return starts

    def part1(self):
        current_name = 'AAA'
        target = 'ZZZ'
        count = 0
        while True:
            for direction in self.directions:
                count += 1
                current_node = self.hauntedmap[current_name]
                if direction == 'L':
                    current_name = current_node['left']
                else:
                    current_name = current_node['right']
                if current_name == target:
                    return count

    def get_cycle_and_offset(self, start):
        target = 'Z'
        count = 0
        current = start
        offset = None
        while True:
            for direction in self.directions:
                count += 1
                if direction == 'L':
                    current = self.hauntedmap[current]['left']
                if direction == 'R':
                    current = self.hauntedmap[current]['right']

                if current[2] == target:
                    if offset == None:
                        offset = count
                    else:
                        return count - offset, offset

    def compute_gcd(self, x, y):
        while(y):
            x, y = y, x % y
        return x

    def compute_lcm(self, x, y):
        lcm = (x * y) // self.compute_gcd(x, y)
        return lcm

    def part2(self):
        starts = self.find_starts()
        total = 1
        for start in starts:
            cycle, throw_away = self.get_cycle_and_offset(start)
            total = self.compute_lcm(total, cycle)
        return total


def main(argv):
    haunted_map = HauntedMap(argv[0])
    ans = haunted_map.part2()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
