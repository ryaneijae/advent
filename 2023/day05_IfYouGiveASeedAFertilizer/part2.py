import sys
import numpy as np

class Almanac:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.mapping = {}
            for line in f.readlines():
                if line == '\n':
                    continue
                elif "seeds:" in line:
                    current_line = line.strip().split(":")
                    self.seeds = current_line[-1].split(" ")
                    self._remove_empty(self.seeds)
                elif "map" in line:
                    last = line.strip().split(" ")[0]
                    self.mapping[last] = []
                else:
                    self.mapping[last].append(line.split())
        print(self.seeds)

    def _sort_mapping(self):
        for each in self.mapping:
            self.mapping[each].sort()

    def _print_mapping(self):
        for item in self.mapping:
            print(f"{item}: {self.mapping[item]}")

    def _remove_empty(self, target_list):
        while ('' in target_list):
            target_list.remove('')

    def transpose(self, target, key_name):
        for each in self.mapping[key_name]:
            dest_start = int(each[0])
            source_start = int(each[1])
            range_len = int(each[2])
            if (target >= source_start) and (target < (source_start + range_len)):
                 return dest_start + (target - source_start)
        return target

    def transpose_backwards(self, target, key_name):
        for each in self.mapping[key_name]:
            dest_start = int(each[1])
            source_start = int(each[0])
            range_len = int(each[2])
            if (target >= source_start) and (target < (source_start + range_len)):
                 return dest_start + (target - source_start)
        return target

    def transpose_seed(self, seed):
        t = self.transpose(seed, 'seed-to-soil')
        t = self.transpose(t, 'soil-to-fertilizer')
        t = self.transpose(t, 'fertilizer-to-water')
        t = self.transpose(t, 'water-to-light')
        t = self.transpose(t, 'light-to-temperature')
        t = self.transpose(t, 'temperature-to-humidity')
        t = self.transpose(t, 'humidity-to-location')
        return t

    def transpose_location(self, location):
        t = self.transpose_backwards(location, 'humidity-to-location')
        t = self.transpose_backwards(t, 'temperature-to-humidity')
        t = self.transpose_backwards(t, 'light-to-temperature')
        t = self.transpose_backwards(t, 'water-to-light')
        t = self.transpose_backwards(t, 'fertilizer-to-water')
        t = self.transpose_backwards(t, 'soil-to-fertilizer')
        t = self.transpose_backwards(t, 'seed-to-soil')
        return t
        
    def in_seeds(self, target):
        for i in range(0, len(self.seeds), 2):
            start = int(self.seeds[i])
            range_len = int(self.seeds[i + 1])
            if (target >= start) and (target < (start + range_len)):
                return True
        return False

    def get_lowest_location(self):
        i = 1
        while True:
            if not (i % 10000): print(f'Checking {i}')
            seed_target = self.transpose_location(i)
            if self.in_seeds(seed_target):
                print(f'Seed: {seed_target} --> Location: {i}')
                return seed_target, i
            else:
                i += 1

def main(argv):
    almanac = Almanac(argv[0])
    x, y = almanac.get_lowest_location()    


if __name__ == '__main__':
    main(sys.argv[1:])
