
import pygame,sys,math
from pygame.locals import *
from Ship import *


pygame.init()
pygame.key.set_repeat(1,1)
screen = pygame.display.set_mode((800,600))
background = pygame.Surface((800,600))

ship= Ship(100,100)

while True:# Game loop
    screen.blit(background,(0,0))
    ship.draw(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT or (event.type==KEYUP and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type==KEYDOWN:
            if event.key==K_UP:
                ship.moveUp()
            elif event.key==K_DOWN:
                ship.moveDown()
            elif event.key==K_LEFT:
                ship.moveLeft()
            elif event.key==K_RIGHT:
                ship.moveRight()
    pygame.time.wait(10)
