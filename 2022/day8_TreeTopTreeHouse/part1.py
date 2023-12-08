import sys
import numpy as np


def get_map(filepath):
    tree_map = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            tree_map.append([int(i) for i in line.strip()])

    return np.array(tree_map)


def is_visible(tree_map, row, col):
    row_max, col_max = tree_map.shape
    node_value = tree_map[row, col]
    # Check if its edge
    if (
            (row == 0)
            or (col == 0)
            or (row == row_max - 1)
            or (col == col_max - 1)
        ): return True
    
    # Check left
    if np.amax(tree_map[row, :col ]) < node_value: return True
    
    # Check right
    if np.amax(tree_map[row, col + 1:]) < node_value: return True
    
    # Check top
    if np.amax(tree_map[:row, col]) < node_value: return True

    # Check bottom
    if np.amax(tree_map[row + 1:, col]) < node_value: return True

    return False

    

def count_visible(tree_map):
    total = 0
    row_size, col_size = tree_map.shape
    for r in range(row_size):
        for c in range(col_size):
            if is_visible(tree_map, r, c): total += 1

    return total


def main(argv):
    tree_map = get_map(argv[0])
    print(count_visible(tree_map))


if __name__ == '__main__':
    main(sys.argv[1:])
