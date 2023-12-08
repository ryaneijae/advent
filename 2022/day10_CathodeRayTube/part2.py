import sys


CRT = ['.'] * 240 

def get_instructions(filepath):
    instructions = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            instructions.append(line.split())

    return instructions


def increment_pc(pc, x):
    pc += 1
    sprite = pc % 40
    if (sprite == x) or (sprite == x + 1) or (sprite == x + 2):
        global CRT
        CRT[pc - 1] = '#'
    return pc


def simulate_computer(instructions):
    pc = 0
    x = 1
    for command in instructions:
        if command[0] == 'noop':
            pc = increment_pc(pc, x)
        elif command[0] == 'addx':
            pc = increment_pc(pc, x)
            pc = increment_pc(pc, x)
            x += int(command[1])


def main(argv):
    instructions = get_instructions(argv[0])
    simulate_computer(instructions)
    print(''.join(CRT[0:39]))
    print(''.join(CRT[40:79]))
    print(''.join(CRT[80:119]))
    print(''.join(CRT[120:159]))
    print(''.join(CRT[160:199]))
    print(''.join(CRT[200:239]))


if __name__ == '__main__':
    main(sys.argv[1:])
