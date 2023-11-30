# Class for the chess board
import re
import sys
import csv
import os
from .piece import Piece
from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook


class Board:
    piece_classes = {
        "p" : Pawn,
        "b" : Bishop,
        "k" : King,
        "n" : Knight,
        "q" : Queen,
        "r" : Rook
    }
    def __init__(self):
        # generate labels
        self._labels = ["  ","A", "B", "C", "D", "E", "F", "G", "H"," "] # labels
        #generate new board
        self._board = self.generate_board()
        # moves until remis
        self._remis_counter = 0
        # have the kings moved yet
        self._K_moved = False
        self._k_moved = False
        # have the rooks moved yet
        self._00R_moved = False
        self._07R_moved = False
        self._70r_moved = False
        self._77r_moved = False

    def generate_board (self):
        board = [
                    [Piece("R", "White"), Piece("N", "White"), Piece("B", "White"), Piece("Q", "White"), Piece("K", "White"), Piece("B", "White"), Piece("N", "White"), Piece("R", "White")],
                    [Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White"), Piece("P", "White")],
                    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
                    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
                    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
                    [Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None), Piece(None, None)],
                    [Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black"), Piece("p", "Black")],
                    [Piece("r", "Black"), Piece("n", "Black"), Piece("b", "Black"), Piece("q", "Black"), Piece("k", "Black"), Piece("b", "Black"), Piece("n", "Black"), Piece("r", "Black")]
                ]
        return board

    def display(self):
        print()
        print(" | ".join(map(str,self._labels)))
        print("---+---+---+---+---+---+---+---+---+---")
        for i,row in enumerate(self._board):
            print (f" {i + 1} |", end= " ")
            print(" | ".join(map(str,row)), end = " ")
            print (f"| {i + 1}")
            if i < 9:
                print("---+---+---+---+---+---+---+---+---+---")
        print(" | ".join(map(str,self._labels)))


    def is_valid_move(self, board, input_move, current_player):
        # check if format is valid and positions are on the board
        if not self.is_valid_format(input_move):
            print ("Invalid move format or end-position not on board")
            return False
        # return positions
        start_position, end_position = self.is_valid_format(input_move)

        # get indeces of move and return them
        start_row_index, start_colum_index, end_row_index, end_colum_index = self.get_indeces(start_position, end_position)

        #check if move-logic is valid
        if not self.is_valid_logic(board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player):
            return False

        # check if player tries to move in check
        if self.is_check(board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player):
            print ("You cannot move into check")
            return False

        # return indeces
        return start_row_index, start_colum_index, end_row_index, end_colum_index


    # check correct format
    def is_valid_format(self, input_move):
        if not(matches := re.search(r"([a-h][1-8]) ([a-h][1-8])", input_move)):
            return False
        matches = re.search(r"([a-h][1-8]) ([a-h][1-8])", input_move)
        return matches.group(1), matches.group(2)

    # get indeces of given move
    def get_indeces(self, start_position, end_position):
        start_colum, start_row = str(start_position[0]), int(start_position[1])
        start_row_index = int(start_row - 1)
        start_colum_index = ord(start_colum) - ord("a")

        end_colum, end_row = str(end_position[0]), int(end_position[1])
        end_row_index = int(end_row - 1)
        end_colum_index = ord(end_colum) - ord("a")

        return start_row_index, start_colum_index, end_row_index, end_colum_index

    # check move logic
    def is_valid_logic(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=False):

        # check if player tries to move a piece
        if board[start_row_index][start_colum_index].type == None:
            if not is_check:
                print("No Piece on this Field!")
            return False

        #check if player tries to move its own piece
        elif board[start_row_index][start_colum_index].color != current_player: # --> Is the player moving his own piece?
            if not is_check:
                print("You have to move your own Piece!")
            return False

        #check if player tries to hit his own piece
        elif board[end_row_index][end_colum_index].color == current_player: # --> ist eine eigene Figur auf dem Zielfeld
            if not is_check:
                print ("You cannot hit your own Piece")
            return False



        #check which piece is to be moved and call its specific logic
        # safe piece_symvol as string
        piece_symbol = str(board[start_row_index][start_colum_index]).lower()
        #check if piece is in piece_classes dict --> Should be the case every time
        if piece_symbol in self.piece_classes:
            # safe piece_class by indexing in dict with the symbol
            piece_class = self.piece_classes[piece_symbol]
            # give the class its parameters by giving it the same properties like the object on the board
            piece = piece_class(board[start_row_index][start_colum_index].type, board[start_row_index][start_colum_index].color)
            # check if piece_logic is valid
            if piece.type in ["K","k"]:
                if not piece.is_valid(board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player,
                                      K_moved=self._K_moved, k_moved=self._k_moved, _00R_moved=self._00R_moved, _07R_moved=self._07R_moved,
                                       _70r_moved=self._70r_moved, _77r_moved=self._77r_moved, is_check=is_check):
                    return False
            else:
                if not piece.is_valid(board, start_row_index, start_colum_index, end_row_index, end_colum_index, current_player, is_check=is_check):
                    return False

        return True

    # check if current or suggested move is in_check
    def is_check(self, board, start_row_index, start_colum_index,
                 end_row_index, end_colum_index, current_player, check_current_position=False, search_checking_pieces=False):

        # Duplicate the originial board
        virtual_board = [row[:] for row in board]
        # Try the move only if it is not the current board that should be checked
        if check_current_position == False:
            # check if king wants to go out of bound
            if not (0 <= end_row_index <= 7)  or not (0<=end_colum_index <=7):
                return True
            # check if piece can even move there, because field might be occupied by own piece
            if virtual_board[end_row_index][end_colum_index].color == current_player:
                # try the move
                return True
            # try move if it is valid
            virtual_board = self.move_piece (virtual_board, start_row_index, start_colum_index, end_row_index, end_colum_index)


        # find king
        king_row, king_col = self.find_king(virtual_board, current_player)

        # create dict where checking pieces will be stored only if search_checking_pieces = True
        if search_checking_pieces:
            checking_pieces = {}
        # Check if king in Check
        # loop through every Field
        for r, row in enumerate(virtual_board):
            for o, object in enumerate(row):
                    # check for enemy pieces
                    if object.color != current_player and object.color != None:
                        # check if they can hit the king
                        if self.is_valid_logic(virtual_board, r, o, king_row, king_col, virtual_board[r][o].color, is_check=True):
                            # if specified ad checking piece and position to dict
                            if search_checking_pieces:
                                checking_pieces[f"{r},{o}"] = object.type
                            else:
                                return True
        if search_checking_pieces:
            return checking_pieces
        return False


    #move the piece
    def move_piece(self, board, start_row_index, start_colum_index, end_row_index, end_colum_index, real_move=False):
        # if this is not a move only to be tested and no pawn is moved and no piece is hit increment counter by one
        # irgendwas stimmt hier noch nciht ganz!!!!!!!
        if real_move and board[start_row_index][start_colum_index].type not in ["P", "p"] and board[end_row_index][end_colum_index].color == None:
            self._remis_counter += 1
        elif real_move and (board[start_row_index][start_colum_index].type in ["P", "p"] or board[end_row_index][end_colum_index].color == None):
            self._remis_counter = 0

        # check if rochade is occurring, if yes also move the corresponding rook --> maybe i should put that in its own function
        # king is moved
        if real_move and board[start_row_index][start_colum_index].type in ["K","k"]:
            self.process_rochade(board, start_row_index, end_colum_index)

        # Move the actual piece
        # What was on the start position is is duplicated to the end position
        board[end_row_index][end_colum_index] = board[start_row_index][start_colum_index]
        # Start position is now empty
        board[start_row_index][start_colum_index] = Piece(None, None)

        # pawn can change if on last field
        if  real_move == True and board[end_row_index][end_colum_index].type in ["P","p"] and (end_row_index == 0 or end_row_index == 7):
            self.change_pawn(board, end_row_index, end_colum_index)

        # White king moved
        if real_move == True and start_row_index == 0 and start_colum_index == 4:
            self._K_moved = True
        # Black king moved
        elif real_move == True and start_row_index == 7 and start_colum_index == 4:
            self._k_moved = True
        # one of the Rooks moved
        elif real_move == True and start_row_index == 0 and start_colum_index == 0:
            self._00R_moved = True
        elif real_move == True and start_row_index == 0 and start_colum_index == 7:
            self._07R_moved = True
        elif real_move == True and start_row_index == 7 and start_colum_index == 0:
            self._70r_moved = True
        elif real_move == True and start_row_index == 7 and start_colum_index == 7:
            self._77r_moved = True

        # return the new board
        return board

    def change_pawn(self, board, end_row_index, end_colum_index):
            current_player = board[end_row_index][end_colum_index].color
            while True:
                new_figure = input("Which figure do you want? Give the first character of the piece type: ")
                if current_player == "White":
                    new_figure = new_figure.upper()
                else:
                    new_figure = new_figure.lower()

                if new_figure.lower() in ["r", "k", "b", "q"]:
                    board[end_row_index][end_colum_index] = Piece(new_figure, current_player)
                    break
                print ("invalid figure")

    def process_rochade(self, board, start_row_index, end_colum_index):
            # White king is moved first time
            if start_row_index == 0 and not self._K_moved:
                # short rochade
                if end_colum_index == 6:
                    board[0][5] = board[0][7]
                    board[0][7] = Piece(None, None)
                # long rochade
                elif end_colum_index == 2:
                    board[0][3] = board[0][0]
                    board[0][0] = Piece(None, None)
            # Black king is moved first time
            elif start_row_index == 7 and not self._k_moved:
                # short rochade
                if end_colum_index == 6:
                    board[7][5] = board[7][7]
                    board[7][7] = Piece(None, None)
                # long rochade
                elif end_colum_index == 2:
                    board[7][3] = board[7][0]
                    board[7][0] = Piece(None, None)

    def is_checkmate(self, board, current_player):

        # check if currentposition is in check
        if not self.is_check(board, None,None,None,None, current_player, check_current_position=True):
            return False
        else:
            # check if king has valid moves --> if yes return False
            if not self.check_king_moves(board, current_player):
                return False
            # else store king position
            king_row, king_col = self.check_king_moves(board, current_player)

            # find possible blocking fields
            checking_pieces_dict = self.is_check(board, None,None,None,None, current_player, check_current_position=True, search_checking_pieces=True)
            # if this pieces are giving check no block is possible
            check_mate_pieces = ["N","n","P","p"]
            # If two pieces are checking there is no block possible --> Checkmate
            if len(checking_pieces_dict) > 1:
                return True
            # If one of the checkmate_pieces is giving check, no block is possible --> Checkmate
            for piece in check_mate_pieces:
                if piece in checking_pieces_dict.values():
                    return True
            # get row and colum of the checking piece
            checking_key = next(iter(checking_pieces_dict.keys()))
            checking_row, checking_col = map(int, checking_key.split(","))

            # check if there is a valid move to either block the piece or hit the checking piece
            # if vertical movement
            if checking_col == king_col:
                for row in range (abs (checking_row - king_row)):
                    if checking_row > king_row:
                        if self.is_blockable_fields(board, king_row + row + 1, king_col, current_player):
                            return False
                    else:
                        if self.is_blockable_fields(board, king_row - row - 1, king_col, current_player):
                            return False
            # if horizontal movement
            elif checking_row == king_row:
              for col in range (abs (checking_col - king_col)):
                    if checking_col > king_col:
                        if self.is_blockable_fields(board, king_row, king_col + col + 1, current_player):
                            return False
                    else:
                        if self.is_blockable_fields(board, king_row, king_col - col - 1, current_player):
                            return False
            # if diagonal movement
            else:
                for row in range (abs (checking_row - king_row)):
                    for col in range (abs (checking_col - king_col)):
                        if king_row > checking_row and king_col > checking_col:
                            if self.is_blockable_fields(board, king_row - row - 1, king_col - col - 1, current_player):
                                return False
                        elif king_row > checking_row and king_col < checking_col:
                            if self.is_blockable_fields(board, king_row - row - 1, king_col + col + 1, current_player):
                                return False
                        elif king_row < checking_row and king_col > checking_col:
                            if self.is_blockable_fields(board, king_row + row + 1, king_col - col - 1, current_player):
                                return False
                        else:
                            if self.is_blockable_fields(board, king_row + row + 1, king_col + col + 1, current_player):
                                return False
            return True


    def is_remis(self, board, current_player):

        # check if it is patt
        if self.is_patt(board, current_player):
            return True
        # if the counter run in the move-piece-function is at 50 it is patt automatically
        elif self._remis_counter == 50:
            return True

        return False

    # find position of the king
    # loop through every field and search for the king with the right color
    def find_king(self, board, current_player):
        for r, row in enumerate(board):
            for o, object in enumerate(row):
                if object.type in ["k","K"] and object.color == current_player:
                    return r, o

    # run through all blocking or hitting positions given by check_mate function and see if a valid move goes there
    def is_blockable_fields(self, board, end_row, end_col, current_player):
        for r, row in enumerate(board):
            for c, object in enumerate(row):
                if object.color == current_player and object.type not in ["K","k"]:
                    if self.is_valid_logic (board, r, c, end_row, end_col, current_player, is_check=True):
                        return True
        return False


    def check_king_moves(self, board, current_player):
        # find king
        king_row, king_col = self.find_king(board, current_player)
        # check king moves
        for horizontal_move in range(-1,2):
            for vertical_move in range (-1,2):
                # check if possible move
                if not self.is_check(board, king_row, king_col, king_row + horizontal_move, king_col + vertical_move, current_player):
                    return False

        return king_row, king_col

    # check if it is patt
    def is_patt(self, board, current_player):
        # duplicate board
        virtual_board = [row[:] for row in board]

        # check, that the king is not in check, otherwise it would be check_mate
        if self.is_check(board, None,None,None,None,current_player, check_current_position=True):
            return False

        # run through every piece and check if it has a valid move
        for r, row in enumerate(virtual_board):
            for o, object in enumerate(row):
                if object.color == current_player:
                    for cr, checking_row in enumerate(virtual_board):
                        for co, checking_object in enumerate(checking_row):
                            if self.is_valid_logic(virtual_board, r,o,cr,co, current_player, is_check=True):
                                if not self.is_check(virtual_board, r, o, cr, co, current_player):
                                    return False

        return True


    def safe_game(self, board, current_player):
        filename = input("Please give the filename: ")
        self.safe_board(board, filename)
        self.safe_variables(current_player, filename)
        print("Game saved")
        sys.exit()


    def reload_game(self, filename):
        self.reload_board(filename)
        current_player = self.reload_variables(filename)
        return current_player


    def safe_board(self, board, filename):
        # filename is players given name plus board plus filetype
        filename = f"saved_games/{filename}_board.csv"
        with open(filename, 'w', newline='') as file:
            # chacnge delimiter to | so that , in the file are no problem
            writer = csv.writer(file, delimiter='|')
            #run through every row
            for row in board:
                # give it the format it should be safed in
                row_data = [(piece.type, piece.color) if piece is not None else (None, None) for piece in row]
                writer.writerow(row_data)
        return

    def safe_variables(self, current_player, filename):
        # filename is changed again
        filename = f"saved_games/{filename}_variables.csv"
        with open (filename, "w", newline='') as file:
            # use dict to store variables
            writer = csv.DictWriter(file, fieldnames=["current_player", "remis_counter", "K_moved", "k_moved", "00R_moved", "07R_moved", "70r_moved", "77r_moved"])
            writer.writeheader()
            writer.writerow({"current_player": current_player, "remis_counter": self._remis_counter, "K_moved": self._K_moved,
                              "k_moved": self._k_moved, "00R_moved": self._00R_moved, "07R_moved": self._07R_moved,
                                  "70r_moved": self._70r_moved, "77r_moved": self._77r_moved})
        return

    def reload_board(self, filename):
        filename = f"saved_games/{filename}_board.csv"
        # check if filename exists
        if not os.path.isfile(filename):
            print("File does not exist!")
            sys.exit()
        # create empty board
        board = []
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter='|')
            # iterate through every row in reader
            for row in reader:
                # create empty row
                row_data = []
                # iterate throug the rows
                for piece_data in row:
                    # clean up
                    piece_type, piece_color = piece_data.split(',')
                    piece_type = piece_type.replace("'", "").replace("(", "").strip()
                    piece_color = piece_color.replace("'", "").replace(")", "").strip()
                    # if is None create piece with None,None
                    if piece_type == 'None' and piece_color == 'None':
                        piece = Piece(None, None)
                    # else create piece like specified
                    else:
                        piece = Piece(piece_type, piece_color)
                    # build everything
                    row_data.append(piece)
                board.append(row_data)
        self._board = board
        return

    def reload_variables(self, filename):
        # create empty variable list
        variables = []
        filename = f"saved_games/{filename}_variables.csv"
        with open (filename, "r", newline='') as file:
            reader = csv.DictReader(file)
            # iterate through the row
            for row in reader:
                # create a dict in the row with the variable_names as keys and the values as values
                variables.append({"current_player": row["current_player"], "remis_counter": row["remis_counter"], "K_moved": row["K_moved"],
                              "k_moved": row["k_moved"], "00R_moved": row["00R_moved"], "07R_moved": row["07R_moved"],
                                  "70r_moved": row["70r_moved"], "77r_moved": row["77r_moved"]})

        # ich muss hier noch testen ob das alles klappt
        # restore all the variables
        current_player = variables[0]["current_player"]
        # str needs to be converted into int
        self._remis_counter = int(variables[0]["remis_counter"])

        # change all the strings in bools
        self._K_moved = variables[0]["K_moved"] == "True"
        self._k_moved = variables[0]["k_moved"] == "True"
        self._00R_moved = variables[0]["00R_moved"] == "True"
        self._07R_moved = variables[0]["07R_moved"] == "True"
        self._70r_moved = variables[0]["70r_moved"] == "True"
        self._77r_moved = variables[0]["77r_moved"] == "True"

        #return the current_player to the main_function
        return current_player


