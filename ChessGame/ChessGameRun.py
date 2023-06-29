import pygame


"""
Displaying current state of the game and handling user input and output
"""

import pygame as m
import ChessEngine
m.init()

#Setting the dimensions of the board and the size of each square on the 8 x 8 board and loading all piece images into a dictionary
W = H = 800
DIMENSION = 8
SIZE = 100
ImgPieces = {}
FPS = 15

"""
Initializing dict of images
"""
def loadImgPieces():
    #transforms and loads each img to scale of each square into the dictionary
    ImgPieces['bB'] = m.transform.scale(m.image.load("images/bB.png"),(SIZE, SIZE))
    ImgPieces['bK'] = m.transform.scale(m.image.load("images/bK.png"),(SIZE, SIZE))
    ImgPieces['bN'] = m.transform.scale(m.image.load("images/bN.png"),(SIZE, SIZE))
    ImgPieces['bP'] = m.transform.scale(m.image.load("images/bP.png"),(SIZE, SIZE))
    ImgPieces['bQ'] = m.transform.scale(m.image.load("images/bQ.png"),(SIZE, SIZE))
    ImgPieces['bR'] = m.transform.scale(m.image.load("images/bR.png"),(SIZE, SIZE))
    ImgPieces['wB'] = m.transform.scale(m.image.load("images/wB.png"),(SIZE, SIZE))
    ImgPieces['wK'] = m.transform.scale(m.image.load("images/wK.png"),(SIZE, SIZE))
    ImgPieces['wN'] = m.transform.scale(m.image.load("images/wN.png"),(SIZE, SIZE))
    ImgPieces['wP'] = m.transform.scale(m.image.load("images/wP.png"),(SIZE, SIZE))
    ImgPieces['wQ'] = m.transform.scale(m.image.load("images/wQ.png"),(SIZE, SIZE))
    ImgPieces['wR'] = m.transform.scale(m.image.load("images/wR.png"),(SIZE, SIZE))

    #For accessing img we can use ImgPieces['imgname']

"""
Handling input and output on graphic board
"""

def main():
    DispScreen = m.display.set_mode((W, H))
    clock = m.time.Clock()
    DispScreen.fill(m.Color("white"))
    game1 = ChessEngine.State() # initializing board
    loadImgPieces() # loading all images
    running = True
    selectedSq = () # last click of the user. Reset after each click
    selectedPair = [] # last 2 clicks of the user. Reset after 2 clicks
    while running:
        for event in m.event.get():
            if event.type == m.QUIT:
                running = False
            elif event.type == m.MOUSEBUTTONDOWN:
                coordinate = m.mouse.get_pos()
                col1 = coordinate[0]//SIZE      # gives row and column on the chess board
                row1 = coordinate[1]//SIZE
                if selectedSq == (row1, col1): # user has selected the same square. Do not update WhiteMove
                    selectedSq == ()
                    selectedPair == []
                else:
                    selectedSq = (row1, col1)   
                    selectedPair.append(selectedSq)
                if len(selectedPair) == 2:
                    currentmove = ChessEngine.Move(selectedPair[0],selectedPair[1], game1.chessboard)
                    game1.doMove(currentmove)
                    print(selectedPair)
                    print(game1.WhiteMove)
                    selectedSq = () # resetting the selected square
                    selectedPair = [] # resetting the list to 0 elements so a new pair can be selected

        drawGraphics(DispScreen, game1.chessboard)
        clock.tick(FPS)
        m.display.flip()

def drawGraphics(DispScreen, chessboard):
    sqcolour = [m.Color("#fccc74"), m.Color("#8a785d")]
    for row in range(8):
        for column in range(8):
            colour = sqcolour[(row + column)%2] # setting the colours of the smaller squares
            m.draw.rect(DispScreen, colour, m.Rect(column*SIZE, row*SIZE, SIZE, SIZE))
            PieceOnSq = chessboard[row][column]
            if PieceOnSq != "--":
                DispScreen.blit(ImgPieces[PieceOnSq], m.Rect(column*100, row*100, 100, 100)) # blitting pieces on to the squares to positions
main()
    
   
