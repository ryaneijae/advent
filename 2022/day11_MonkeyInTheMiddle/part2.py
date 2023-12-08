import sys
import re
import my_logs
logger = my_logs.setup_logger(__name__)


def get_input(filepath):
    instructions = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            instructions.append(line.strip())

    return instructions


def text_chunks(text, size):
    return (text[chunk:chunk + size] for chunk in range(0, len(text), size))


class Monkey:
    def __init__(self, name=None, q=[], operand='', op_val=None,
                 test_value=None, if_true=None, if_false=None):
        self.name = name
        self.q = q
        self.operand = operand
        self.op_val = op_val
        self.test_value = test_value
        self.if_true = if_true
        self.if_false = if_false
        self.inspection = 0
        logger.debug(f"Creating Object {self}")


    def see(self, x):
        logger.debug(f"{self.name} sees {x}")
        self.inspection += 1
        if self.operand == '+':
            return x + int(self.op_val)
        elif self.operand == '*':
            if self.op_val == 'old':
                return x * x
            return x * int(self.op_val)
        else:
            sys.exit("Unexpected Operand")

    def do(self,x):
        if x % self.test_value == 0: 
            logger.debug(f"throwing {x} to {self.if_true}")
            return self.if_true, x
        else:
            logger.debug(f"throwing {x} to {self.if_false}")
            return self.if_false, x

    def __str__(self):
        return (f"{self.name}:\n"
                f"   Starting items: {self.q} \n"
                f"   Operating: new = old {self.operand} {self.op_val}\n"
                f"   Test: divisible by {self.test_value}\n"
                f"      If true: throw to {self.if_true}\n"
                f"      If false: throw to {self.if_false}"
                f"\n"
                )
            

def create_monkey(instructions):
    monkeys = {}
    for chunk in text_chunks(instructions, 7):
        name = chunk[0].replace(':', '')
        q = re.findall("(?<!\.)\d+(?!\.)", chunk[1])
        operand = re.findall("[+*]", chunk[2])[0]
        op_val = chunk[2].split(' ')[-1]
        test_value = int(chunk[3].split(' ')[-1])
        if_true = 'Monkey ' + chunk[4].split(' ')[-1]
        if_false = 'Monkey ' + chunk[5].split(' ')[-1]
        monkeys[name] = Monkey(
                name=name,
                q=q,
                operand=operand,
                op_val=op_val,
                test_value=test_value,
                if_true=if_true,
                if_false=if_false
            )
    return monkeys


def print_all_monkeys(monkeys):
    for monkey in monkeys:
        logger.debug(monkeys[monkey])


def get_least_multiple(monkeys):
    product = 1
    for monkey in monkeys:
        product = product * monkeys[monkey].test_value
    return product


def main(argv):
    instructions = get_input(argv[0])
    monkeys = create_monkey(instructions)
    calming = get_least_multiple(monkeys)
    rounds = 10000
    for each_round in range(1, rounds + 1):
        for monkey in monkeys:
            while monkeys[monkey].q:
                x = int(monkeys[monkey].q[0])
                monkeys[monkey].q.pop(0)
                x = monkeys[monkey].see(x)
                x = x % calming
                pass_to , x= monkeys[monkey].do(x)
                monkeys[pass_to].q.append(x)

    for monkey in monkeys:
        print(f"{monkeys[monkey].name} inspected items "
              f"{monkeys[monkey].inspection} times.")

if __name__ == '__main__':
    main(sys.argv[1:])
