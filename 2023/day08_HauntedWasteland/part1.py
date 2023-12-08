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


def main(argv):
    haunted_map = HauntedMap(argv[0])
    ans = haunted_map.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
