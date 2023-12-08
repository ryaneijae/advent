import sys


signal_strength = 0

def get_instructions(filepath):
    instructions = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            instructions.append(line.split())

    return instructions

def increment_pc(pc, x):
    pc += 1
    print_list = [20, 60, 100, 140, 180, 220]
    if pc in print_list:
        print(f"pc: {pc}, register X: {x}")
        global signal_strength
        signal_strength += pc * x
        print(f"Signal Strength: {signal_strength}")
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


if __name__ == '__main__':
    main(sys.argv[1:])
