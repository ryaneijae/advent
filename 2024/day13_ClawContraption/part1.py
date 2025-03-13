import sys
import re

class ClawContraption:
    def __init__(self, filepath):
        self.claw = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                if 'Button A' in line:
                    Ax, Ay = re.findall(r'\d+', line)
                elif 'Button B' in line:
                    Bx, By = re.findall(r'\d+', line)
                elif 'Prize' in line:
                    Px, Py = re.findall(r'\d+', line)
                else:
                    self.claw.append((int(Ax), int(Bx), int(Px),
                                      int(Ay), int(By), int(Py)))
            self.claw.append((int(Ax), int(Bx), int(Px),
                              int(Ay), int(By), int(Py)))

    def solve(self, Ax, Bx, Px, Ay, By, Py):
        b = ((Px * Ay) - (Py * Ax)) / ((Ay * Bx) - (Ax * By))
        a = (Px - (Bx * b)) / Ax
        return a, b

    def part1(self):
        total = 0
        for e in self.claw:
            a, b = self.solve(*e)
            if a.is_integer() and b.is_integer():
                total += int(3 * a + b)
        return total


def main(argv):
    p = ClawContraption(argv[0])
    print(p.part1())


if __name__ == '__main__':
    main(sys.argv[1:])
