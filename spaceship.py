import pygame
from pygame.locals import *
import globalvariables as globals
import math
import os
def findxy(direction):
        x = math.sin(math.radians(direction)) # Trigonometry.
        y = math.cos(math.radians(direction)) # I'm not even going to pretend I thought of this by myself: https://stackoverflow.com/questions/5346874/pygame-making-a-sprite-move-in-the-direction-it-is-facing.
        return [x,y]
def findImages(directory):
    fileslist = []
    filenames = []
    for i in os.listdir(directory):
        filenames.append(i)
    filenames.sort()
    print(filenames)
    for i in filenames:
        fileslist.append(pygame.image.load(os.path.join(directory,i)).convert_alpha())
    return fileslist
class Spaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction, turnspeed):
        super().__init__() # Very important
        self.appearance = appearance
        self.imagelist = findImages(f"resources/spaceships/{str(appearance)}/")
        self.maxspeed = maxspeed
        self.acceleration = acceleration
        self.direction = direction
        self.turnspeed = turnspeed
        self.speed = 0
        self.image = pygame.transform.rotate(self.imagelist[0],direction)
        self.rect = self.image.get_rect(center=coords)
        self.mask = pygame.mask.from_surface(self.image)
        self.percievedx = coords[0]
        self.percievedy = coords[1]
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
            number = 0
        else:
            number = math.floor(self.speed*-1)
        self.image = self.imagelist[number]

        xy = findxy(self.direction)
        self.percievedx += xy[0]*self.speed
        self.percievedy += xy[1]*self.speed
        self.image = pygame.transform.rotate(self.image,self.direction)
        self.mask = pygame.mask.from_surface(self.image) # Recalculate the mask so that it adapts to the new direction that it is facing, otherwise the hit box will be very wrong.
        self.rect = self.image.get_rect(center=(globals.playerorigin))
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
