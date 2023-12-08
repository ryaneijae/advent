import sys
import ast

def text_chunks(text, size):
    return (text[chunk:chunk + size] for chunk in range(0, len(text), size))


def get_distress_signal(filepath):
    distress_signal = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if line != '\n': 
                distress_signal.append(ast.literal_eval(line))
            else:
                distress_signal.append(None)
    return distress_signal


def compare_distress_signal(left_in, right_in):
    
    left = left_in.copy()
    right = right_in.copy()

    r = min(len(left), len(right))
    
    for i in range(r):
        if (type(left[i]) == int) and (type(right[i]) == int):
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True

        elif (type(left[i]) == list) and (type(right[i]) == list):
            check = compare_distress_signal(left[i], right[i])
            if check is None: continue
            elif check: return True
            else: return False

        else:
            if type(left[i]) == int:
                left[i] = [left[i]]
            elif type(right[i]) == int:
                right[i] = [right[i]]
            else:
                sys.exit("Something went wrong. Both are not int")

            check = compare_distress_signal(left[i], right[i])
            if check is None: continue
            elif check: return True
            else: return False

    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True

    return None


def remove_items(item_list, item):
    count = item_list.count(item)
    for i in range(count):
        item_list.remove(item)

    return item_list


def sort_distress_signal(distress_signal):
    # Remove Nones
    distress_signal = remove_items(distress_signal, None)

    size = len(distress_signal)
    print(f"Size of list: {size}")

    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if compare_distress_signal(
                    distress_signal[j],
                    distress_signal[min_index]
                ) is False:
                pass
            else:
                min_index = j
        hold = distress_signal[min_index]
        distress_signal[min_index] = distress_signal[i]
        distress_signal[i] = hold

    return distress_signal


def main(argv):

    distress_signal = get_distress_signal(argv[0])

    distress_signal.append([[2]])
    distress_signal.append([[6]])

    distress_signal = sort_distress_signal(distress_signal.copy())
    
    for i in range(len(distress_signal)):
        if distress_signal[i] == [[2]]:
            print(f"[[2]] found at {i + 1}")
            x = i + 1
        if distress_signal[i] == [[6]]:
            print(f"[[6]] found at {i + 1}")
            y = i + 1

    print(f"Decoder Key is {x * y}")


if __name__ == '__main__':
    main(sys.argv[1:])
