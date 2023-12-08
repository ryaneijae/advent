import pytest

from part1 import Tree


def test_tree_default_init():
    tree = Tree()

    assert tree.name == None
    assert tree.size == 0
    assert tree.children == []
    assert tree.parent == None


def test_tree_init_with_name():
    tree = Tree(name='example')

    assert tree.name == 'example'


def test_tree_init_with_node_size():
    tree = Tree(node_size=1234)

    assert tree.name == None
    assert tree.size == 1234
    assert tree.children == []
    assert tree.parent == None


def test_tree_set_name():
    tree = Tree()
    tree.name = 'example'

    assert tree.name == 'example'


def test_tree_total():
    tree = Tree(name='root')

    tree.children.append(Tree(name='child_1', node_size=1234))
    tree.children.append(Tree(name='child_dir'))
    tree.children[-1].children.extend((
            Tree(name='child_2', node_size=4321, parent='child_dir'),
            Tree(name='child_3', node_size=9876, parent='child_dir'),
            Tree(name='child_4', node_size=4567, parent='child_dir'),
        ))
    tree.children.append(Tree(name='child_5', node_size=2222))

    assert tree.total() == 22220


