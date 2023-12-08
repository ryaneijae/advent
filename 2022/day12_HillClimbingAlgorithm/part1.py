import sys
import os
import numpy as np


def get_height_map(filepath):
    height_map = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            height_map.append([i for i in line.strip()])

    return np.array(height_map)


def print_map(height_map, searching):
    row_size, col_size = height_map.shape
    for r in range(row_size):
        for c in range(col_size):
            if (r, c) in searching:
                print(height_map[r, c].upper(), end=' ')
            else:
                print(height_map[r, c], end=' ')
        print()
    print()


def get_start_and_end(height_map):
    row_size, col_size = height_map.shape
    for r in range(row_size):
        for c in range(col_size):
            if height_map[r, c] == 'S': start = (r, c)
            if height_map[r, c] == 'E': end = (r, c)

    return start, end


def char_compare(a, b, n=1):
    if ord(a) - ord(b) <= n:
        return True
    return False


def find_shortest_path(height_map):
    start, end = get_start_and_end(height_map)
    row_size, col_size = height_map.shape
    height_map[start] = 'a'
    height_map[end] = 'z'
    shortest = 0
    found = False
    searching = set()
    searching.add((end))
    stop_checking = set()
    while not found:
        to_add = []
        for each in searching:
            if each in stop_checking: continue
            each_x, each_y = each
            current = height_map[each]
            each_add = []
            # add top if close
            if each_x != 0:
                if char_compare(current, height_map[each_x - 1, each_y]):
                    each_add.append((each_x - 1, each_y))

            # add bottom if close
            if each_x != row_size - 1:
                if char_compare(current, height_map[each_x + 1, each_y]):
                    each_add.append((each_x + 1, each_y))

            # add left if close
            if each_y != 0:
                if char_compare(current, height_map[each_x, each_y - 1]):
                    each_add.append((each_x, each_y - 1))

            # add right if close
            if each_y != col_size - 1:
                if char_compare(current, height_map[each_x, each_y + 1]):
                    each_add.append((each_x, each_y + 1))


            if set(each_add) <= searching: stop_checking.add((each))
            to_add.extend(each_add)
        
        searching.update(to_add)
        shortest += 1
        if start in searching: found = True

    return shortest



def main(argv):
    height_map = get_height_map(argv[0])
    shortest = find_shortest_path(height_map)
    print(f"Shortest path {shortest}")

if __name__ == '__main__':
    main(sys.argv[1:])
