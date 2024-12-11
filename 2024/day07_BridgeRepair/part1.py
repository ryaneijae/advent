import sys

class BridgeRepair:
    def __init__(self, filepath):
        self.equations = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                broken = line.strip().split(':')
                answer = broken[0]
                operands = broken[1].strip().split(' ')
                self.equations.append((int(answer), [int(x) for x in operands]))
        print(self.equations)

    def is_correct(self, a, l, b): # Convert to binary then 1 is multiply and 0 is add
        # Should never happen
        if len(l) <= 1: sys.exit('Wrong list given')
        if b < 0: sys.exit('function called incorrectly')
        if 2**(len(l) - 1) <= b: sys.exit('function called incorrectly')

        ans = l[0]
        for i in range(len(l) - 2, 0, -1):
            if b >= 2**i:
                ans = ans * l[len(l) - i - 1]
                b = b - 2**i
            else:
                ans += l[len(l) - i - 1]    
        if b == 1:
            ans = ans * l[-1]
        elif b == 0:
            ans += l[-1]
        else:
            sys.exit('Math was wrong')

        if a == ans:
            return True
        return False

    def can_be_true(self, a, l):
        for i in range(2**(len(l)-1)):
            if self.is_correct(a, l, i):
                return True
        return False

    def part1(self):
        total = 0
        for e in self.equations:
            if self.can_be_true(e[0], e[1]):
                print(f'{e[0]}, {e[1]} is True')
                total += e[0]
            else:
                print(f'{e[0]}, {e[1]} is False')
        return total

def main(argv):
    b = BridgeRepair(argv[0])
    print(b.part1())


if __name__ == '__main__':
    main(sys.argv[1:])
