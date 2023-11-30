import pytest
from ..pieces.bishop import Bishop
from .test_chess_boards import b_test_board



def test_is_valid_movement():
    b = Bishop(None, None)
    assert b.is_valid_movement(3,3,4,4) == True
    assert b.is_valid_movement(3,3,2,2) == True
    assert b.is_valid_movement(3,3,2,4) == True
    assert b.is_valid_movement(3,3,4,2) == True
    assert b.is_valid_movement(3,3,4,5) == False

def test_is_obstacle():
    b = Bishop(None, None)
    assert b.is_obstacle(b_test_board,3,3,6,0) == True
    assert b.is_obstacle(b_test_board,3,3,0,6) == True
    assert b.is_obstacle(b_test_board,3,3,7,7) == True
    assert b.is_obstacle(b_test_board,3,3,2,2) == False
    assert b.is_obstacle(b_test_board,3,3,1,1) == False

def test_is_valid():
    b = Bishop(None,None)
    assert b.is_valid(b_test_board,3,3,6,0,"") == False
    assert b.is_valid(b_test_board,3,3,7,7,"") == False
    assert b.is_valid(b_test_board,3,3,4,5,"") == False
    assert b.is_valid(b_test_board,3,3,4,4,"") == True
    assert b.is_valid(b_test_board,3,3,6,6,"") == True

