from ..board import Board
import final_project.tests.test_chess_boards as t

# ich mache keine tests mehr für die rochade

def test_is_valid_format():
    b = Board()
    # valid format
    start_position, end_position = b.is_valid_format("a1 c5")
    assert start_position == "a1"
    assert end_position == "c5"
    start_position, end_position = b.is_valid_format("b3 f7")
    assert start_position == "b3"
    assert end_position == "f7"
    # invalid format
    assert b.is_valid_format("b3b7") == False
    assert b.is_valid_format("A3 b7") == False
    assert b.is_valid_format("A3 B7") == False
    assert b.is_valid_format("k3 b7") == False
    assert b.is_valid_format("a9 a5") == False

def test_get_indeces():
    b = Board()
    start_row_index, start_colum_index, end_row_index, end_colum_index = b.get_indeces("a1", "c5")
    assert start_row_index == 0
    assert start_colum_index == 0
    assert end_row_index == 4
    assert end_colum_index == 2
    start_row_index, start_colum_index, end_row_index, end_colum_index = b.get_indeces("c8", "b4")
    assert start_row_index == 7
    assert start_colum_index == 2
    assert end_row_index == 3
    assert end_colum_index == 1

def test_is_valid_logic(capsys):
    b = Board()
    # White tries to move empty Field
    return1 = b.is_valid_logic(t.normal_test_board, 4,4,2,1, "White")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "No Piece on this Field!\n"
    # Black tries to move empty Field
    return1 = b.is_valid_logic(t.normal_test_board, 4,4,2,1, "Black")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "No Piece on this Field!\n"
    # White tries to move black piece
    return1 = b.is_valid_logic(t.normal_test_board, 7,7,2,1, "White")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "You have to move your own Piece!\n"
    # black tries to move white piece
    return1 = b.is_valid_logic(t.normal_test_board, 1,1,2,1, "Black")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "You have to move your own Piece!\n"
    # White tries to hit its own piece
    return1 = b.is_valid_logic(t.normal_test_board, 0,1,1,3, "White")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "You cannot hit your own Piece\n"
    # Black tries to hit its own piece
    return1 = b.is_valid_logic(t.normal_test_board, 7,3,6,3, "Black")
    captured = capsys.readouterr()
    assert return1 == False
    assert captured.out == "You cannot hit your own Piece\n"

    # I only need one test per permutation here because we know from the other tests, that the piece logic is correct
    # Wrong Bishop move
    assert b.is_valid_logic(t.b_test_board,3,3,7,0,"White") == False
    # Right Bishop move
    assert b.is_valid_logic(t.b_test_board,3,3,4,4,"White") == True
    # Wrong King move
    assert b.is_valid_logic(t.b_test_board,3,3,7,0,"White") == False
    # Right King move
    assert b.is_valid_logic(t.king_test_board,3,3,3,4,"White") == True
    # wrong Knight move
    assert b.is_valid_logic(t.knight_test_board,3,3,7,0,"White") == False
    # Right Knight move
    assert b.is_valid_logic(t.knight_test_board,3,3,5,4,"White") == True
    # Wrong Pawn move
    assert b.is_valid_logic(t.normal_test_board,0,1,0,4,"White") == False
    # right Pawn move
    assert b.is_valid_logic(t.normal_test_board,1,0,2,0,"White") == True
    # Wrong Queen move
    assert b.is_valid_logic(t.queen_test_board,3,3,5,4,"White") == False
    # right Queen move
    assert b.is_valid_logic(t.queen_test_board,3,3,4,4,"White") == True
    # Wrong Rook move
    assert b.is_valid_logic(t.rook_test_board,3,3,3,0,"White") == False
    # Right Rook move
    assert b.is_valid_logic(t.rook_test_board,3,3,3,4,"White") == True

def test_move_piece():
    b = Board()
    board = b.move_piece(t.cc2_test_board, 3,3,4,3)
    assert board[3][3].type == None
    assert board[4][3].type == "K"


def test_find_king():
    b = Board()
    row, object = b.find_king(t.normal_test_board, "White")
    assert row == 0
    assert object == 4
    row, object = b.find_king(t.normal_test_board, "Black")
    assert row == 7
    assert object == 4
    row, object = b.find_king(t.king_test_board, "White")
    assert row == 3
    assert object == 3


def test_is_check():
    b = Board()
    # check if current_position is in check
    assert b.is_check(t.cc2_test_board, None,None,None,None, "White", check_current_position = True) == True
    assert b.is_check(t.cc2_test_board, None,None,None,None, "Black", check_current_position = True) == False
    # check if future position is in check
    # Diese tests machen so keinen sinn, es muss natürlich eine eigene Figur gezogen werden
    assert b.is_check(t.cc3_test_board, 3,3,2,3, "White") == True
    assert b.is_check(t.cc3_test_board, 3,3,4,3, "White") == True
    assert b.is_check(t.cc3_test_board, 3,3,3,4, "White") == False
    # check if output of checking positions is working
    return_dict = b.is_check(t.cc4_test_board, None,None,None,None, "White", check_current_position = True, search_checking_pieces=True)
    assert return_dict == {"0,3":"q"}
    return_dict = b.is_check(t.cc1_test_board, None,None,None,None, "White", check_current_position = True, search_checking_pieces=True)
    assert return_dict == {'0,3': 'q', '1,5': 'b', '5,1': 'b', '6,6': 'b'}


def test_is_blockable_fields():
    b = Board()
    assert b.is_blockable_fields(t.cb1_test_board, 0,2,"White") == False
    assert b.is_blockable_fields(t.cb2_test_board, 0,2,"White") == True
    assert b.is_blockable_fields(t.cb3_test_board, 0,2,"White") == True


def test_is_checkmate():
    b = Board()
    assert b.is_checkmate(t.ccm1_test_board, "White") == False
    assert b.is_checkmate(t.ccm2_test_board, "White") == True
    assert b.is_checkmate(t.ccm3_test_board, "White") == False
    assert b.is_checkmate(t.ccm4_test_board, "White") == False
    assert b.is_checkmate(t.ccm5_test_board, "Black") == True
    assert b.is_checkmate(t.cp1_test_board, "White") == False

def test_is_patt():
    b = Board()
    assert b.is_patt(t.cp1_test_board, "White") == True
    assert b.is_patt(t.normal_test_board, "Black") == False
    assert b.is_patt(t.cp2_test_board, "White") == False



