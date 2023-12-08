import sys
import math

class FerryRace:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                raceinfo = line.split(':')
                if raceinfo[0] == 'Time':
                    self.time = raceinfo[-1].replace(' ', '')
                if raceinfo[0] == 'Distance':
                    self.distance = raceinfo[-1].replace(' ', '')

    def _remove_empty(self, target_list):
        while ('' in target_list):
            target_list.remove('')

    def calc_winning(self):
        t = int(self.time)
        d = int(self.distance)
        bottom = (t - math.sqrt(t * t - 4 * d)) / 2
        top = (t + math.sqrt(t * t - 4 * d)) / 2
            
        if bottom.is_integer():
            lower_bound = int(bottom + 1)
        else:
            lower_bound = int(math.ceil(bottom))

        if top.is_integer():
            upper_bound = int(top - 1)
        else:
            upper_bound = int(math.floor(top))

        return upper_bound - lower_bound + 1


def multiply_arr(arr):
    product = 1
    for item in arr:
        product = product * item

    return product


def main(argv):
    ferryrace = FerryRace(argv[0])
    ans = ferryrace.calc_winning()
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
