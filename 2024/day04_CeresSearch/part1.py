import sys

class CeresSearch:
    def __init__(self, filepath):
        self.target = 'XMAS'
        self.target_len = len(self.target)

        self.grid = []

        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.grid.append(line.strip())
        
        self.rowc = len(self.grid)
        self.colc = len(self.grid[0])
       
        self._print_grid()

    def _print_grid(self):
        for line in self.grid:
            print(' '.join(line))
        print()
        print(f'{self.rowc} rows x {self.colc} cols')
        print()

    def find_and_reverse(self, s):
        print(f'Looking in {s}')
        total = 0
        if self.target in s:
            print('found')
            total += 1
        if self.target in s[::-1]:
            print('found reverse')
            total += 1
        return total

    def check_hor(self, r, c):
        col_min = max(0, c - self.target_len + 1)
        col_max = min(self.colc, c + self.target_len)
        return self.find_and_reverse(self.grid[r][col_min : col_max])
            
    def check_ver(self, r, c):
        temp_string = ''.join([row[c] for row in self.grid])
        row_min = max(0, r - self.target_len + 1)
        row_max = min(self.rowc, r + self.target_len)
        return self.find_and_reverse(temp_string[row_min : row_max])

    def check_diag(self, r, c):
        total = 0

        # Top Left to Bottom Right
        temp_string = ''
        col_min = c - self.target_len + 1
        row_min = r - self.target_len + 1
        while col_min < 0 or row_min < 0:
            col_min += 1
            row_min += 1
        col_max = c + self.target_len
        row_max = r + self.target_len
        while col_max > self.colc or row_max > self.rowc:
            col_max -= 1
            row_max -= 1
        for i in range(row_max - row_min):
            temp_string += self.grid[row_min + i][col_min + i]
        total += self.find_and_reverse(temp_string)

        # Top Right to Bottom Left
        temp_string = ''
        col_min = c - self.target_len + 1
        row_max = r + self.target_len
        while col_min < 0 or row_max > self.rowc:
            col_min += 1
            row_max -= 1
        col_max = c + self.target_len
        row_min = r - self.target_len + 1
        while col_max > self.colc or row_min < 0:
            col_max -= 1
            row_min += 1
        print(f'col: {col_min}, {col_max}  row: {row_min}, {row_max}')
        for i in range(row_max - row_min):
            temp_string += self.grid[row_min + i][col_max - i - 1]
        print(temp_string)
        total += self.find_and_reverse(temp_string)

        return total


    def check(self, r, c):
        return self.check_hor(r, c) + self.check_ver(r, c) + self.check_diag(r, c)

    def part1(self):
        total = 0
        for r in range(self.rowc):
            for c in range(self.colc):
                if self.grid[r][c] == 'X':
                    print(f'Checking {r}, {c}')
                    total += self.check(r, c)
        return total

def main(argv):
    c = CeresSearch(argv[0])
    print(c.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
