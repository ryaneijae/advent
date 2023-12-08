import sys
import numpy as np


def get_map(filepath):
    tree_map = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            tree_map.append([int(i) for i in line.strip()])

    return np.array(tree_map)


def get_scenic_score(tree_map, row, col):
    row_max, col_max = tree_map.shape
    node_value = tree_map[row, col]

    if(
            (row == 0)
            or (col == 0)
            or (row == row_max - 1)
            or (col == col_max - 1)
        ): return 0

    # Left Value
    for i in range(col):
        left_score = i + 1
        if tree_map[row, col - (i + 1)] >= node_value: break

    # Right Value
    for i in range(col_max - (col + 1)):
        right_score = i + 1
        if tree_map[row, col + (i + 1)] >= node_value: break

    # Top Value
    for i in range(row):
        top_score = i + 1
        if tree_map[row - (i + 1), col] >= node_value: break

    # Bottom Value
    for i in range(row_max - (row + 1)):
        bottom_score = i + 1
        if tree_map[row + (i + 1), col] >= node_value: break

    return left_score * right_score * top_score * bottom_score


def main(argv):
    tree_map = get_map(argv[0])
    row_size, col_size = tree_map.shape
    highest = 0
    for r in range(row_size):
        for c in range(col_size):
            scenic_score = get_scenic_score(tree_map, r, c)
            if scenic_score > highest: highest = scenic_score
    
    print(highest)


if __name__ == '__main__':
    main(sys.argv[1:])
