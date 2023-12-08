import pytest
from part1 import GearRatios

def test_GearRatios_is_partnumber():
    g = GearRatios('input/sample.txt')

    assert g.is_partnumber(0, 2, 0) == True
    assert g.is_partnumber(5, 7, 0) == False
    assert g.is_partnumber(2, 3, 2) == True
    assert g.is_partnumber(6, 8, 2) == True
    assert g.is_partnumber(0, 2, 4) == True
    assert g.is_partnumber(7, 8, 5) == False
    assert g.is_partnumber(2, 4, 6) == True
    assert g.is_partnumber(6, 8, 7) == True
    assert g.is_partnumber(1, 3, 9) == True
    assert g.is_partnumber(5, 7, 9) == True

def test_GearRatios_get_number_loc():

    answer = [(0, 2, 0), (5, 7, 0), (2, 3, 2), (6, 8, 2), (0, 2, 4), (7, 8, 5), (2, 4, 6), (6, 8, 7), (1, 3, 9), (5, 7, 9)]
    
    g = GearRatios('input/sample.txt')

    assert g.get_number_loc() == answer
