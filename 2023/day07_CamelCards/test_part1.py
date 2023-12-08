import pytest
from part1 import CamelCards

filepath = 'input/sample.txt'

five_a_kind = 'AAAAA'
four_a_kind = 'AAAAK'
full_house = 'AAAKK'
three_a_kind = 'AAAKQ'
two_pair = 'AAKKQ'
pair = 'AAKQJ'
high_card = 'AKQJT'

def test_CamelCards_type():
    c = CamelCards(filepath)

    assert c._type(five_a_kind) == 6
    assert c._type(four_a_kind) == 5
    assert c._type(full_house) == 4
    assert c._type(three_a_kind) == 3
    assert c._type(two_pair) == 2
    assert c._type(pair) == 1
    assert c._type(high_card) == 0
    assert c._type('12345') == 0
    assert c._type('ABCD') == -1
    assert c._type('ABCDE1') == -1

def test_CamelCards_first_bigger():
    c = CamelCards(filepath)

    assert c._first_bigger(five_a_kind, five_a_kind) == True
    assert c._first_bigger(five_a_kind, four_a_kind) == True
    assert c._first_bigger(five_a_kind, full_house) == True
    assert c._first_bigger(five_a_kind, three_a_kind) == True
    assert c._first_bigger(five_a_kind, two_pair) == True
    assert c._first_bigger(five_a_kind, pair) == True
    assert c._first_bigger(five_a_kind, high_card) == True

    assert c._first_bigger(four_a_kind, five_a_kind) == False
    assert c._first_bigger(four_a_kind, four_a_kind) == True
    assert c._first_bigger(four_a_kind, full_house) == True
    assert c._first_bigger(four_a_kind, three_a_kind) == True
    assert c._first_bigger(four_a_kind, two_pair) == True
    assert c._first_bigger(four_a_kind, pair) == True
    assert c._first_bigger(four_a_kind, high_card) == True

    assert c._first_bigger(full_house, five_a_kind) == False
    assert c._first_bigger(full_house, four_a_kind) == False
    assert c._first_bigger(full_house, full_house) == True
    assert c._first_bigger(full_house, three_a_kind) == True
    assert c._first_bigger(full_house, two_pair) == True
    assert c._first_bigger(full_house, pair) == True
    assert c._first_bigger(full_house, high_card) == True

    assert c._first_bigger(three_a_kind, five_a_kind) == False
    assert c._first_bigger(three_a_kind, four_a_kind) == False
    assert c._first_bigger(three_a_kind, full_house) == False
    assert c._first_bigger(three_a_kind, three_a_kind) == True
    assert c._first_bigger(three_a_kind, two_pair) == True
    assert c._first_bigger(three_a_kind, pair) == True
    assert c._first_bigger(three_a_kind, high_card) == True
    
    assert c._first_bigger(two_pair, five_a_kind) == False
    assert c._first_bigger(two_pair, four_a_kind) == False
    assert c._first_bigger(two_pair, full_house) == False
    assert c._first_bigger(two_pair, three_a_kind) == False
    assert c._first_bigger(two_pair, two_pair) == True
    assert c._first_bigger(two_pair, pair) == True
    assert c._first_bigger(two_pair, high_card) == True

    assert c._first_bigger('TT997', 'TT998') == False
    assert c._first_bigger('23456', '65432') == False
    assert c._first_bigger('65432', '23456') == True
