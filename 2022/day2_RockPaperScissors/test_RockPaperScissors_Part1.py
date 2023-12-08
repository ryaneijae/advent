import pytest
import RockPaperScissors_Part1

def test_RPS_points():
    assert RockPaperScissors_Part1.RPS_points("Rock", "Paper") == 8
    assert RockPaperScissors_Part1.RPS_points("Paper", "Rock") == 1
    assert RockPaperScissors_Part1.RPS_points("Scissors", "Scissors") == 6

def test_error_RPS_points():
    with pytest.raises(ValueError):
        RockPaperScissors_Part1.RPS_points("Rock", "Rok")

def test_interpretation():
    assert RockPaperScissors_Part1.interpretation("A") == "Rock"
    assert RockPaperScissors_Part1.interpretation("B") == "Paper"
    assert RockPaperScissors_Part1.interpretation("C") == "Scissors"
    assert RockPaperScissors_Part1.interpretation("X") == "Rock"
    assert RockPaperScissors_Part1.interpretation("Y") == "Paper"
    assert RockPaperScissors_Part1.interpretation("Z") == "Scissors"

def test_error_nterpretation():
    with pytest.raises(ValueError):
        RockPaperScissors_Part1.interpretation("R")
