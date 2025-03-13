import sys

lookup = {
    1: {'U': 1,
        'L': 1,
        'D': 4,
        'R': 2},
    2: {'U': 2,
        'L': 1,
        'D': 5,
        'R': 3},
    3: {'U': 3,
        'L': 2,
        'D': 6,
        'R': 3},
    4: {'U': 1,
        'L': 4,
        'D': 7,
        'R': 5},
    5: {'U': 2,
        'L': 4,
        'D': 8,
        'R': 6},
    6: {'U': 3,
        'L': 5,
        'D': 9,
        'R': 6},
    7: {'U': 4,
        'L': 7,
        'D': 7,
        'R': 8},
    8: {'U': 5,
        'L': 7,
        'D': 8,
        'R': 9},
    9: {'U': 6,
        'L': 8,
        'D': 9,
        'R': 9},
        }

class BathroomSecurity:
    def __init__(self, filepath):
        self.password = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.password.append(line.strip())
        print(self.password)

    def get_code(self, l, current):
        for i in range(len(l)):
            moving = lookup[current]
            current = moving[l[i]]
        return current
    
    def part1(self):
        current = 5
        password = ''
        for p in self.password:
            current = self.get_code(p, current)
            password += str(current)
        return password

def main(argv):
    b = BathroomSecurity(argv[0])
    print(b.part1())

if __name__ == '__main__':
    main(sys.argv[1:])
