import sys
import numpy as np


def get_scan(filepath):
    cave_scan = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            cave_scan.append(
                    line.replace(' ', '')
                    .strip()
                    .split('->')
                )

    return cave_scan


def convert_to_cord(cave_scan):
    cord_scan = []
    for scan in cave_scan:
        cord = []
        for point in scan:
            cord_x, cord_y = point.split(',')
            cord.append((int(cord_x), int(cord_y)))
        cord_scan.append(cord)

    return cord_scan


def get_scan_min_max(cave_scan):
    x_min = 500
    x_max = 500
    y_max = 0

    for scan in cave_scan:
        for point in scan:
            x, y = point
            if y > y_max: y_max = y
            if x > x_max: x_max = x
            if x < x_min: x_min = x

    return x_min, x_max, y_max


def create_picture(x_min, x_max, y_max, cord):
    picture = np.full((y_max + 1, x_max - x_min + 1),'.')
    origin = 500
    picture[0, origin - x_min] = '+'
    return picture


def print_picture(arr):
    r, c = np.shape(arr)
    for x in range(r):
        for y in range(c):
            print(arr[x, y], end=' ')
        print()


def main(argv):
    cave_scan = get_scan(argv[0])
    cave_scan = convert_to_cord(cave_scan)
    x_min, x_max, y_max = get_scan_min_max(cave_scan)
    print(cave_scan)
    print(x_min, x_max, y_max)
    picture = create_picture(x_min, x_max, y_max, None)
    print_picture(picture) 
    

if __name__ == '__main__':
    main(sys.argv[1:])
