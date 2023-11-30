from ..pieces.king import King
from .test_chess_boards import king_test_board, rochade_test_board
from ..board import Board

def test_is_valid():
    k = King(None,None)
    assert k.is_valid(king_test_board,3,3,4,4," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,2,2," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,4,2," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,2,4," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,3,4," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,4,3," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,3,2," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,2,3," ", False, False, False, False, False, False) == True
    assert k.is_valid(king_test_board,3,3,4,5," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,5,5," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,1,1," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,2,5," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,3,5," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,5,3," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,3,1," ", False, False, False, False, False, False) == False
    assert k.is_valid(king_test_board,3,3,1,3," ", False, False, False, False, False, False) == False

def test_is_rochade():
    k = King(None,None)
    # are the movements checked
    assert k.is_rochade(rochade_test_board,0,4,0,6,"White",False,True,True,False,True, True) == True
    assert k.is_rochade(rochade_test_board,0,4,0,2,"White",False,True,False,True,False,False) == True
    assert k.is_rochade(rochade_test_board,0,4,0,6,"White",True,False,False,False,False,False) == False
    assert k.is_rochade(rochade_test_board,0,4,0,2,"White",True,False,False,False,False,False) == False
    assert k.is_rochade(rochade_test_board,7,4,7,6,"Black",False,True,True,False,True, True) == False
    assert k.is_rochade(rochade_test_board,7,4,7,2,"Black",False,True,False,True,False,False) == False
    assert k.is_rochade(rochade_test_board,7,4,7,6,"Black",True,False,False,False,True,False) == True
    assert k.is_rochade(rochade_test_board,7,4,7,2,"Black",True,False,False,False,False,True) == True
    assert k.is_rochade(rochade_test_board,7,4,0,6,"Black",False,True,True,False,True, True) == False
    assert k.is_rochade(rochade_test_board,0,4,7,6,"White",True,False,False,False,True,False) == False

