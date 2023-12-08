import sys


def get_signal_start(message):
    for checking in range(len(message)):
        target = list(message[ checking : checking + 4 ])
        if len(target) == len(set(target)): break
        else: checking += 1

    return checking + 4


def main(argv):
    with open(argv[0], 'r') as f:
        for line in f.readlines():
            message_start = get_signal_start(line)
            print(f"{line.strip()}: first marker after character {message_start}")


if __name__ == '__main__':
    main(sys.argv[1:])
