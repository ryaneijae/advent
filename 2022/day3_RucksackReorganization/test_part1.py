import pytest
from part1 import rucksack

def test_default_initial_rucksack():
    r = rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert r.compartment_len == 12
    assert r.left == "vJrwpWtwJgWr"
    assert r.right == "hcsFMMfFFhFp"

def test_error_default_initial_rucksack():
    with pytest.raises(ValueError):
        r = rucksack("ABCDE")

def test_common_rucksack():
    r = rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert r.common() == ['p']

    q = rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert q.common() == ['L']

def test_priority_rucksack():
    r = rucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    assert r.priority() == 16
    q = rucksack("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
    assert q.priority() == 38
