import pygame
from pygame.locals import *
import globalvariables as globals
import math
def findxy(direction):
        x = math.sin(math.radians(direction)) # Trigonometry.
        y = math.cos(math.radians(direction)) # Thank you Stack Overflow: https://stackoverflow.com/questions/5346874/pygame-making-a-sprite-move-in-the-direction-it-is-facing.
        return [x,y]
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed):
        super().__init__()
        self.direction = direction
        self.x = x; self.y = y
        self.originalimage = pygame.image.load("resources/laser.png")
        self.speed = speed
        self.rect = self.originalimage.get_rect(center=(x,y))
        self.mask = pygame.mask.from_surface(self.originalimage)
        self.image = pygame.transform.rotate(self.originalimage,self.direction)
        return
    def update(self):
        x,y = findxy(self.direction)
        self.x += x*-1*self.speed
        self.y += y*-1*self.speed
        self.rect = self.image.get_rect(center=(self.x-globals.playerspaceship.percievedx,self.y-globals.playerspaceship.percievedy))
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
