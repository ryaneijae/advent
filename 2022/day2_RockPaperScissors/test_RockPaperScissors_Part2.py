import pytest
import RockPaperScissors_Part2

def test_RPS_points():
    assert RockPaperScissors_Part2.RPS_points("Rock", "Paper") == 8
    assert RockPaperScissors_Part2.RPS_points("Paper", "Rock") == 1
    assert RockPaperScissors_Part2.RPS_points("Scissors", "Scissors") == 6

def test_error_RPS_points():
    with pytest.raises(ValueError):
        RockPaperScissors_Part2.RPS_points("Rock", "Rok")

def test_interpretation():
    assert RockPaperScissors_Part2.interpretation("A") == "Rock"
    assert RockPaperScissors_Part2.interpretation("B") == "Paper"
    assert RockPaperScissors_Part2.interpretation("C") == "Scissors"
    assert RockPaperScissors_Part2.interpretation("X") == "Rock"
    assert RockPaperScissors_Part2.interpretation("Y") == "Paper"
    assert RockPaperScissors_Part2.interpretation("Z") == "Scissors"

def test_error_interpretation():
    with pytest.raises(ValueError):
        RockPaperScissors_Part2.interpretation("R")

def test_mychoice():
    assert RockPaperScissors_Part2.mychoice("A", "Y") == "Rock"
    assert RockPaperScissors_Part2.mychoice("B", "X") == "Rock"
    assert RockPaperScissors_Part2.mychoice("C", "Z") == "Rock"



