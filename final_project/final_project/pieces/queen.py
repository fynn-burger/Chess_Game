# class Queen
# contains move-logic for Queen

from ..piece import Piece
from .bishop import Bishop
from .rook import Rook

class Queen(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)
        self.virtual_bishop = Bishop(None, None)
        self.virtual_rook = Rook(None, None)

    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):

        if (self.is_valid_movement(start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check) == False or \
            self.is_obstacle(board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check)):
            return False

        return True

    def is_valid_movement(self, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        if not (abs(start_row_index - end_row_index) == abs(start_colum_index - end_colum_index) or \
                 self.virtual_rook.is_vertical (start_row_index, start_colum_index, end_row_index, end_colum_index) or  \
                    self.virtual_rook.is_horizontal (start_row_index, start_colum_index, end_row_index, end_colum_index)):
            if not is_check:
                print ("Queen can only go diagonally, horizontally or vertically")
            return False

        return True

    def is_obstacle(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        if self.virtual_bishop.is_obstacle(board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check) or \
                self.virtual_rook.is_obstacle(board, start_row_index, start_colum_index, end_row_index,end_colum_index, is_check=is_check):
            if not is_check:
                print ("There is an obstacle")
            return True

        return False