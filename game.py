import pygame
from pygame.locals import *

# pygame.init()


BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255,0,0)

DISPLAYSURF = pygame.display.set_mode((500, 500))

mySurface = pygame.Surface((50, 50))

pygame.draw.circle(DISPLAYSURF, WHITE, (250, 250), 30)
pygame.draw.line(DISPLAYSURF, WHITE, (0, 250), (500, 250), 5)
pygame.draw.lines(DISPLAYSURF, WHITE, 1,[(100,100), (150, 100), (200,300)], 5)
#                   surface,   color, 처음과 끝 연결할지 말지, 점들의 리스트, 두께
pygame.draw.polygon(DISPLAYSURF, RED, [(0,0), (400, 200), (150, 380), (300, 250)], 5)


#Game loop begins
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()