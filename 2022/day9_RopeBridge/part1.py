import sys


def get_movement(filepath):
    movement = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            movement.append(line.split())
    
    return movement


def simulate_movement(movement):
    head_location = []
    head_x = 0
    head_y = 0
    head_location.append((head_x, head_y))

    tail_location = []
    tail_x = 0
    tail_y = 0
    tail_location.append((tail_x, tail_y))

    for instruction in movement:
        for i in range(int(instruction[1])):
            if instruction[0] == 'R': head_x += 1
            elif instruction[0] == 'L': head_x -= 1
            elif instruction[0] == 'U': head_y += 1
            elif instruction[0] == 'D': head_y -= 1
            else:
                sys.exit(f"Unexpected Direction {instruction[0]}")

            if (abs(head_x - tail_x) > 1) or (abs(head_y - tail_y) > 1):
                if head_x == tail_x: tail_y += int((head_y - tail_y) / 2)
                elif head_y == tail_y: tail_x += int((head_x - tail_x) / 2)
                else:
                    if abs(head_x - tail_x) == 1:
                        tail_x = head_x
                        tail_y += int((head_y - tail_y) / 2)
                    else:
                        tail_y = head_y
                        tail_x += int((head_x - tail_x) / 2)

            head_location.append((head_x, head_y))
            tail_location.append((tail_x, tail_y))
    
    return head_location, tail_location


def main(argv):
    movement = get_movement(argv[0])
    head_location, tail_location = simulate_movement(movement)

    tail_unique = set(tail_location)
    print(len(tail_unique))


if __name__ == '__main__':
    main(sys.argv[1:])
