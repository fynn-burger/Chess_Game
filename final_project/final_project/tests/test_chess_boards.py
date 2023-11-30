from ..piece import Piece

normal_test_board = [
    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece("K", "White"), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black")],
    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
    ]

b_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("B", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

king_test_board = [
    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece(None,None), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black")],
    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
    ]

knight_test_board = [
    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece("K", "White"), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("N", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black")],
    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
    ]

pawn_test_board = [
    [Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("P", "White"), Piece("p", "Black"), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("n", "Black"), Piece("Q", "White"), Piece("n", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("p", "Black"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("Q", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("P", "White"), Piece("p", "Black"), Piece(None, None), Piece(None, None), Piece("Pawn", "Black"), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

queen_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("Q", "White"), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

rook_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("P", "White"), Piece(None, None), Piece("R", "White"), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

# check if in check = cc
cc1_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("b", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("b", "Black"), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

cc2_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

cc3_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

cc4_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

# check if in checkmate:
# not checkmate
ccm1_test_board = [
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

# is checkmate
ccm2_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]
# Player can hit checking figure vertically
ccm3_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece("R", "White"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]
# player can hit checking figure diagonally
ccm3_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("B", "White"), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

# blocking is possible
ccm4_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("R", "White"), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]
ccm5_test_board = [
    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece("K", "White"), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("B", "W"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("Q", "White"), Piece("p", "Black"), Piece("p", "Black")],
    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
    ]
# check block = cb
# no block
cb1_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]
# horizontal block
cb2_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("R", "White"), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

# diagonal block
cb3_test_board = [
    [Piece(None, None), Piece("K", "White"), Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece("r", "Black"), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece("B", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None,None), Piece(None,None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]


rochade_test_board = [
    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece("K", "White"), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black")],
    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
    ]

# check for patt
cp1_test_board = [
    [Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]

cp2_test_board = [
    [Piece("K", "White"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece("q", "Black"), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece("P", "White"), Piece(None, None), Piece(None, None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None,None), Piece(None, None)],
    [Piece(None, None), Piece(None, None), Piece("k", "Black"),Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)]
    ]


