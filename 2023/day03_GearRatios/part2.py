import sys
import numpy as np

def arr_to_int(arr):
    value = 0
    for i in range(len(arr)):
        value = value * 10 + int(arr[i])
    return value

class GearRatios:
    def __init__(self, filepath):
        schematic = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                schematic.append([i for i in line.strip()])
        
        total = 0
        self.schematic = np.array(schematic)
        self.row_len, self.ele_len = self.schematic.shape

    def print(self):
        for row in self.schematic:
            print(row)
        print(f"({self.row_len} x {self.ele_len})")

    def is_partnumber(self, ele_index_min, ele_index_max, row_index):
        ele_range_min = ele_index_min - 1
        ele_range_max = ele_index_max + 1
        row_range_min = row_index - 1
        row_range_max = row_index + 1
        
        if ele_range_min < 0: ele_range_min = 0
        if row_range_min < 0: row_range_min = 0
        if ele_range_max > self.ele_len: ele_range_max = self.ele_len - 1
        if row_range_max >= self.row_len: row_range_max = self.row_len - 1

        for row in range(row_range_min, row_range_max + 1):
            for ele in range(ele_range_min, ele_range_max + 1):
                if self.schematic[row, ele] not in ".0123456789":
                    return True
        return False

    def get_number_loc(self):
        number_loc = []
        for row_index in range(self.row_len):
            last_was_num = False
            start = None
            for ele_index in range(self.ele_len):
                if self.schematic[row_index, ele_index] in "0123456789":
                    if last_was_num: continue
                    start = ele_index
                    last_was_num = True
                else:
                    if last_was_num:
                        last_was_num = False
                        number_loc.append((start, ele_index - 1, row_index))
                        start = None
            if start != None:
                number_loc.append((start, self.ele_len, row_index))

        return number_loc

    def get_star_loc(self):
        star_loc = []
        for row_index in range(self.row_len):
            for ele_index in range(self.ele_len):
                if self.schematic[row_index, ele_index] == '*':
                    star_loc.append((row_index, ele_index))

        return star_loc

    def sum_of_partnumber(self):
        total = 0
        number_location = self.get_number_loc()
        for ele_index_min, ele_index_max, row_index in number_location:
            if self.is_partnumber(ele_index_min, ele_index_max, row_index):
                pn = self.schematic[row_index, ele_index_min : ele_index_max+1]
                int_pn = arr_to_int(pn)
                total = total + int_pn
        return total

    def is_gear(self, star_row, star_ele):
        count = 0
        gear_ratio = 1
        for each_ele_min, each_ele_max, each_row in self.number_loc:
            matrix = []
            ele_range_min = each_ele_min - 1
            ele_range_max = each_ele_max + 1
            row_range_min = each_row - 1
            row_range_max = each_row + 1
        
            if ele_range_min < 0: ele_range_min = 0
            if row_range_min < 0: row_range_min = 0
            if ele_range_max > self.ele_len: ele_range_max = self.ele_len - 1
            if row_range_max >= self.row_len: row_range_max = self.row_len - 1

            for row in range(row_range_min, row_range_max + 1):
                for ele in range(ele_range_min, ele_range_max + 1):
                    matrix.append((row, ele))

            if (star_row, star_ele) in matrix:
                count = count + 1
                gear_ratio = gear_ratio * arr_to_int(
                        self.schematic[each_row, each_ele_min: each_ele_max+1]
                        )

        if count == 2:
            return gear_ratio
        return 0        

    def get_gear_ratios(self):
        self.star_loc = self.get_star_loc()
        self.number_loc = self.get_number_loc()
        total = 0
        for star_row, star_ele in self.star_loc:
            total = total + self.is_gear(star_row, star_ele)
        
        return total


def main(argv):
    gear_ratios = GearRatios(argv[0])
    gear_ratios.print()
    ans = gear_ratios.get_gear_ratios()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
