import sys

def replace_digits(text):
    updated_text = text.strip()
    updated_text = updated_text.replace('1', 'one')
    updated_text = updated_text.replace('2', 'two')
    updated_text = updated_text.replace('3', 'three')
    updated_text = updated_text.replace('4', 'four')
    updated_text = updated_text.replace('5', 'five')
    updated_text = updated_text.replace('6', 'six')
    updated_text = updated_text.replace('7', 'seven')
    updated_text = updated_text.replace('8', 'eight')
    updated_text = updated_text.replace('9', 'nine')
    return updated_text

def find_calibration_value(text):
    output = []
    clean_text = replace_digits(text)
    for window_mid in range(len(clean_text)):
        window_start = window_mid - 2
        window_end = window_mid + 3
        if window_start < 0: window_start = 0
        if window_end > len(clean_text): window_end = len(clean_text)
        window = clean_text[window_start: window_end]
        if 'one' in window: output.append('1')
        if 'two' in window: output.append('2')
        if 'three' in window: output.append('3')
        if 'four' in window: output.append('4')
        if 'five' in window: output.append('5')
        if 'six' in window: output.append('6')
        if 'seven' in window: output.append('7')
        if 'eight' in window: output.append('8')
        if 'nine' in window: output.append('9')

    value = int(output[0]) * 10 + int(output[-1])
    return value

def main(argv):
    total = 0
    with open(argv[0], 'r') as f:
        for line in f.readlines():
            total = total + find_calibration_value(line)
    print(total)

if __name__ == '__main__':
    main(sys.argv[1:])
