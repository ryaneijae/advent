import pytest
import part1

def test_decypher():
    line = "34-41,33-1000"
    assert part1.decypher(line) == [34, 41, 33, 1000]

    line2 = "36-8,100-85"
    assert part1.decypher(line2) == [36, 8, 100, 85]

def test_isvalid():
    line = [34, 41, 33, 1000]
    line2 = [36, 1, 44, 100]
    line3 = [1, 1, 3, 3]
    assert part1.isvalid(line) == True
    assert part1.isvalid(line2) == False
    assert part1.isvalid(line3) == True

def test_isFullyContained():
    line = [34, 41, 33, 1000]
    line2 = [1, 1, 3, 3]

    assert part1.isFullyContained(line) == True
    assert part1.isFullyContained(line2) == False
