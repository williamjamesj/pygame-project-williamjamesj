import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class Barrier(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.x = x+globals.playerorigin[0]; self.y = y+globals.playerorigin[1]
        self.colour = (255,255,255)
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.x = self.x-globals.playerspaceship.percievedx
        self.rect.y = self.y-globals.playerspaceship.percievedy # The platform moves, the player stays stationary.
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return