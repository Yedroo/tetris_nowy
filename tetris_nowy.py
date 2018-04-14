import pygame, sys
from pygame.locals import *

screen_width = 800     #szerokość okna
screen_height = 600    #wysokość okna
squarex = screen_width/2
squarey = 0

pygame.init()


FPS = 30
fpsClock = pygame.time.Clock()

# okno i opis
DISPLAY_SURFACE = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

# wykorzystywane kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 187, 0)
GRAY = (225, 225, 225)

# kwadrat
dir = 'down'
square_width = 100
square_height = 100
square_pos = ((screen_width - square_width)/2, 0)
square = pygame.Surface([square_width, square_height])
square.fill(BLACK)
square_prost = square.get_rect()
square_prost.x = square_pos[0]
square_prost.y = square_pos[1]
DISPLAY_SURFACE.blit(square, square_pos)

# pętla programu
while True:
    DISPLAY_SURFACE.fill(GRAY)

# ruch niezależny
    if dir =='down':
        square_prost.y +=5
        if square_prost.y >= screen_height-square_height:
            dir = 'up'

    DISPLAY_SURFACE.blit((square), (square_prost.x, square_prost.y))

# utrzymywanie okna
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# sterowanie przez użytkownika
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            square_prost.x -= 5
            if square_prost.x< 0:
                square_prost.x = 0
        if event.key == pygame.K_RIGHT:
            square_prost.x += 5
            if square_prost.x> screen_width - square_width:
                square_prost.x = screen_width - square_width

    pygame.display.update()
    fpsClock.tick(FPS)
