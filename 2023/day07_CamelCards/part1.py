import sys

card_compare = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
        }

class CamelCards:
    def __init__(self, filepath):
        self.cards = []
        with open(filepath, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                placeholder = line.split(' ')
                self.cards.append(
                        {
                            "cards": placeholder[0],
                            "bid": int(placeholder[1])
                        }
                    )

        self.sorted_cards = self.sort(self.cards)

    def _type(self, x):
        if len(x) != 5: return -1
        placeholder = {}
        for each in x:
            if each in placeholder.keys():
                placeholder[each] += 1
            else:
                placeholder[each] = 1
        most = placeholder[max(placeholder, key=placeholder.get)]
        if most == 5: return 6 # Five of a Kind
        if most == 4: return 5 # Four of a Kind
        if most == 3 and len(placeholder) == 2: return 4 # Full House
        if most == 3 and len(placeholder) == 3: return 3 # Three of a Kind
        if most == 2 and len(placeholder) == 3: return 2 # Two Pair
        if most == 2 and len(placeholder) == 4: return 1 # One Pair
        if most == 1: return 0 # High Card
        # Something went wrong
        return -1

    def _compare(self, a, b):
        # return True if a is bigger or equal
        for i in range(len(a)):
            a_int = card_compare[a[i]]
            b_int = card_compare[b[i]]
            if a_int > b_int: return True
            elif a_int < b_int: return False
        return True

    def _first_bigger(self, a, b):
        # return True if a is bigger or equal
        a_type = self._type(a)
        b_type = self._type(b)
        if a_type > b_type: return True
        elif a_type < b_type: return False
        return self._compare(a, b)

    def sort(self, target):
        temp_target = target.copy()
        new_arr = []
        while len(temp_target):
            lowest = None
            for i in range(len(temp_target)):
                if lowest == None:
                    lowest = i
                if self._first_bigger(temp_target[lowest]['cards'], temp_target[i]['cards']):
                    lowest = i
            new_arr.append(temp_target[lowest])
            temp_target.pop(lowest)

        return new_arr

    def get_total_winnings(self):
        total = 0
        for i in range(len(self.sorted_cards)):
            total += self.sorted_cards[i]['bid'] * (i + 1)
        return total


def main(argv):
    camelcards = CamelCards(argv[0])
    ans = camelcards.get_total_winnings()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
