import pygame, sys, random, time
from pygame.locals import *

WINDOWWIDTH = 800     #szerokość okna
WINDOWHEIGHT = 600    #wysokość okna
board_width = 10
board_height = 20
#squarex = screen_width/2
#squarey = 0

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5
S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]
Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]
I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]
O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]
J_SHAPE_TEMPLATE = [['.....',
                     '.O...',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..OO.',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '...O.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '.OO..',
                     '.....']]
L_SHAPE_TEMPLATE = [['.....',
                     '...O.',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..O..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '.O...',
                     '.....'],
                    ['.....',
                     '.OO..',
                     '..O..',
                     '..O..',
                     '.....']]
T_SHAPE_TEMPLATE = [['.....',
                     '..O..',
                     '.OOO.',
                     '.....',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     '.OOO.',
                     '..O..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '..O..',
                    '.....']]
SHAPES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}



FPS = 30
fpsClock = pygame.time.Clock()

# okno i opis
#DISPLAY_SURFACE = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption('Tetris')

# wykorzystywane kolory

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 187, 0)
GRAY = (225, 225, 225)
LIGHTGRAY = (100, 100, 100)

COLORS = ( BLACK, WHITE, GREEN, GRAY )
BGCOLOR = LIGHTGRAY
# kwadrat
#dir = 'down'
#square_width = 100
#square_height = 100
#square_pos = ((screen_width - square_width)/2, 0)
#square = pygame.Surface([square_width, square_height])
#square.fill(BLACK)
#square_prost = square.get_rect()
#square_prost.x = square_pos[0]
#square_prost.y = square_pos[1]
#DISPLAY_SURFACE.blit(square, square_pos)

# pętla programu
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)
    pygame.display.set_caption('Tetris działaj plz')
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()
    while True:
        DISPLAYSURF.fill(GRAY)
        if fallingPiece == None:
             fallingPiece = nextPiece
             nextPiece = getNewPiece()
        runGame()

    # ruch niezależny
       # if dir =='down':
        #    square_prost.y +=5
         #   if square_prost.y >= screen_height-square_height:
          #      dir = 'up'

       # DISPLAY_SURFACE.blit((square), (square_prost.x, square_prost.y))

    # utrzymywanie okna
   #     for event in pygame.event.get():
   #         if event.type == QUIT:
   #             pygame.quit()
   #             sys.exit()

    # sterowanie przez użytkownika
       # if dir =='down':
       #     if event.type == pygame.KEYDOWN:
       #             if event.key == pygame.K_LEFT:
       #             square_prost.x -= 5
       #             if square_prost.x< 0:
       #                 square_prost.x = 0
       #         if event.key == pygame.K_RIGHT:
       #             square_prost.x += 5
       #             if square_prost.x> screen_width - square_width:
       #                 square_prost.x = screen_width - square_width
       # pygame.display.update()
       # fpsClock.tick(FPS)

def runGame():
    #ustawianie własnosci okna na start
    board = getBlankBoard()
    fallingPiece = getNewPiece()
    nextPiece = getNewPiece()
    while True:
        if fallingPiece == None:
            #nie ma żadnego kształtu więc stwórz nowy
            fallingPiece = nextPiece
            nextPiece = getNewPiece()

           # for event in pygame.event.get():
           #     if event.type == KEYUP:




            DISPLAYSURF.fill(BGCOLOR)
            drawBoard(board)
           # drawNextPiece(nextPiece)
        if fallingPiece != None:
            drawPiece(fallingPiece)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def getNewPiece():

# zwraca losoy element o losowym ustawieniu i losowym kolorze
    shape = random.choice(list(SHAPES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(SHAPES[shape]) - 1),
                'x': int(WINDOWWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece

def getBlankBoard():
    #tworzy pustą planszę
    board = []
    for i in range (board_width):
        board.append ([blank] * board_height )
    return board

def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()
#def drawPiece(piece, pixelx =None, pixely=None):
    #shapeToDraw = SHAPES[piece['shape']][piece['rotation']]
