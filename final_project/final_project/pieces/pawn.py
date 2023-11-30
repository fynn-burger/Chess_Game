# class Pawn
# contains move-logic for Pawn
# contains logic for changing figure --> Not yet!

from ..piece import Piece

class Pawn(Piece):
    def __init__(self, symbol, color):
        super().__init__(symbol, color)

    def is_valid(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):
        '''
            1.  Der bauer kann 1 oder 2 Schritte nach vorne gehen, wenn auf dem Zielfeld keine andere Figur steht --> "vorne hängt von schwarz und
                weiß ab"
            2.  Der Bauer kann diagonal schlagen, wenn dort eine gegnerische Figur steht.
            3.  en passant (lasse ich erstmal weg): Wenn der gegnerische Bauer im vorherigen Zug 2 nach vorne gezogen ist nun nun neben dem eigenen
                steht, kann der eigen schräg vorbei schlagen, als wäre der bauer davor nur einen Schritt nach vorne gegangen.
            4.  Wenn der Bauer auf der gegnerischen Grundlinie steht kann er sich in eine andere Figur verwandeln --> Auch noch nicht
        '''
        if (self.is_valid_movement(board,start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=is_check) == False or \
            self.is_obstacle(board, start_row_index, start_colum_index, end_row_index, current_player, is_check=is_check)):
            return False

        return True
        # Check move directions
        # Does the Pawn move in the right direction?

    def is_valid_movement(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):
        if (current_player == "White" and not start_row_index < end_row_index) or (current_player == "Black" and not start_row_index > end_row_index):
            if not is_check:
                print("Pawn can not go in that direction!")
            return False
        # Pawn can never go further than 2
        elif abs (start_row_index - end_row_index) > 2:
            if not is_check:
                print ("Pawn can not go that far")
            return False
        # Pawn can not got more than 1 if not on baseline
        elif ((current_player == "White" and abs(start_row_index - end_row_index) > 1 and start_row_index != 1) or (current_player == "Black" and abs(start_row_index - end_row_index) > 1 and start_row_index != 6)):
            if not is_check:
                print ("Pawn can not go that far!")
            return False
        # Pawn can not go vertically more than one step and not at all if going 2 steps
        elif abs (start_colum_index - end_colum_index) > 1 or (abs(start_row_index - end_row_index) == 2 and abs (start_colum_index - end_colum_index) != 0):
            if not is_check:
                print ("Pawn can not go that far vertically")
            return False
        # Pawn has to go at least one step horizontally
        elif abs (start_row_index - end_row_index) == 0:
            if not is_check:
                print ("Pawn has to go horizontally")
            return False
        # Pawn can only go vertically, if he hit another figure
        elif abs (start_row_index - end_row_index) == 1 and abs (start_colum_index - end_colum_index) == 1 and board[end_row_index][end_colum_index].type == None:
            if not is_check:
                print("Pawn can only go diagoanlly to hit another piece")
            return False

        return True

    def is_obstacle(self, board, start_row_index, start_colum_index, end_row_index, current_player, is_check=False):

        #check obstacles
        if current_player == "White" and abs (start_row_index - end_row_index) == 2:
            if board[start_row_index + 1][start_colum_index].type != None:
                if not is_check:
                    print ("There is an obstacle")
                return True

        elif current_player == "Black" and abs (start_row_index - end_row_index) == 2:
            if board[start_row_index - 1][start_colum_index].type != None:
                if not is_check:
                    print ("There is an obstacle")
                return True

        return False
