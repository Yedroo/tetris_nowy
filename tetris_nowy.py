import pygame, sys
from pygame.locals import *

colors = [
(0,   0,   0  ),
(255, 85,  85),
(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) # Helper color for background grid
]

# Define the shapes of the single parts
tetris_shapes = [
	[[1, 1, 1],
	 [0, 1, 0]],

	[[0, 2, 2],
	 [2, 2, 0]],

	[[3, 3, 0],
	 [0, 3, 3]],

	[[4, 0, 0],
	 [4, 4, 4]],

	[[0, 0, 5],
	 [5, 5, 5]],

	[[6, 6, 6, 6]],

	[[7, 7],
	 [7, 7]]
]

screen_width = 800     #szerokość okna
screen_height = 600    #wysokość okna
squarex = screen_width/2
squarey = 0

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

DISPLAY_SURFACE = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('kiedyś będzie Tetris')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 187, 0)
GRAY = (225, 225, 225)

#DISPLAY_SURFACE.fill(GRAY)
#pygame.draw.line(DISPLAY_SURFACE, BLACK, (60, 60), (120, 60), 4)
#pygame.draw.line(DISPLAY_SURFACE, WHITE, (60, 70), (120, 70), 4)
#pygame.draw.circle(DISPLAY_SURFACE, WHITE, (300, 50), 20, 0)
#pygame.draw.rect(DISPLAY_SURFACE, GREEN, (squarex-50, 0, 100, 100))

#while squarey < height:     #automatic square drop

dir = 'down'



#square = pygame.draw.rect(DISPLAY_SURFACE, GREEN, (squarex-50, 0, 100, 100))
square_width = 100
square_height = 100
square_pos = ((screen_width - square_width)/2, 0)
square = pygame.Surface([square_width, square_height])
square.fill(BLACK)
square_prost = square.get_rect()
square_prost.x = square_pos[0]
square_prost.y = square_pos[1]
DISPLAY_SURFACE.blit(square, square_pos)

while True:
    DISPLAY_SURFACE.fill(GRAY)


    if dir =='down':
        square_prost.y +=20
        if square_prost.y >= screen_height-square_height:
            dir = 'up'
   # elif dir == 'up':
   #    square_prost.y -= 20
   #     if square_prost.y <= 0:
   #         dir = 'down'
    DISPLAY_SURFACE.blit((square), (square_prost.x, square_prost.y))


   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

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
