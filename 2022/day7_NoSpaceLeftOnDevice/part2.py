import sys
import my_logs
logger = my_logs.setup_logger(__name__)

class Tree:
    def __init__(self, name=None, node_size=0, parent=None):
        self.name = name
        self.size = node_size
        self.children = []
        self.parent = parent

    def total(self):
        if self.size != 0:
            return self.size
        
        return sum([i.total() for i in self.children])

    def get_file_type(self):
        if self.size == 0:
            return 'dir'

        return 'file'

    def __str__(self, lvl=0):
        output = (
            '  ' * lvl
            + '- '
            + repr(self.name)
            + f"({self.get_file_type()}, Size={self.total()})"
            + '\n'
        )

        for child in self.children:
            output += child.__str__(lvl + 1)

        return output

    def __repr__(self):
        return '<tree representation>'


def parse_and_build(filepath):
    files = {}
    current_dir = None
    files['root'] = Tree(name='root')
    with open(filepath, 'r') as f:
        for line in f.readlines():
            if '$ cd' in line:
                parse_line = line.split()
                if parse_line[-1] == '/':
                    current_dir = 'root'
                elif parse_line[-1] == '..':
                    current_dir = files[current_dir].parent
                else: 
                    current_dir = current_dir + '/' + parse_line[-1]
            elif '$ ls' in line:
                pass
            else:
                parse_line = line.split()
                if 'dir' in parse_line[0]:
                    files[current_dir + '/' + parse_line[1]] = Tree(
                            name=current_dir + '/' + parse_line[1],
                            parent=current_dir
                        )
                    files[current_dir].children.append(files[current_dir + '/' + parse_line[1]])
                else:
                    files[current_dir + '/' + parse_line[1]] = Tree(
                            name=current_dir + '/' + parse_line[1],
                            node_size=int(parse_line[0]),
                            parent=current_dir
                        )
                    files[current_dir].children.append(files[current_dir + '/' + parse_line[1]])

    logger.debug("Returning the following")
    logger.debug(files['root'])
    logger.debug(files)
    return files


def main(argv):
    files = parse_and_build(argv[0])
    print(files['root'])
    root_size = files['root'].total()
    total_size = 70000000
    current_free = total_size - root_size
    need_size = 30000000
    need_to_free = need_size - current_free
    print(need_to_free)
    sum = 0
    for item in files:
        if files[item].get_file_type() == 'dir':
            if files[item].total() >= need_to_free:
                print(f"Found directory ({files[item].name}) with more than {need_to_free} as size: {files[item].total()}")
                sum += files[item].total()

    print(f"Total: {sum}")


if __name__ == '__main__':
    main(sys.argv[1:])
