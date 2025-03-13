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
        self._print_mapping()

    def _sort_build_map(self):
        temp_map = self.built_map.copy()
        new_arr = []
        while len(temp_map):
            lowest = None
            for i in range(len(temp_map)):
                if lowest == None:
                    lowest = i
                    continue
                x, y = temp_map[lowest][0]
                new_x, new_y = temp_map[i][0]
                if new_x < x:
                    lowest = i
            new_arr.append(temp_map[lowest])
            temp_map.pop(lowest)

        self.built_map = new_arr
        return self.built_map

    def _add_to_built_map(self, source, destination, range_len):
        source_end = source + range_len - 1
        delta = destination - source
        first_start, first_end = self.built_map[0][0]
        if source_end < first_start:
            self.built_map.insert(0, [(source, source_end), delta])

    def build_map(self):
        self.built_map = []
        for each in self.mapping['seed-to-soil']:
            start = int(each[1])
            delta = int(each[0]) - start
            end = start + int(each[2]) - 1
            self.built_map.append([(start, end), delta])
        
        print(self._sort_build_map())
        self._add_to_built_map(15, 0, 15)
        print(self.built_map)


    def _remove_empty(self, target_list):
        while ('' in target_list):
            target_list.remove('')
    
    def _print_mapping(self):
        for item in self.mapping:
            print(f"{item}: {self.mapping[item]}")


def main(argv):
    almanac = Almanac(argv[0])
    almanac.build_map()

if __name__ == '__main__':
    main(sys.argv[1:])
