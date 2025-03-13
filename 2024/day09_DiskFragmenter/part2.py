import sys
import re

class DiskFragmenter:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            line = ''.join(f.readlines())
            self.disk = line.strip()

    def expanded(self, l):
        expanded = []
        i = 0
        free = False
        for e in l:
            if free:
                for x in range(int(e)):
                    expanded.append('.')
            else:
                for x in range(int(e)):
                    expanded.append(str(i))
                i += 1
            free = not free
        return expanded

    def find_last(self, l):
        for i in range(len(l) - 1, -1, -1):
            if l[i] != '.':
                return i
        sys.exit('Not Possible')

    def compress(self, l):
        t = l.copy()
        for i in range(len(t)):
            if t[i] == '.':
                last = self.find_last(t)
                if last <= i: break
                t[i], t[last] = t[last], t[i]
        return t

    def find_spot(self, count, l):
        pattern = ''.join(['\\.' for i in range(count)])
        match = re.search(pattern, ''.join(l))
        if match:
            return match.start()
        return None
    
    def compress_whole(self, t):
        l = t.copy()
        l = [x for x in ''.join(l)]
        for x in range(9, -1, -1):
            i = len(l) - 1
            while i > 0:
                if l[i] == str(x):
                    count = 0
                    while l[i] == str(x):
                        count += 1
                        i += -1
                    place = self.find_spot(count, l)
                    i += 1
                    if place and place < i:
                        for j in range(count):
                            l[place + j], l[i + j] = l[i + j], l[place + j]
                i += -1
        return l

    def check_sum(self, l):
        total = 0
        for i in range(len(l)):
            if l[i] != '.':
                total += i * int(l[i])
        return total

    def part1(self):
        expanded = self.expanded(self.disk)
        compressed = self.compress(expanded)
        return self.check_sum(compressed)

    def part2(self):
        expanded = self.expanded(self.disk)
        print(''.join(expanded))
        compressed = self.compress_whole(expanded)
        print(''.join(compressed))
        return self.check_sum(compressed)


def main(argv):
    d = DiskFragmenter(argv[0])
    print(d.part2())

if __name__ == '__main__':
    main(sys.argv[1:])
