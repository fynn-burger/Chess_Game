#class Knight
# contains move-logic for Knight

from ..piece import Piece

class Knight(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)


    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):
        if not ((abs(start_row_index - end_row_index) == 2 and abs(start_colum_index - end_colum_index) == 1) or \
            (abs(start_row_index - end_row_index) == 1 and abs(start_colum_index - end_colum_index) == 2)):
            if not is_check:
                print("The knight goes an L-Shape")
            return False

        return True