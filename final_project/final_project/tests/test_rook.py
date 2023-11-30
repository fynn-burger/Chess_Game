import pytest
from ..pieces.rook import Rook
from .test_chess_boards import rook_test_board


def test_is_vertical():
    r = Rook(None,None)
    assert r.is_vertical (0,1,0,4) == True
    assert r.is_vertical (0,4,0,1) == True
    assert r.is_vertical (1,1,4,1) == False
    assert r.is_vertical (1,1,4,4) == False
    assert r.is_vertical (1,1,1,1) == False


def test_is_horizontal():
    r = Rook(None,None)
    assert r.is_horizontal (1,1,1,1) == False
    assert r.is_horizontal (0,1,0,4) == False
    assert r.is_horizontal (0,4,0,1) == False
    assert r.is_horizontal (1,1,4,1) == True
    assert r.is_horizontal (4,1,1,1) == True
    assert r.is_horizontal (1,1,4,4) == False

def test_is_valid_movement():
    r = Rook(None,None)
    assert r.is_valid_movement (1,1,1,1) == False
    assert r.is_valid_movement (1,1,2,2) == False
    assert r.is_valid_movement (1,1,0,0) == False
    assert r.is_valid_movement (1,1,2,3) == False
    assert r.is_valid_movement (0,1,0,4) == True
    assert r.is_valid_movement (0,4,0,1) == True
    assert r.is_valid_movement (1,1,4,1) == True
    assert r.is_valid_movement (4,1,1,1) == True

def test_is_obstacle_vertically():
    r = Rook(None,None)
    assert r.is_obstacle_vertically(rook_test_board, 3,3,3,7) == True
    assert r.is_obstacle_vertically(rook_test_board, 3,3,3,0) == True
    assert r.is_obstacle_vertically(rook_test_board, 3,3,3,5) == False
    assert r.is_obstacle_vertically(rook_test_board, 3,3,3,1) == False


def test_is_obstacle_horizontally():
    r = Rook(None,None)
    assert r.is_obstacle_horizontally(rook_test_board, 3,3,0,3) == True
    assert r.is_obstacle_horizontally(rook_test_board, 3,3,7,3) == True
    assert r.is_obstacle_horizontally(rook_test_board, 3,3,2,3) == False
    assert r.is_obstacle_horizontally(rook_test_board, 3,3,5,3) == False


def test_is_obstacle():
    r = Rook(None,None)
    assert r.is_obstacle(rook_test_board, 3,3,0,3) == True
    assert r.is_obstacle(rook_test_board, 3,3,7,3) == True
    assert r.is_obstacle(rook_test_board, 3,3,2,3) == False
    assert r.is_obstacle(rook_test_board, 3,3,5,3) == False
    assert r.is_obstacle(rook_test_board, 3,3,3,7) == True
    assert r.is_obstacle(rook_test_board, 3,3,3,0) == True
    assert r.is_obstacle(rook_test_board, 3,3,3,5) == False
    assert r.is_obstacle(rook_test_board, 3,3,3,1) == False

def test_is_valid():
    r = Rook (None,None)
    assert r.is_valid (rook_test_board,1,1,1,1, " ") == False
    assert r.is_valid (rook_test_board,1,1,2,2, " ") == False
    assert r.is_valid (rook_test_board,1,1,0,0, " ") == False
    assert r.is_valid (rook_test_board,1,1,2,3, " ") == False
    assert r.is_valid (rook_test_board,0,1,0,4, " ") == True
    assert r.is_valid (rook_test_board,0,4,0,1, " ") == True
    assert r.is_valid (rook_test_board,1,1,4,1, " ") == False
    assert r.is_valid (rook_test_board,4,1,1,1, " ") == False
    assert r.is_valid(rook_test_board, 3,3,0,3, " ") == False
    assert r.is_valid(rook_test_board, 3,3,7,3, " ") == False
    assert r.is_valid(rook_test_board, 3,3,2,3, " ") == True
    assert r.is_valid(rook_test_board, 3,3,5,3, " ") == True
    assert r.is_valid(rook_test_board, 3,3,3,7, " ") == False
    assert r.is_valid(rook_test_board, 3,3,3,0, " ") == False
    assert r.is_valid(rook_test_board, 3,3,3,5, " ") == True
    assert r.is_valid(rook_test_board, 3,3,3,1, " ") == True
