import sys
import argparse
from final_project.board import Board

def main():
    # initialize board
    board = Board()
    # game starts with white
    current_player = "White"
    # if game is reloaded reload it if not ignore this
    parser = argparse.ArgumentParser(description = "Play Chess")
    parser.add_argument("-l", default="", help="Name of the game you want to load", type=str)
    args = parser.parse_args()
    if args.l != "":
        current_player = board.reload_game(args.l)
    # display board
    board.display()

    # game loop runs as long as check_mate and remis = False
    while not (board.is_checkmate(board._board, current_player) or board.is_remis(board._board, current_player)):
        print()
        # ask for input and call the appropriate functions or start the move code
        player_input = input(f"{current_player}'s move: ")
        if player_input.lower().strip() == "draw":
            is_draw(current_player)
            continue
        elif player_input.lower().strip() == "surrender":
            is_surrender(current_player)
        elif player_input.lower().strip() == "save":
            board.safe_game(board._board, current_player)
        else:
            # check if move is valid
            if not board.is_valid_move(board._board, player_input, current_player):
                pass
            else:
                # if is valid get indeces and pass them to move_piece function
                start_row_index, end_row_index, start_colum_index, end_colum_index = board.is_valid_move(board._board, player_input, current_player)
                board.move_piece(board._board, start_row_index, end_row_index, start_colum_index, end_colum_index, real_move=True)
                board.display()
                # change player
                if current_player == "White":
                    current_player = "Black"
                else:
                    current_player = "White"
    if board.is_checkmate(board._board, current_player):
        checkmate_endgame(current_player)
    elif board.is_remis(board._board, current_player):
        print ("It is a Remis!")
        sys.exit()

def is_draw(current_player):
    answer = input (f"{current_player} wants to draw. Write Y to accept or any other key to decline: ")
    if answer.lower().strip() == "y":
        print("Draw accepted!")
        sys.exit()
    return False

def is_surrender(current_player):
    if current_player == "White":
        print (f"{current_player} surrendered! Black won!")
        sys.exit()
    else:
        print (f"{current_player} surrendered! White won!")
        sys.exit()

def checkmate_endgame(current_player):
    if current_player == "White":
        print ("Black won!")
        sys.exit()
    else:
        print ("White won!")
        sys.exit()

if __name__ == "__main__":
    main()


