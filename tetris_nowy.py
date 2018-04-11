import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello World!')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 187, 0)
GRAY = (225, 225, 225)

DISPLAY_SURFACE.fill(GRAY)
pygame.draw.line(DISPLAY_SURFACE, BLACK, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAY_SURFACE, WHITE, (60, 70), (120, 70), 4)
pygame.draw.circle(DISPLAY_SURFACE, WHITE, (300, 50), 20, 0)
pygame.draw.rect(DISPLAY_SURFACE, GREEN, (200, 150, 100, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
