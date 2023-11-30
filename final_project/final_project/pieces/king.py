# class King
# contains move-logic for King

from ..piece import Piece

class King(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)

    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player,
                 K_moved, k_moved, _00R_moved, _07R_moved, _70r_moved, _77r_moved, is_check=False):
        '''
        1.  Der könig kann sich diagonal und vertikal/horizontal um einen Schritt bewegen
            Diagonal : beide differenzen sind 1
            straight: eine differenz ist eins und eine null
        2.  Er darf nicht ins Schach gehen --> Also nicht wohin wo er bedroht wird --> Das wird auch automatisch durch die is_check_methode festgestellt
        3.  Er muss immer ein Feld abstand vom gegnerischen könig haben --> Das wird ja automatisch durch die is_check_Funktion sichergestellt
        4.  Der König kann eine Rochade machen --> Das wird im moment auch gehen, wenn der König oder der Turm sich in der Zwischenzeit schon bewegt haben
            Rochade erstmal komplett weg
        '''

        if (self.is_regular_movement(start_row_index, start_colum_index, end_row_index, end_colum_index) == False and \
            self.is_rochade(board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, K_moved, k_moved, _00R_moved, _07R_moved, _70r_moved, _77r_moved) == False):
            if not is_check:
                print("Invalid King move")
            return False

        return True

    def is_regular_movement(self, start_row_index, start_colum_index, end_row_index, end_colum_index):
        is_straight = abs(start_row_index - end_row_index) + abs(start_colum_index - end_colum_index) == 1
        is_diagonal = (abs(start_row_index - end_row_index) == 1 and abs(start_colum_index - end_colum_index) == 1)

        if not (is_straight or is_diagonal):
            return False

        return True

    def is_rochade(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, K_moved, k_moved, _00R_moved, _07R_moved, _70r_moved, _77r_moved):

        from ..board import Board
        b = Board()
        if current_player == "White":
            attacking_player = "Black"
        else:
            attacking_player = "White"

        if current_player == "White" and start_row_index == 0 and start_colum_index == 4:
            if not K_moved:
                if end_row_index == 0:
                    if end_colum_index == 2 and not _00R_moved:
                        for col in range (4, 1, -1):
                            if b.is_blockable_fields(board, 0, col, attacking_player):
                                return False

                        return True

                    elif end_colum_index == 6 and not _07R_moved:
                        for col in range (4, 7):
                            if b.is_blockable_fields(board, 0, col, attacking_player):
                                return False

                        return True


        elif current_player == "Black" and start_row_index == 7 and start_colum_index == 4:
            if not k_moved:
                if end_row_index == 7:
                    if end_colum_index == 2 and not _70r_moved:
                        for col in range (4, 1, -1):
                            if b.is_blockable_fields(board, 7, col, attacking_player):
                                return False

                        return True

                    elif end_colum_index == 6 and not _77r_moved:
                        for col in range (4, 7):
                            if b.is_blockable_fields(board, 7, col, attacking_player):
                                return False
                        return True

        return False

