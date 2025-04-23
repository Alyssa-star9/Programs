import socket
import threading

class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.turn = "X"
        self.you = "X" # Person who runs the server
        self.opponent = "O"
        self.winner = None
        self.end_game = False

        self.counter = 0
    
    def host_game(self, host, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

