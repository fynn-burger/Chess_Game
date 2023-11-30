# class Rook
# contains move-logic for Rook

from ..piece import Piece

class Rook(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)


    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):
        '''
        1.  Der Turm kann sich vertikal und horizontal soweit er will bewegen
        '''
        if (self.is_valid_movement(start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check) == False or \
            self.is_obstacle(board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check)):
            return False

        return True



    def is_valid_movement(self, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        if not (self.is_vertical(start_row_index, start_colum_index, end_row_index, end_colum_index) or \
                self.is_horizontal(start_row_index, start_colum_index, end_row_index, end_colum_index)): # --> If the rook goes not either just vertical or just horizontal return False
            if not is_check:
                print ("Rook can only move vertically or horizontally")
            return False

        return True

    def is_vertical(self, start_row_index, start_colum_index, end_row_index, end_colum_index):
        if abs(start_row_index - end_row_index) == 0 and abs(start_colum_index - end_colum_index) > 0:
            return True

        return False

    def is_horizontal(self, start_row_index, start_colum_index, end_row_index, end_colum_index):
        if abs(start_row_index - end_row_index) > 0 and abs(start_colum_index - end_colum_index) == 0:
            return True

        return False

    def is_obstacle(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        if self.is_obstacle_vertically(board, start_row_index, start_colum_index, end_row_index, end_colum_index) or \
                self.is_obstacle_horizontally(board, start_row_index, start_colum_index, end_row_index, end_colum_index):
            if not is_check:
                print ("There is an obstacle")
            return True

        return False


    def is_obstacle_vertically(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index):
        # Vertical movement to the right
        if self.is_vertical(start_row_index, start_colum_index, end_row_index, end_colum_index) and start_colum_index < end_colum_index:
            for i in range(abs(start_colum_index - end_colum_index) -1):
                if board[start_row_index][start_colum_index + i + 1].type != None:
                    return True

        # Vertical movement to the left
        elif self.is_vertical(start_row_index, start_colum_index, end_row_index, end_colum_index) and start_colum_index > end_colum_index:
            for i in range(abs(start_colum_index - end_colum_index) -1):
                if board[start_row_index][start_colum_index - i - 1].type != None:
                    return True

        return False

    def is_obstacle_horizontally(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index):
        # horizontal movement downwards
        if self.is_horizontal(start_row_index, start_colum_index, end_row_index, end_colum_index) and start_row_index < end_row_index:
            for i in range(abs(start_row_index - end_row_index) -1):
                if board[start_row_index + i + 1][start_colum_index].type != None:
                    return True

        # horizontal movement upwards
        elif self.is_horizontal(start_row_index, start_colum_index, end_row_index, end_colum_index) and start_row_index > end_row_index:
            for i in range(abs(start_row_index - end_row_index) -1):
                if board[start_row_index - i - 1][start_colum_index].type != None:
                    return True

        return False

