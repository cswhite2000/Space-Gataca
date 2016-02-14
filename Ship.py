import pygame
from pygame.locals import *

class Ship:
    def __init__ (self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("https://cloud.githubusercontent.com/assets/15203641/13030928/2a482cb0-d26f-11e5-80a5-67f7e2bee92e.png")
    def draw(self, window):
        window.blit(self.img, (self.x,self.y))
    def moveLeft(self):
        self.x=self.x-5
    def moveRight(self):
        self.x=self.x+5
    def moveUp(self):
        self.y=self.y-5
    def moveDown(self):
        self.y=self.y+5
