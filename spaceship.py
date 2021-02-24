import pygame
from pygame.locals import *
import globalvariables as globals
import math
def findxy(direction):
        x = math.sin(math.radians(direction))
        y = math.cos(math.radians(direction))
        return [x,y]
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction, turnspeed):
        super().__init__() # Very important
        self.appearance = appearance
        print(f"resources\spaceships\{str(appearance)}\00.png")
        self.originalimage = pygame.image.load(f"resources/spaceships/{str(appearance)}/00.png")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.turnspeed = turnspeed
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
            self.direction += self.turnspeed
        if right:
            self.direction -= self.turnspeed
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        if self.speed < self.maxspeed*-1:
            self.speed = self.maxspeed*-1
        if math.floor(self.speed*-1) <= 0:
            number = "00"
        elif math.floor(self.speed*-1)<=9:
            number = f"0{math.floor(self.speed*-1)}"
        else:
            number = f"{math.floor(self.speed*-1)}"
        print(f"resources/spaceships/{str(self.appearance)}/{number}.png")
        self.originalimage = pygame.image.load(f"resources/spaceships/{str(self.appearance)}/{number}.png")
        xy = findxy(self.direction)
        self.x += xy[0]*self.speed
        self.y += xy[1]*self.speed
        self.image = pygame.transform.rotate(self.originalimage,self.direction)
        self.rect = self.image.get_rect(center=(math.floor(self.x),math.floor(self.y)))
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
