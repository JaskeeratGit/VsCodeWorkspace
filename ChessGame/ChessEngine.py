"""
Managing current state of the game and deciding all possible moves.
"""

class State():
    def __init__(self):
        self.chessboard = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
                           ["bP","bP","bP","bP","bP","bP","bP","bP"],
                           ["--","--","--","--","--","--","--","--"],
                           ["--","--","--","--","--","--","--","--"],
                           ["--","--","--","--","--","--","--","--"],
                           ["--","--","--","--","--","--","--","--"],
                           ["wP","wP","wP","wP","wP","wP","wP","wP"],
                           ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.WhiteMove = True
        self.MoveList = []
    
    def doMove(self, move):
        self.chessboard[move.initialRow][move.initialCol] = "--"               # Problem Here
        self.chessboard[move.finalRow][move.finalCol] = move.pieceSelected     # Problem Here
        self.MoveList.append(move)
        self.WhiteMove = not self.WhiteMove


class Move():
    def __init__(self, start, end, chessboardInst):
        self.initialRow = start[0]
        self.initialCol = start[1]
        self.finalRow = end[0]
        self.finalCol = end[1]
        self.pieceSelected = chessboardInst[self.initialRow][self.initialCol]
        self.pieceCap = chessboardInst[self.finalRow][self.finalCol]
        
        