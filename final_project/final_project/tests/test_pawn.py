import pytest
from ..pieces.pawn import Pawn
from .test_chess_boards import pawn_test_board



def test_is_valid_movement():
    p = Pawn (None,None)
    # valid moves of white
    assert p.is_valid_movement(pawn_test_board,1,1,2,0,"White") == True
    assert p.is_valid_movement(pawn_test_board,1,1,2,2,"White") == True
    assert p.is_valid_movement(pawn_test_board,1,4,3,4,"White") == True
    assert p.is_valid_movement(pawn_test_board,1,4,2,4,"White") == True

    # valid moves of black
    assert p.is_valid_movement(pawn_test_board,1,2,0,1,"Black") == True
    assert p.is_valid_movement(pawn_test_board,1,2,0,2,"Black") == True
    assert p.is_valid_movement(pawn_test_board,1,2,0,3,"Black") == True
    assert p.is_valid_movement(pawn_test_board,6,4,5,4,"Black") == True
    assert p.is_valid_movement(pawn_test_board,6,4,4,4,"Black") == True

    # invalid moves of white
    assert p.is_valid_movement(pawn_test_board,1,1,1,0,"White") == False
    assert p.is_valid_movement(pawn_test_board,1,1,1,2,"White") == False
    assert p.is_valid_movement(pawn_test_board,1,1,3,2,"White") == False
    assert p.is_valid_movement(pawn_test_board,1,4,0,4,"White") == False
    assert p.is_valid_movement(pawn_test_board,6,0,5,0,"White") == False
    assert p.is_valid_movement(pawn_test_board,6,0,4,0,"White") == False
    # invalid moves of Black
    assert p.is_valid_movement(pawn_test_board,6,1,5,0,"Black") == False
    assert p.is_valid_movement(pawn_test_board,6,1,5,2,"Black") == False
    assert p.is_valid_movement(pawn_test_board,6,1,7,1,"Black") == False
    assert p.is_valid_movement(pawn_test_board,3,5,1,5,"Black") == False
    assert p.is_valid_movement(pawn_test_board,6,1,6,0,"Black") == False
    assert p.is_valid_movement(pawn_test_board,6,1,6,2,"Black") == False

def test_is_obstacle():
    p = Pawn(None,None)
    # White moves
    assert p.is_obstacle(pawn_test_board,1,1,2,"White") == False
    assert p.is_obstacle(pawn_test_board,1,4,3,"White") == False
    assert p.is_obstacle(pawn_test_board,1,4,2,"White") == False
    assert p.is_obstacle(pawn_test_board,0,3,1,"White") == False
    assert p.is_obstacle(pawn_test_board,1,1,3,"White") == True
    # Black moves
    assert p.is_obstacle(pawn_test_board,6,4,5,"Black") == False
    assert p.is_obstacle(pawn_test_board,6,4,4,"Black") == False
    assert p.is_obstacle(pawn_test_board,6,1,4,"Black") == True

def test_is_valid ():
    p = Pawn (None,None)
    # Valid move
    assert p.is_valid(pawn_test_board,1,1,2,0,"White") == True
    #invalid cause of obstacle
    assert p.is_valid(pawn_test_board,1,1,3,1,"White") == False


