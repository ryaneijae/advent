import sys
import numpy as np


class HotSpring:
    def __init__(self, filepath):
        self.hotsprings = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                each_line = line.strip().split(' ')
                status = each_line[0]
                answer = each_line[-1].split(',')
                self.hotsprings.append([status, answer])
        self._print()

    def _print(self):
        for row in self.hotsprings:
            print(f'{row[0]} {row[1]}')

    def simplify(self, status):
        ret = []
        for i in range(len(status)):
            if ret == []:
                if status[i] != '.':
                    ret.append(status[i])
                continue
            if ret[-1] == '.' and status[i] == '.':
                continue
            ret.append(status[i])
        if ret == []: return '.'
        if ret[0] == '.': ret = ret[1 : ]
        if ret[-1] == '.': ret = ret[0 : -1]
        return ''.join(ret)

    def get_answer(self, criteria):
        ans = []
        for each in criteria:
            x = int(each)
            placeholder = ['#'] * x
            placeholder.append('.')
            ans.append(''.join(placeholder))
        ans = ''.join(ans)
        if ans[-1] == '.': ans = ans[0 : -1]
        return ans

    def arrangements(self, status, answer):
        simple_status = self.simplify(status)
        if '?' not in simple_status:
            if simple_status == answer:
                return 1
            return 0

        i = simple_status.index('?')
        damaged = list(simple_status)
        damaged[i] = '#'
        operational = list(simple_status)
        operational[i] = '.'
        return (
            self.arrangements(''.join(damaged), answer)
            + self.arrangements(''.join(operational), answer)
        )

    def part1(self):
        total = 0
        for row in self.hotsprings:
            print(f'Checking {row}')
            arrangements = self.arrangements(row[0], self.get_answer(row[1]))
            print(f'Returned {arrangements}')
            total += arrangements
        return total

def main(argv):
    hotspring = HotSpring(argv[0])
    ans = hotspring.part1()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
