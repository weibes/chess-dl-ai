"""
Author: Brendan Weibel
Stores internal board representation of the chess board
Not to be used, just using python-chess for now.
"""


"""

import numpy as np


class ChessBoardException():
    def __init__(self, description):
        self.description =  description
        super().__init__(description)

class ChessBoard:
    

    \"""
    board variable stores board state
    stored as a numpy array with the shape (8, 8, 2), where the first dim is the ranks (1-8), the 2nd dim is the file (a-g), and the 3rd dim will be the following:
        position 0: the piece name
        position 1: either 'w' or 'b', representing if its black or white
        If position 0 is blank, then position 1 shouldn't matter, as it represents no piece there.
    the first 2 
    p: pawn
    n: knight
    b: bishop
    r: rook
    k: king
    q: queen
    \"""
    def __init__ (self, board=None):
        if board.shape() != (8, 8, 2):
            raise ChessBoardException('Given board shape not valid.')
        
        self.board = board


    def set_board(self, board):
        if board.shape() != (8, 8, 2):
            raise ChessBoardException('Given board shape not valid.')
        
        self.board = board
    
    def get_board(self):
        if self.board == None:
            raise ChessBoardException('There is no chess board saved.')
        return self.board



    # input: location as 2d numpy array
    # output: a numpy array of shape (2) with position 0 giving the piece name, positing 2 giving 'w' or 'b'
    def get_board_location(self, location):
        if location.shape() != np.zeros((2)).shape()
        return self.board[location]
    

   
"""
