import sys
import numpy as np


pipe_map = {
        '|': {'n': True, 'w': False, 's': True, 'e': False},
        '-': {'n': False, 'w': True, 's': False, 'e': True},
        'L': {'n': True, 'w': False, 's': False, 'e': True},
        'J': {'n': True, 'w': True, 's': False, 'e': False},
        '7': {'n': False, 'w': True, 's': True, 'e': False},
        'F': {'n': False, 'w': False, 's': True, 'e': True},
        '.': {'n': False, 'w': False, 's': False, 'e': False},
}


class Maze:
    def __init__(self, filepath):
        maze = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                placeholder = line.strip()
                maze.append([x for x in placeholder])
        
        self.maze = np.array(maze)
        self.row_len, self.col_len = self.maze.shape

    def _print_maze(self):
        for row in self.maze:
            print(row)
        print(f'({self.row_len} x {self.col_len})')

    def find_start(self):
        for row_index in range(len(self.maze)):
            for col_index in range(len(self.maze[row_index])):
                if self.maze[row_index, col_index] == 'S':
                    return row_index, col_index

    def find_starting_direction(self, row, col):
        if row != 0:
            # Checking North
            checking = self.maze[row - 1, col]
            if pipe_map[checking]['s']: return 'n'
        if col != 0:
            # Checking West
            checking = self.maze[row, col - 1]
            if pipe_map[checking]['e']: return 'w'
        if row != self.row_len:
            # Checking South
            checking = self.maze[row + 1, col]
            if pipe_map[checking]['n']: return 's'
        if col != self.col_len:
            # Checking East
            checking = self.maze[row, col + 1]
            if pipe_map[checking]['w']: return 'e'
        sys.exit('Something went wrong!')

    def find_starting_shape(self, row, col):
        s = {
                'n': False,
                'w': False,
                's': False,
                'e': False
        }
        if row != 0:
            # Checking North
            checking = self.maze[row - 1, col]
            if pipe_map[checking]['s']: s['n'] = True
        if col != 0:
            # Checking West
            checking = self.maze[row, col - 1]
            if pipe_map[checking]['e']: s['w'] = True
        if row != self.row_len:
            # Checking South
            checking = self.maze[row + 1, col]
            if pipe_map[checking]['n']: s['s'] = True
        if col != self.col_len:
            # Checking East
            checking = self.maze[row, col + 1]
            if pipe_map[checking]['w']: s['e'] = True

        return s

    def find_next_pipe(self, last_row, last_col, direction):
        if direction == 'n':
            start = 's'
            row = last_row - 1
            col = last_col
        elif direction == 'w':
            start = 'e'
            row = last_row
            col = last_col - 1
        elif direction == 's':
            start = 'n'
            row = last_row + 1
            col = last_col
        else: # direction = 'e'
            start = 'w'
            row = last_row
            col = last_col + 1

        remaining_dir = ['n', 'w', 's', 'e']
        remaining_dir.remove(start)

        current = self.maze[row, col]

        for each_dir in remaining_dir:
            if pipe_map[current][each_dir]:
                return row, col, each_dir

        sys.exit('Pipe broken!')

    def find_pipes(self):
        self.pipes = []
        last_row, last_col = self.find_start()
        last_dir = self.find_starting_direction(last_row, last_col)
        pipe_map['S'] = self.find_starting_shape(last_row, last_col)

        while (last_row, last_col, last_dir) not in self.pipes:
            self.pipes.append((last_row, last_col, last_dir))
            last_row, last_col, last_dir = self.find_next_pipe(
                    last_row, last_col, last_dir
                    )

    def part1(self):
        self.find_pipes()
        return len(self.pipes) // 2


def main(argv):
    maze = Maze(argv[0])
    ans = maze.part1()
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])
