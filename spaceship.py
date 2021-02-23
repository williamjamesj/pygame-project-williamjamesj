import pygame
from pygame.locals import *
import globalvariables as globals
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction):
        self.x,self.y = coords # Coordinates in a tuple or list (x,y) or [x,y]
        self.appearance = appearance
        self.image = pygame.image.load("testpic.png")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.speed = 0
    def update(self,doThrust,doSlow):
        if doThrust:
            self.speed += self.acceleration
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        self.x+=self.speed
