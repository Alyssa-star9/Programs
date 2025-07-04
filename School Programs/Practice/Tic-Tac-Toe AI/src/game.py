# This is an unbeatable super computer that will either win or tie every tic-tac-toe game that it plays.
# This game acts as a practice for custom functions.

import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

# Define the function to create the board (essentially just the visual ouput).
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)] # this is a single list used to represent a 3x3 board
        self.current_winner = None # this is to keep track of the winner!

    def print_board(self):
        #This is just for getting the rows.
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # tells us which row to pick
            print("│ " + " │ ".join(row) + " │") # this is basically saying join them in a string where the seperator is this vertical line

    @staticmethod
    def print_board_nums():
        # 0 │ 1 │ 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] # give me the row indices
        for row in number_board:
             print("│ " + " │ ".join(row) + " │")
    
    def available_moves(self):
        # this shows what moves are left to be made after a move has already been made
        return [i for i, spot in enumerate(self.board) if spot == " "] # this is an empty space, and thus an available move
    
    def empty_squares(self):
        return " " in self.board
    
    def num_empty_squares(self):
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        # if invalid move, then make the move (assign square to letter)
        # then return try. if invalid, return false
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row anywhere, so we have to check all of these!
        # first let's check the row
        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # check column
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal_1]):
                return True
            diagonal_2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal_2]):
                return True
            
        # if all of these checks fail
        return False

def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game (the letter! or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = "X" # starting letter
    # iterate while the game still has empty squares
    # (we don't have to worry about the winner because we'll just return that
    # since it breaks the loop)
    while game.empty_squares():
        # get the move from the apporpriate player
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # let's define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print(" ") # this is just an empty line

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # after we make out move, we need to alternate letters
            letter = "O" if (letter == "X") else "X" # switches player
            # this is the same thing as an if... else loop, just in one line
        
        # tiny break to make things easier to read
        time.sleep(0.8)

    if print_game:
        print("It's a tie!")

# import everything from the player file
if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
