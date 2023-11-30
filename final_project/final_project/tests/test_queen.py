import pytest
from ..pieces.queen import Queen
from .test_chess_boards import queen_test_board


def test_is_valid_movement():
    q = Queen(None,None)
    # diagonal
    assert q.is_valid_movement(3,3,5,5) == True
    assert q.is_valid_movement(3,3,5,1) == True
    assert q.is_valid_movement(3,3,1,1) == True
    assert q.is_valid_movement(3,3,1,5) == True
        # vertical
    assert q.is_valid_movement(3,3,3,5) == True
    assert q.is_valid_movement(3,3,3,1) == True
    # horizontal
    assert q.is_valid_movement(3,3,5,3) == True
    assert q.is_valid_movement(3,3,1,3) == True
    # invalid
    assert q.is_valid_movement(3,3,4,5) == False
    assert q.is_valid_movement(3,3,5,4) == False
    assert q.is_valid_movement(3,3,6,1) == False
    assert q.is_valid_movement(3,3,7,1) == False

def test_is_obstacle():
    q = Queen(None,None)
    # all obstacles on map
    assert q.is_obstacle(queen_test_board, 3,3,0,3) == True
    assert q.is_obstacle(queen_test_board, 3,3,0,0) == True
    assert q.is_obstacle(queen_test_board, 3,3,3,0) == True
    assert q.is_obstacle(queen_test_board, 3,3,6,0) == True
    assert q.is_obstacle(queen_test_board, 3,3,7,3) == True
    assert q.is_obstacle(queen_test_board, 3,3,7,7) == True
    assert q.is_obstacle(queen_test_board, 3,3,3,7) == True
    assert q.is_obstacle(queen_test_board, 3,3,0,6) == True
    # valid moves
    assert q.is_obstacle(queen_test_board, 3,3,1,3) == False
    assert q.is_obstacle(queen_test_board, 3,3,1,1) == False
    assert q.is_obstacle(queen_test_board, 3,3,5,0) == False
    assert q.is_obstacle(queen_test_board, 3,3,6,3) == False
    assert q.is_obstacle(queen_test_board, 3,3,5,5) == False
    assert q.is_obstacle(queen_test_board, 3,3,3,5) == False
    assert q.is_obstacle(queen_test_board, 3,3,1,5) == False

def test_is_valid():
    q = Queen(None,None)
    # all obstacles on map
    assert q.is_valid(queen_test_board, 3,3,0,3, " ") == False
    assert q.is_valid(queen_test_board, 3,3,0,0, " ") == False
    assert q.is_valid(queen_test_board, 3,3,3,0, " ") == False
    assert q.is_valid(queen_test_board, 3,3,6,0, " ") == False
    assert q.is_valid(queen_test_board, 3,3,7,3, " ") == False
    assert q.is_valid(queen_test_board, 3,3,7,7, " ") == False
    assert q.is_valid(queen_test_board, 3,3,3,7, " ") == False
    assert q.is_valid(queen_test_board, 3,3,0,6, " ") == False
    # valid moves
    assert q.is_valid(queen_test_board, 3,3,1,3, " ") == True
    assert q.is_valid(queen_test_board, 3,3,1,1, " ") == True
    assert q.is_valid(queen_test_board, 3,3,5,1, " ") == True
    assert q.is_valid(queen_test_board, 3,3,6,3, " ") == True
    assert q.is_valid(queen_test_board, 3,3,5,5, " ") == True
    assert q.is_valid(queen_test_board, 3,3,3,5, " ") == True
    assert q.is_valid(queen_test_board, 3,3,1,5, " ") == True
    # invalid moves because of piece movement logic
    assert q.is_valid(queen_test_board,3,3,4,5, " ") == False
    assert q.is_valid(queen_test_board,3,3,5,4, " ") == False
    assert q.is_valid(queen_test_board,3,3,6,1, " ") == False
    assert q.is_valid(queen_test_board,3,3,7,1, " ") == False
