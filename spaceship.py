import pygame
from pygame.locals import *
import globalvariables as globals
import math
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction):
        super().__init__() # Very important
        self.appearance = appearance
        self.originalimage = pygame.image.load("testpic.png")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.speed = 0
        self.image = pygame.transform.rotate(self.originalimage,direction*-1)
        self.rect = self.image.get_rect(center=coords)
        self.x = coords[0]
        self.y = coords[1]
        return
    def update(self,doThrust,doSlow,left,right):
        if doThrust:
            self.speed += self.acceleration
        if doSlow:
            self.speed -= self.acceleration
        if left:
            self.direction -= self.acceleration
        if right:
            self.direction += self.acceleration
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        self.x+=math.cos(math.radians(self.direction))*self.speed
        self.y+=math.sin(math.radians(self.direction))*self.speed
        self.image = pygame.transform.rotate(self.originalimage,self.direction*-5)
        self.rect = self.image.get_rect(center=(math.floor(self.x),math.floor(self.y)))
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
