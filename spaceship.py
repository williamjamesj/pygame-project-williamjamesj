import pygame
from pygame.locals import *
import globalvariables as globals
import math
import os
from bullet import Bullet
import random
def findxy(direction):
        x = math.sin(math.radians(direction)) # Trigonometry.
        y = math.cos(math.radians(direction)) # Thank you Stack Overflow!: https://stackoverflow.com/questions/5346874/pygame-making-a-sprite-move-in-the-direction-it-is-facing.
        return [x,y]
def findDirection(xy):
    return(math.degrees(math.atan2(xy[0],xy[1])))
def findImages(directory):
    fileslist = []
    filenames = []
    for i in os.listdir(directory):
        filenames.append(i)
    filenames.sort()
    for i in filenames:
        fileslist.append(pygame.image.load(os.path.join(directory,i)).convert_alpha())
    return fileslist
class PlayerSpaceship(pygame.sprite.Sprite):
    def __init__(self,coords,appearance,maxspeed, acceleration, direction, turnspeed, firerate=1):
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
        self.canshoot = True
        self.firerate = firerate
        return
    def update(self,doThrust,doSlow,left,right,doshoot):
        if doThrust:
            self.speed -= self.acceleration # Going forwards (what we think is forwards) is actually going backwards in this code, so we just "slow down" to speed up and vice versa 
        if doSlow:
            self.speed += self.acceleration
        if left:
            self.direction += self.turnspeed
        if right:
            self.direction -= self.turnspeed
        if doshoot and self.canshoot:
            globals.bullets.add(Bullet(globals.playerorigin[0]+self.percievedx,globals.playerorigin[1]+self.percievedy, self.direction, 20))
            pygame.time.set_timer(USEREVENT + 1, self.firerate*1000)
            self.canshoot = False
        if self.speed > 0: # Stops the spaceship from going in reverse, because the idea of a spaceship reversing makes me uncomfortable.
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
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        return
class EnemySpaceship(PlayerSpaceship):
    def __init__(self, coords, appearance, maxspeed, acceleration, direction, turnspeed, firerate):
        super().__init__(coords, appearance, maxspeed, acceleration, direction, turnspeed, firerate=firerate)
        self.x = coords[0]
        self.y = coords[1]
        return
    def update(self):
        distancetoplayer = math.sqrt((self.x-globals.playerspaceship.percievedx)**2+(self.y-globals.playerspaceship.percievedy)**2)
        print(findDirection([self.x-globals.playerspaceship.percievedx,self.y-globals.playerspaceship.percievedy]))
        self.direction = findDirection([self.x-globals.playerspaceship.percievedx,self.y-globals.playerspaceship.percievedy])
        self.image = self.imagelist[0]
        self.image = pygame.transform.rotate(self.image,self.direction)
        self.rect = self.image.get_rect(center=(self.x-globals.playerspaceship.percievedx+globals.playerorigin[0],self.y-globals.playerspaceship.percievedy+globals.playerorigin[1]))
        if random.randint(0,50) == 5:
            globals.enemyBullets.add(Bullet(globals.playerorigin[0]+self.percievedx,globals.playerorigin[1]+self.percievedy, self.direction, 20))
    def draw(self,screen):
        super().draw(self,screen)
