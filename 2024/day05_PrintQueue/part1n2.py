import sys

class PrintQueue:
    def __init__(self, filepath):
        self.rules = []
        self.update = []
        with open(filepath, 'r') as f:
            is_update = False
            for line in f.readlines():
                if line == '\n':
                    is_update = True
                elif is_update:
                    page = line.strip()
                    self.update.append(page.split(','))
                else:
                    rule = line.strip()
                    self.rules.append(rule.split('|'))

    def is_sorted(self, order):
        for rule in self.rules:
            if rule[0] in order and rule[1] in order:
                if order.index(rule[0]) >= order.index(rule[1]):
                    return False
        return True

    def swap(self, l, i, j):
        holder = l[i]
        l[i] = l[j]
        l[j] = holder

    def sort(self, order):
        o = order.copy()
        while not self.is_sorted(o):
            for rule in self.rules:
                if rule[0] in o and rule[1] in o:
                    if o.index(rule[0]) >= o.index(rule[1]):
                        self.swap(o, o.index(rule[0]), o.index(rule[1]))
        return o

    def part1(self):
        total = 0
        for order in self.update:
            if self.is_sorted(order):
                total += int(order[len(order) // 2])
        return total

    def part2(self):
        total = 0
        for order in self.update:
            if not self.is_sorted(order):
                sorted_o = self.sort(order)
                total += int(sorted_o[len(sorted_o) // 2])
        return total


def main(argv):
    p = PrintQueue(argv[0])
    print(p.part1())
    print(p.part2())


if __name__ == '__main__':
    main(sys.argv[1:])
