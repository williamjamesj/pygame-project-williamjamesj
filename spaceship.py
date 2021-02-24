import pygame
from pygame.locals import *
import globalvariables as globals
import math
def findxy(direction):
        x = math.sin(math.radians(direction))
        y = math.cos(math.radians(direction))
        return [x,y]
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction):
        super().__init__() # Very important
        self.appearance = appearance
        self.originalimage = pygame.image.load("testpic.png")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.speed = 0
        self.image = pygame.transform.rotate(self.originalimage,direction)
        self.rect = self.image.get_rect(center=coords)
        self.x = coords[0]
        self.y = coords[1]
        return
    def update(self,doThrust,doSlow,left,right):
        if doThrust:
            self.speed -= self.acceleration
        if doSlow:
            self.speed += self.acceleration
        if left:
            self.direction += 1
        if right:
            self.direction -= 1
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        print(self.direction)
        xy = findxy(self.direction)
        self.x += xy[0]*self.speed
        print (self.x)
        self.y += xy[1]*self.speed
        self.image = pygame.transform.rotate(self.originalimage,self.direction)
        self.rect = self.image.get_rect(center=(math.floor(self.x),math.floor(self.y)))
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
