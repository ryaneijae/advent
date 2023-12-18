import sys
import numpy as np


class LensLibrary:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.lens = line.strip().split(',')

        print(self.lens)

        self.hash_map = [{} for _ in range(256)]

    def _print_hash_map(self):
        for i in range(len(self.hash_map)):
            if self.hash_map[i]:
                print(f'{i}: {self.hash_map[i]}')

    def hash_algorithm(self, arr):
        current = 0
        for i in range(len(arr)):
            current = ((current + ord(arr[i])) * 17) % 256
        return current

    def part1(self):
        total = 0
        for each in self.lens:
            ans = self.hash_algorithm(each)
            total = total + ans
        return total

    def build_hashmap(self):
        for each in self.lens:
            if '=' in each:
                placeholder = each.split('=')
                name = placeholder[0]
                f_len = placeholder[1]
                dest = self.hash_algorithm(name)
                self.hash_map[dest][name] = int(f_len)
            else:
                name = each[0:-1]
                dest = self.hash_algorithm(name)
                if name in self.hash_map[dest]:
                    del self.hash_map[dest][name]

    def calc_total_hashmap(self):
        total = 0
        for i in range(len(self.hash_map)):
            dict_index = 1
            for lens in self.hash_map[i]:
                total += (i + 1) * dict_index * self.hash_map[i][lens]
                dict_index += 1
        return total

    def part2(self):
        self.build_hashmap()
        return self.calc_total_hashmap()


def main(argv):
    lens = LensLibrary(argv[0])
    ans = lens.part2()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
