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

width = 1000
height = 1500

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((width, height))
pygame.display.set_caption('kiedyś będzie Tetris')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 187, 0)
GRAY = (225, 225, 225)

DISPLAY_SURFACE.fill(GRAY)
#pygame.draw.line(DISPLAY_SURFACE, BLACK, (60, 60), (120, 60), 4)
#pygame.draw.line(DISPLAY_SURFACE, WHITE, (60, 70), (120, 70), 4)
#pygame.draw.circle(DISPLAY_SURFACE, WHITE, (300, 50), 20, 0)
pygame.draw.rect(DISPLAY_SURFACE, GREEN, (int(len(width))/2, 0, 250, 250))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
