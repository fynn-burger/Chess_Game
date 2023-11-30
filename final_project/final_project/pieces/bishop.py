# Class for bishop
# contains move-logic for bishop
from ..piece import Piece

class Bishop(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)



    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):
        if (self.is_valid_movement(start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check) == False or \
            self.is_obstacle(board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=is_check)):
            return False

        return True

    def is_valid_movement(self, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        # checks if bishop tries to go diagonal
        if abs(start_row_index - end_row_index) != abs(start_colum_index - end_colum_index):
            if not is_check:
                print ("The bishop can only move diagonally")
            return False

        return True

    def is_obstacle(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, is_check=False):
        #checks if there are obstacles --> top (1) to bottom (8)
        #checks for going down and right
        if start_row_index < end_row_index and start_colum_index < end_colum_index:
            for i in range (abs(start_row_index - end_row_index) - 1):
                if board[start_row_index + i + 1][start_colum_index + i + 1].type != None:
                    if not is_check:
                        print ("You cannot jump other pieces")
                    return True

        #checks for going down and left
        elif start_row_index < end_row_index and start_colum_index > end_colum_index:
            for i in range (abs(start_row_index - end_row_index) - 1):
                if board[start_row_index + i + 1][start_colum_index - i - 1].type != None:
                    if not is_check:
                        print ("You cannot jump other pieces")
                    return True

        #checks for going up and right
        elif start_row_index > end_row_index and start_colum_index < end_colum_index:
            for i in range (abs(start_row_index - end_row_index) - 1):
                if board[start_row_index - i - 1][start_colum_index + i + 1].type != None:
                    if not is_check:
                        print ("You cannot jump other pieces")
                    return True

        #checks for going up and left
        elif start_row_index > end_row_index and start_colum_index > end_colum_index:
            for i in range (abs(start_row_index - end_row_index) - 1):
                if board[start_row_index - i - 1][start_colum_index - i - 1].type != None:
                    if not is_check:
                        print ("You cannot jump other pieces")
                    return True

        return False

