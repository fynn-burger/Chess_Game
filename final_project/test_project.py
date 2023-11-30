import pytest
from unittest.mock import patch
from project import is_surrender, is_draw, checkmate_endgame

def test_is_draw():
    with patch('builtins.input', return_value='Y'):
        with pytest.raises(SystemExit):
            is_draw("White")
    with patch('builtins.input', return_value='N'):
        assert is_draw("White") == False

def test_is_surrender():
    with pytest.raises(SystemExit):
        is_surrender("White")
    with pytest.raises(SystemExit):
        is_surrender("Black")
def test_checkmate_endgame():
    with pytest.raises(SystemExit):
        checkmate_endgame("White")
    with pytest.raises(SystemExit):
        checkmate_endgame("Black")
