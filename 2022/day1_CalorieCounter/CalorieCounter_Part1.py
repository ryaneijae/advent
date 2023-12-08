import sys
from copy import copy

class Elf:
    def __init__(self):
        self.number = 0
        self.calories = 0

    def newFruit(self, c):
        self.number += 1
        self.calories += c

    def reset(self):
        self.number = 0
        self.calories = 0

def print_list(i_list):
    for i in range(len(i_list)):
        print(i_list[i].number, i_list[i].calories)

def main(argv):
    elves = []
    newElf = Elf()
    with open(argv[0]) as file:
        for line in file.readlines():
            if line.strip(): # line is not empty
                newElf.newFruit(int(line))
            else:
                elves.append(copy(newElf))
                newElf.reset()
        if newElf.number: # Add last Elf
            elves.append(copy(newElf))
    print("The following is the list of Elves with number of Fruit and number of calories")
    print_list(elves)

    print("~~~~~~~~Sorting~~~~~~~~~")
    elves.sort(key=lambda x: x.calories, reverse=True)
    print("The elf with the most amount of calories is carrying:")
    print("Fruits: ", elves[0].number, "  Calories: ", elves[0].calories)

if __name__ == '__main__':
    main(sys.argv[1:])
