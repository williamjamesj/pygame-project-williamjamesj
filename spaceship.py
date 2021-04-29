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
    def __init__(self,coords,appearance,maxspeed, acceleration, direction, turnspeed, shields, firerate=1):
        super().__init__() # Very important
        self.appearance = appearance
        self.imagelist = findImages(f"resources/spaceships/{str(appearance)}/")
        self.maxspeed = int(maxspeed)
        self.acceleration = float(acceleration)
        self.direction = direction
        self.turnspeed = float(turnspeed)
        self.speed = 0
        self.image = pygame.transform.rotate(self.imagelist[0],direction)
        self.rect = self.image.get_rect(center=coords)
        self.mask = pygame.mask.from_surface(self.image)
        self.percievedx = coords[0]
        self.percievedy = coords[1]
        self.canshoot = True
        self.originalfirerate = float(firerate)
        self.firerate = float(firerate)
        self.shields = int(shields)
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
            globals.bullets.add(Bullet(globals.playerorigin[0]+self.percievedx,globals.playerorigin[1]+self.percievedy, self.direction, 35))
            pygame.time.set_timer(USEREVENT + 1, int(self.firerate*1000))
            globals.audioHandler.playSound('laser')
            self.canshoot = False
        if self.speed > 0: # Stops the spaceship from going in reverse, because thats just not going to happen.
            self.speed = 0
        if self.speed < self.maxspeed*-1:
            self.speed = self.maxspeed*-1
        # Finds which stage of the Animation the ship should show
        if math.floor(self.speed*-1) <= 0:
            number = 0
        else:
            number = math.floor(self.speed*-1)
        if number>len(self.imagelist)-1: # In case the ship goes faster than there are animation frames.
            self.image = self.imagelist[-1] 
        else:
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
    def __init__(self, coords, appearance, maxspeed, acceleration, direction, turnspeed, firerate,brakingdistance=200,shield=0):
        super().__init__(coords, appearance, maxspeed, acceleration, direction, turnspeed, firerate)
        self.shield = shield
        self.firerate = firerate
        self.x = coords[0]
        self.y = coords[1]
        self.brakingdistance = brakingdistance
        return
    def update(self): # Overrides the player 
        distancetoplayer = math.sqrt((self.x-globals.playerspaceship.percievedx)**2+(self.y-globals.playerspaceship.percievedy)**2) # This *could* be useful some day. Thanks past Will, this is rather helpful!
        self.direction = findDirection([self.x-globals.playerspaceship.percievedx,self.y-globals.playerspaceship.percievedy])
        self.image = self.imagelist[0] # Only show the first animation, as the ship is stationary.
        self.image = pygame.transform.rotate(self.image,self.direction)
        self.rect = self.image.get_rect(center=(self.x-globals.playerspaceship.percievedx+globals.playerorigin[0],self.y-globals.playerspaceship.percievedy+globals.playerorigin[1]))
        self.mask = pygame.mask.from_surface(self.image)
        if random.randint(0,self.firerate) == 0: # Means there is a 1 in *firerate* chance of firing
            globals.enemyBullets.add(Bullet(globals.playerorigin[0]+self.x,globals.playerorigin[1]+self.y, self.direction+random.randint(-10,10), 35))
            globals.audioHandler.playSound('laser')
        # Movement Code - Enemies will fly toward the player, coming to a full stop once they're 200 units (?) from the player.
        if self.maxspeed != 0 and self.acceleration != 0:
            canAccelerate = self.speed <= self.maxspeed
            canDeccelerate = self.speed >= 0
            shouldStop = distancetoplayer<self.brakingdistance
            if canAccelerate and not shouldStop:
                self.speed += self.acceleration
            elif canDeccelerate:
                self.speed -= 1
            if shouldStop and self.speed < 1:
                self.speed = 0
            x,y = findxy(self.direction)
            self.x+=x*self.speed*-1
            self.y+=y*self.speed*-1
        return
    def draw(self,screen):
        super().draw(self,screen) # Uses the existing draw function.
        return
class DummySpaceship(PlayerSpaceship):
    def __init__(self):
        super().__init__([0,0], "yellowspaceship", 0, 0, 0, 0, 0)
        self.x = 0
        self.y = 0
        return
    def update(self):
        self.image = self.imagelist[0]
        self.image = pygame.transform.rotate(self.image,int(self.direction))
        self.rect = self.image.get_rect(center=(int(self.x)-math.floor(globals.playerspaceship.percievedx)+globals.playerorigin[0],int(self.y)-math.floor(globals.playerspaceship.percievedy)+globals.playerorigin[1]))
        return
