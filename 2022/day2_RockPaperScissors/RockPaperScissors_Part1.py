import sys

def RPS_points(opponent, you):
    loss = 0
    draw = 3
    win = 6
    rock = 1
    paper = 2
    scissor = 3
    if opponent == "Rock":
        if you == "Rock": return draw + rock
        elif you == "Paper": return win + paper
        elif you == "Scissors": return loss + scissor
    elif opponent == "Paper":
        if you == "Rock": return loss + rock
        elif you == "Paper": return draw + paper
        elif you == "Scissors": return win + scissor
    elif opponent == "Scissors":
        if you == "Rock": return win + rock
        elif you == "Paper": return loss + paper
        elif you == "Scissors": return draw + scissor
    raise ValueError("Unexpected Input Received")
    return

def interpretation(i):
    if i == "A": return "Rock"
    elif i == "B": return "Paper"
    elif i == "C": return "Scissors"
    elif i == "X": return "Rock"
    elif i == "Y": return "Paper"
    elif i == "Z": return "Scissors"
    else:
        raise ValueError("Unexpected Input Received")
    return

def main(argv):
    total = 0
    with open(argv[0]) as file:
        for line in file.readlines():
            # print("Printing 0 and 2: ", line[0], line[2])
            points = RPS_points(interpretation(line[0]), interpretation(line[2]))
            total += points
            # print("Current round points: ", points)
            # print("Printing current total ", total)
    print("Total Score: ", total)

if __name__ == '__main__':
    main(sys.argv[1:])
