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
                distress_signal.append([])
    return distress_signal


def compare_distress_signal(left, right):
    print(f"Comparing {left} and {right}")
    r = min(len(left), len(right))
    
    for i in range(r):
        if (type(left[i]) == int) and (type(right[i]) == int):
            print(f"Both {left[i]} and {right[i]} are ints")
            if left[i] > right[i]:
                print(f"Right is smaller. Returning False")
                return False
            elif left[i] < right[i]:
                print(f"Left is smaller. Returning True")
                return True
            print("They are equal.")

        elif (type(left[i]) == list) and (type(right[i]) == list):
            print(f"Both {left[i]} and {right[i]} are lists")
            check = compare_distress_signal(left[i], right[i])
            if check is None: continue
            elif check: return True
            else: return False

        else:
            if type(left[i]) == int:
                print("Converting Left")
                left[i] = [left[i]]
            elif type(right[i]) == int:
                print("Converting Right")
                right[i] = [right[i]]
            else:
                sys.exit("Something went wrong. Both are not int")

            print(f"Both {left[i]} and {right[i]} are now lists")
            check = compare_distress_signal(left[i], right[i])
            if check is None: continue
            elif check: return True
            else: return False

    if len(left) > len(right):
        print("Right Side ran out. Returning False")
        return False
    elif len(left) < len(right):
        print("Left Side ran out. Returning True")
        return True

    return None


def main(argv):

    distress_signal = get_distress_signal(argv[0])
    pair = 1
    total = 0
    for chunk in text_chunks(distress_signal, 3):
        
        check = compare_distress_signal(chunk[0], chunk[1])
        if check is False:
            print(f"Pair {pair}: Not Right Order")
        else:
            print("Check was None")
            print(f"Pair {pair}: Right Order")
            total += pair
        print()
        pair += 1


    print(f"Sum of indices: {total}")


if __name__ == '__main__':
    main(sys.argv[1:])
