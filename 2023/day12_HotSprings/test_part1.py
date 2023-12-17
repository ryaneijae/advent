import pytest
from part1 import HotSpring

sample_path = 'input/sample.txt'

def test_hot_springs_simplify():
    h = HotSpring(sample_path)

    assert h.simplify('..##.') == '##'
    assert h.simplify('#?##?###?####') == '#?##?###?####'
    assert h.simplify('.#.....##.') =='#.##'

def test_get_answer():
    h = HotSpring(sample_path)
    assert h.get_answer(['1', '2', '3']) == '#.##.###'
