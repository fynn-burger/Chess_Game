# CHESS GAME
This project is a player vs player Chess game in the command line. The players will alternate moves in the format e2 e4
Implemented functionality: Surrender, Draw, Save, and Reload, All the move-logic except en-passant, most of the checkmate and remis cases
#### Video Url: https://youtu.be/su36lOdtGNY
#### Descriptions
The project consists of the main file, a board, and a piece class as well as classes for all the piece types. It also includes test-files
for every functional file.
##### Main function and other functions on the same indentation level
In the main Function first is handled what should follow if the User reloads a game before the Gameloop starts
Then the game loop will ask as long as no checkmate or remis occurred for an Input.
Remis and Surrender behavior is handled on functions on the same indentation level and saving a game in the board class.
If the player inputs a move this is checked through the board and respective piece class, and then the move is done
and the current player is changed. The loop begins anew.
If checkmate or Remis occurs there will be a message about who won or about the Remis
##### Board Class
Here the board is initialized (as a list of lists, containing objects of the piece class) and there are the following functions
__display()__: Displays the Board  
__is_valid_move()__: calls functions to check the input format, calculate the board indices, check move-logic and if the player tries to move into check.  
__is_valid_format()__: Checks for format e2 e4 and that the start and end-position are on a 8x8 board.  
__is_valid_logic()__: Checks if the player is trying to move its own piece and not trying to capture its own piece  
                  Then it calls the appropriate class to check the specific move logic.
__is_check()__: Creates a virtual board, to then loop over every piece and check if they have a valid move to capture the king
            It can check the current position and the position after the proposed move and it can give back a dict of the checking pieces.
__move_piece__: If the move is valid, this function is called to move the piece. It indexes into the list of lists and changes it. Here we
                also have functions to check if rochade occurred, to then move the rook too, to check if a piece that could participate in
                rochade is moved to save this and make a later rochade impossible, and a counter to count moves that do not involve a pawn
                or a captured piece, for the Remis rule.
__change_pawn()__: Changes the pawn to another figure if on the last line.
__is_checkmate()__: Checks if the current player is in check, if he has any valid king move, and if there are moves to either block the check
                    or capture the checking piece. (Using the is_check and other functions to find the king etc.)
__is_patt()__: Checks by looping through every piece and then every field on the board, if there is any possible move if the king is not in check
__is_remis()__: Checks if is_patt is True or the counter of move_piece is at 50. If yes it is Remis
__saving and reloading__: I have a few functions to save a current game to two CSV files, one with the board and one with the relevant variables
                          And there are functions to if reloaded initialize the board with this board and the reloaded variables

##### Piece Class
Short superclass for all the pieces, that are initialized with Type and Color, and there is one __str__ function
###### Rook Class
Handles move-logic specific to the rook and checks for possible obstacles
###### Pawn Class
Handles move-logic specific to the pawn and checks for possible obstacles
Including diagonal capturing and the possibility of going to fields if on the baseline
--> Here one could also implement en-passant, which I did not
###### Knight Class
Handles move-logic specific to the knight and checks for possible obstacles
###### Bishop Class
Handles move-logic specific to the bishop and checks for possible obstacles
###### Queen Class
Handles move-logic specific to the queen and checks for possible obstacles
###### King Class
Handles move-logic specific to the king and checks for possible obstacles
Including Rochade
