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

    def is_correct(self, a, l, b): 
        # Convert to binary then
        #    2 is concat
        #    1 is multiply
        #    0 is add
        # Should never happen
        if len(l) <= 1: sys.exit('Wrong list given')
        if b < 0: sys.exit('function called incorrectly')
        if 3**(len(l) - 1) <= b: sys.exit('function called incorrectly')

        ans = l[0]
        for i in range(len(l) - 2, -1, -1):
            digit = b // 3**i
            remainder = b % 3**i
            if digit == 1:
                ans = ans * l[len(l) - i - 1]
            elif digit == 0:
                ans += l[len(l) - i - 1]
            else:
                ans = int(str(ans) + str(l[len(l) - i- 1]))
            b = remainder

        if a == ans:
            return True
        return False

    def can_be_true(self, a, l):
        for i in range(3**(len(l) - 1)):
            if self.is_correct(a, l, i):
                return True
        return False

    def part2(self):
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
    print(b.part2())


if __name__ == '__main__':
    main(sys.argv[1:])
