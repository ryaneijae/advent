import sys

class rucksack:
    def __init__(self, content):
        if (len(content) % 2) != 0:
            raise ValueError("Input String is not Even")
            return
        self.compartment_len = len(content) / 2
        self.left = content[:len(content)//2]
        self.right = content[len(content)//2:]

    def common(self):
        comm = []
        for i in self.left:
            for j in self.right:
                if (i == j) and (i not in comm): comm.append(i)
        return comm

    def priority(self):
        total = 0
        comm = self.common()
        for i in comm:
            if i.islower():
                total += ord(i) - 96
            else:
                total += ord(i) - 64 + 26
        return total

def main(argv):
    sum = 0
    with open(argv[0]) as file:
        for line in file.readlines():
            r = rucksack(line.strip())
            # print(r.common())
            # print(r.priority())
            sum += r.priority()
    print("Sum of Priorities: ", sum)

if __name__ == '__main__':
    main(sys.argv[1:])
