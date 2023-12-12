import pytest
import part1

def test_in_between_happy():
    assert part1.in_between(0, 5, 2) == True
    assert part1.in_between(0, 50000, 2000) == True
    assert part1.in_between(1000000000,2000000000, 1000000001) == True
    assert part1.in_between(0, 10, 0) == True
    assert part1.in_between(0, 10, 10) == True
    assert part1.in_between(0, -5, -2) == True
    assert part1.in_between(-100, 100, 0) == True
    assert part1.in_between(-1000, 5000, 2) == True
    assert part1.in_between(-100, 10, -94) == True

def test_in_between_reverse():
    assert part1.in_between(5, 0, 2) == True
    assert part1.in_between(50000, 0, 2000) == True
    assert part1.in_between(2000000000,1000000000, 1000000001) == True
    assert part1.in_between(10, 0, 0) == True
    assert part1.in_between(10, 00, 10) == True
    assert part1.in_between(-5, 0, -2) == True
    assert part1.in_between(100, -100, 0) == True
    assert part1.in_between(5000, -1000, 2) == True
    assert part1.in_between(10, -100, -94) == True

def test_in_between_negative():
    assert part1.in_between(0, 5, -1) == False
    assert part1.in_between(50000, 0, -2000) == False
    assert part1.in_between(2000000000,1000000000, 999999999) == False

