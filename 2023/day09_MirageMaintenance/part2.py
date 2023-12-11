import sys

class Report:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.reading = []
            for line in f.readlines():
                placeholder = line.strip().split(' ')
                self.reading.append([int(x) for x in placeholder])

    def find_next(self, arr):
        done = True
        new_arr = []
        for i in range(len(arr) - 1):
            x = arr[i + 1] - arr[i]
            if x != 0: done = False
            new_arr.append(x)

        if done: return arr[-1]
        return self.find_next(new_arr) + arr[-1]

    def part1(self):
        total = 0
        for each in self.reading:
            x = self.find_next(each)
            total += x
        return total

    def find_previous(self, arr):
        done = True
        new_arr = []
        for i in range(len(arr) - 1):
            x = arr[i + 1] - arr[i]
            if x != 0: done = False
            new_arr.append(x)
        if done: return arr[0]
        return arr[0] - self.find_previous(new_arr)

    def part2(self):
        total = 0
        for each in self.reading:
            x = self.find_previous(each)
            total += x
        return total


def main(argv):
    report = Report(argv[0])
    ans = report.part2()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
