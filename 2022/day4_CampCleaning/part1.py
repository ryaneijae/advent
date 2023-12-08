import sys

def decypher(line):
    line = line.replace("-", ',')
    assignment = line.split(",")
    int_assignment = [eval(i) for i in assignment]
    return int_assignment

def isvalid(l):
    if (l[0] > l[1]) or (l[2] > l[3]): return False
    return True

def isFullyContained(l):
    if (l[0] <= l[2]) and (l[1] >= l[3]): return True # First Assignment Contains Second Assignment
    if (l[0] >= l[2]) and (l[1] <= l[3]): return True # Second Assignment Contains the First Assignment
    return False

def main(argv):
    with open(argv[0]) as file:
        count = 0
        for line in file.readlines():
            assignment = decypher(line.strip())
            if not isvalid(assignment): raise ValueError("Assignment range seems incorrect.")
            if isFullyContained(assignment):
                count += 1
        print("Total complete overlap is: ", count)

if __name__ == '__main__':
    main(sys.argv[1:])
