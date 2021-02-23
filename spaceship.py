import pygame
from pygame.locals import *
import globalvariables as globals
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction):
        super().__init__() # Very important
        self.appearance = appearance
        self.image = pygame.image.load("testpic.png")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.speed = 0
        self.rect = self.image.get_rect()
        self.rect.center = coords
        return
    def update(self,doThrust,doSlow):
        if doThrust:
            self.speed += self.acceleration
        if doSlow:
            self.speed -= self.acceleration
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        self.rect.x+=self.speed
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
