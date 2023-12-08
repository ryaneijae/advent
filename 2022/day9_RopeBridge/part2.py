import sys


def get_movement(filepath):
    movement = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            movement.append(line.split())
    
    return movement

def head_change(direction, head_x, head_y):
    if direction == 'R': head_x += 1
    elif direction == 'L': head_x -= 1
    elif direction == 'U': head_y += 1
    elif direction == 'D': head_y -= 1
    else:
        sys.exit(f"Unexpected Direction {direction}")

    return head_x, head_y


def tail_change(head_x, head_y, tail_x, tail_y):
    if (abs(head_x - tail_x) > 1) or (abs(head_y - tail_y) > 1):
        if head_x == tail_x: tail_y += int((head_y - tail_y) / 2)
        elif head_y == tail_y: tail_x += int((head_x - tail_x) / 2)
        else:
            if abs(head_x - tail_x) == 1:
                tail_x = head_x
                tail_y += int((head_y - tail_y) / 2)
            elif abs(head_y - tail_y) == 1:
                tail_y = head_y
                tail_x += int((head_x - tail_x) / 2)
            else:
                tail_x += int((head_x - tail_x) / 2)
                tail_y += int((head_y - tail_y) / 2)

    return tail_x, tail_y


def simulate_movement(movement):
    head_location = []
    head_x = 0
    head_y = 0
    head_location.append((head_x, head_y))
   
    knot_1_x = 0
    knot_1_y = 0
    knot_2_x = 0
    knot_2_y = 0
    knot_3_x = 0
    knot_3_y = 0
    knot_4_x = 0
    knot_4_y = 0
    knot_5_x = 0
    knot_5_y = 0
    knot_6_x = 0
    knot_6_y = 0
    knot_7_x = 0
    knot_7_y = 0
    knot_8_x = 0
    knot_8_y = 0

    tail_location = []
    tail_x = 0
    tail_y = 0
    tail_location.append((tail_x, tail_y))

    for instruction in movement:
        for i in range(int(instruction[1])):
            head_x, head_y = head_change(instruction[0], head_x, head_y)
            knot_1_x, knot_1_y = tail_change(head_x, head_y, knot_1_x, knot_1_y)
            knot_2_x, knot_2_y = tail_change(knot_1_x, knot_1_y, knot_2_x, knot_2_y)
            knot_3_x, knot_3_y = tail_change(knot_2_x, knot_2_y, knot_3_x, knot_3_y)
            knot_4_x, knot_4_y = tail_change(knot_3_x, knot_3_y, knot_4_x, knot_4_y)
            knot_5_x, knot_5_y = tail_change(knot_4_x, knot_4_y, knot_5_x, knot_5_y)
            knot_6_x, knot_6_y = tail_change(knot_5_x, knot_5_y, knot_6_x, knot_6_y)
            knot_7_x, knot_7_y = tail_change(knot_6_x, knot_6_y, knot_7_x, knot_7_y)
            knot_8_x, knot_8_y = tail_change(knot_7_x, knot_7_y, knot_8_x, knot_8_y)
            tail_x, tail_y = tail_change(knot_8_x, knot_8_y, tail_x, tail_y)

            head_location.append((head_x, head_y))
            tail_location.append((tail_x, tail_y))

    print(f"head: {head_x}, {head_y}")
    print(f"2: {knot_2_x}, {knot_2_y}")
    print(f"3: {knot_3_x}, {knot_3_y}")
    print(f"4: {knot_4_x}, {knot_4_y}")
    print(f"5: {knot_5_x}, {knot_5_y}")
    print(f"6: {knot_6_x}, {knot_6_y}")
    print(f"7: {knot_7_x}, {knot_7_y}")
    print(f"8: {knot_8_x}, {knot_8_y}")
    print(f"tail: {tail_x}, {tail_y}")

    
    return head_location, tail_location


def main(argv):
    movement = get_movement(argv[0])
    head_location, tail_location = simulate_movement(movement)

    tail_unique = set(tail_location)
    print(len(tail_unique))


if __name__ == '__main__':
    main(sys.argv[1:])
