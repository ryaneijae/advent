import sys
import numpy as np

class Scratchcard:
    def __init__(self, card_info):
        card = card_info.split('|')
        self.winning_numbers = card[0].split(" ")
        self.numbers = card[-1].split(" ")

        self._remove_empty(self.winning_numbers)
        self._remove_empty(self.numbers)

        self.winning_numbers.sort()
        self.numbers.sort()

    def _remove_empty(self, target_list):
        while ('' in target_list):
            target_list.remove('')

    def get_matches(self):
        count = 0
        for winning_number in self.winning_numbers:
            if winning_number in self.numbers: count += 1
        return count

def main(argv):
    cards = {} 

    with open(argv[0], 'r') as f:
        for line in f.readlines():
            card_info = line.strip().split(":")
            cards[card_info[0].split(' ')[-1]] = Scratchcard(card_info[-1].strip())

    count = [1]*len(cards)
    for i in range(len(cards)):
        winning = cards[str(i + 1)].get_matches()
        for w in range(winning):
            count[i + w + 1] += count[i]

    print(sum(count))


if __name__ == '__main__':
    main(sys.argv[1:])
