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
            self.speed -= self.acceleration # Going forwards (what we think is forwards) is actually going backwards to pygame, so we just "slow down" to speed up and vice versa 
        if doSlow:
            self.speed += self.acceleration
        if left:
            self.direction += self.turnspeed
        if right:
            self.direction -= self.turnspeed
        if self.speed > 0: # Stops the spaceship from going in reverse, because thats not what spaceships do.
            self.speed = 0
        if self.speed < self.maxspeed*-1:
            self.speed = self.maxspeed*-1
        # Finds which stage of the Animation the ship should show
        if math.floor(self.speed*-1) <= 0:
            number = "00"
        elif math.floor(self.speed*-1)<=9:
            number = f"0{math.floor(self.speed*-1)}"
        else:
            number = f"{math.floor(self.speed*-1)}"
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
