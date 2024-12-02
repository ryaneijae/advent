import sys


class RedNoseReport:
    def __init__(self, filepath):
        self.reports = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                self.reports.append(line.strip().split(' '))

    def check(self, l): # if safe, return True. Else, return False
        if len(set(l)) != len(l):
            return False
        if sorted(l) != l and sorted(l) != l[::-1]:
            return False
        for i in range(len(l) - 1):
            if abs(l[i] - l[i + 1]) > 3:
                return False
        return True

    def part1(self):
        total = 0
        for l in self.reports:
            int_l = [int(x) for x in l]
            if self.check(int_l):
                total += 1
        return total


def main(argv):
    r = RedNoseReport(argv[0])
    print(r.part1())


if __name__ == '__main__':
    main(sys.argv[1:])
