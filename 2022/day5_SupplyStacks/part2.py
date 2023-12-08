import sys
import re


def get_instructions(filepath):
    instructions = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if 'move' in line:
                int_match = re.findall("(?<!\.)\d+(?!\.)", line)
                instructions.append([int(i) for i in int_match])
    
    return instructions


def get_original_state(filepath): # TODO: Need to figure out how to automate this.
    original_state = []
    if filepath == 'input/sample.txt':
        original_state = [
            ['Z', 'N'],
            ['M', 'C', 'D'],
            ['P']
        ]
    elif filepath == 'input/input.txt':
        original_state = [
            ['W', 'B', 'D', 'N', 'C', 'F', 'J'], #1
            ['P', 'Z', 'V', 'Q', 'L', 'S', 'T'], #2
            ['P', 'Z', 'B', 'G', 'J', 'T'], #3
            ['D', 'T', 'L', 'J', 'Z', 'B', 'H', 'C'], #4
            ['G', 'V', 'B', 'J', 'S'], #5
            ['P', 'S', 'Q'], #6
            ['B', 'V', 'D', 'F', 'L', 'M', 'P', 'N'], #7
            ['P', 'S', 'M', 'F', 'B', 'D', 'L', 'R'], #8
            ['V', 'D', 'T', 'R'] #9
        ]

    return original_state


def implement_instructions(original_state, instructions):
    state = original_state
    for i in instructions:
        move_from = i[1]
        move_to = i[2]
        move_number = i[0]
        temp_stack = []
        for j in range(move_number):
            temp_stack.append(state[move_from - 1].pop())
    
        for j in range(move_number):
            state[move_to - 1].append(temp_stack.pop())

    return state


def main(argv):
    final_state = implement_instructions(
            get_original_state(argv[0]),
            get_instructions(argv[0])
    )

    print([i[-1] for i in final_state])

if __name__ == '__main__':
    main(sys.argv[1:])
