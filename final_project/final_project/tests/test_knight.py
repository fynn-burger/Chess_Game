import pytest
from ..pieces.knight import Knight


board = []
def test_is_valid():
    k = Knight(None,None)
    # all valid moves
    assert k.is_valid(board, 3,3,5,4, " ") == True
    assert k.is_valid(board, 3,3,5,2, " ") == True
    assert k.is_valid(board, 3,3,1,4, " ") == True
    assert k.is_valid(board, 3,3,5,2, " ") == True
    assert k.is_valid(board, 3,3,4,5, " ") == True
    assert k.is_valid(board, 3,3,2,5, " ") == True
    assert k.is_valid(board, 3,3,4,1, " ") == True
    assert k.is_valid(board, 3,3,2,1, " ") == True
    # some invalid moves
    assert k.is_valid(board, 3,3,6,3, " ") == False
    assert k.is_valid(board, 3,3,3,6, " ") == False
    assert k.is_valid(board, 3,3,0,3, " ") == False
    assert k.is_valid(board, 3,3,3,0, " ") == False
    assert k.is_valid(board, 3,3,4,4, " ") == False
    assert k.is_valid(board, 3,3,2,2, " ") == False
    assert k.is_valid(board, 3,3,4,2, " ") == False
    assert k.is_valid(board, 3,3,2,4, " ") == False
    assert k.is_valid(board, 3,3,3,2, " ") == False
    assert k.is_valid(board, 3,3,2,3, " ") == False

