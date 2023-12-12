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


def intersection(a, b):
    c = [value for value in a if value in b]
    return c


class Maze:
    def __init__(self, filepath):
        maze = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                placeholder = line.strip()
                maze.append([x for x in placeholder])
        
        self.maze = np.array(maze)
        self.row_len, self.col_len = self.maze.shape

    def _print_maze(self, arr):
        print(np.matrix(arr))
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

    def _surrounded(self, row, col):
        if row <= 0 or col <= 0 or row >= self.row_len - 1 or col >= self.col_len - 1:
            return False
        
        checking = [(x, col) for x in range(row)]
        if not intersection(checking, self.just_pipe): 
            return False
        
        checking = [(x, col) for x in range(row + 1, self.row_len)]
        if not intersection(checking, self.just_pipe):
            return False
        
        checking = [(row, x) for x in range(col)]
        if not intersection(checking, self.just_pipe):
            return False
        
        checking = [(row, x) for x in range(col + 1, self.col_len)]
        if not intersection(checking, self.just_pipe):
            return False
        
        return True

    def _count(self, row, col):
        checking = []
        for i in range(self.row_len):
            checking.append((i, col))

        for i in range(self.col_len):
            checking.append((row, i))

        checking.remove((row, col))
        checking.remove((row, col))
        x = intersection(checking, self.just_pipe)
        print(row, col, x)
        print(len(x))
        return len(x)

    def part2(self):
        self.find_pipes()
        
        self.new_maze = self.maze.copy()
        
        self.just_pipe = []
        
        for r, c, d in self.pipes:
            self.just_pipe.append((r, c))
        
        for row in range(self.row_len):
            for col in range(self.col_len):
                if (row, col) not in self.just_pipe:
                    if self._surrounded(row, col):
                        self.new_maze[row, col] = self._count(row, col)
                    else:
                        self.new_maze[row, col] = '.'

        

        self._print_maze(self.new_maze)
        


def main(argv):
    maze = Maze(argv[0])
    ans = maze.part2()
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])
