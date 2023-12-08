import sys

def common(l):
    initial_comm = []
    comm = []
    for i in l[0]:
        for j in l[1]:
            if (i == j) and (not i in initial_comm): initial_comm.append(i)
    for k in initial_comm:
        for x in l[2]:
            if (k == x) and (not k in comm): comm.append(k)
    return comm

def priority(l):
    total = 0
    badges = common(l)
    for i in badges:
        if i.islower():
            total += ord(i) - 96
        else:
            total += ord(i) - 64 + 26
    return total

def group_list(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i:i + n]

def main(argv):
    groups = []
    total = 0
    with open(argv[0]) as file:
        lines = [line.strip() for line in file]
        groups = list(group_list(lines, 3))
        for i in groups:
            print(i)
            total += priority(i)
    print("Sum of Priorities: ", total)

if __name__ == '__main__':
    main(sys.argv[1:])
