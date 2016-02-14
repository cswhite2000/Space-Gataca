
import pygame,sys,math
from pygame.locals import *
from Ship import *
from Bullets import *
from Bullet import *
from Enemies import *
from Enemy import *

pygame.init()
pygame.key.set_repeat(1,1)
screen = pygame.display.set_mode((800,600))
background = pygame.Surface((800,600))

ship = Ship(100,450)
bullets= Bullets()
lastShootTime=0
lastEnemyShoot=0

enemies=Enemies()
enemies.addNew(100,100)
enemies.addNew(200,100)

while True:# Game loop
    screen.blit(background,(0,0))
    ship.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    
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
            elif event.key==K_SPACE:
                #bullets.addNew(ship.x,ship.y)
                if pygame.time.get_ticks()>lastShootTime+500:
                    bullets.addNew(ship.x+34,ship.y-30)
                    lastShootTime=pygame.time.get_ticks()
            if pygame.time.get_ticks()>lastEnemyShoot+500:
                    i=0
                    while i<len(enemies.enemies):
                        enemies.addBlast(enemies.enemies[i].x,enemies.enemies[i].y)
                        i+=1
                    lastEnemyShoot=pygame.time.get_ticks()
    bullets.tick()
    enemies.tick()
    pygame.time.wait(10)
