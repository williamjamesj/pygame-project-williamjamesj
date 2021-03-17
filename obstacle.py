import pygame
from pygame.locals import *
import globalvariables as globals
class Barrier(pygame.sprite.Sprite):
    '''Draws an obstacle'''
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
        return
    def update(self):
        self.rect.x = self.x-globals.playerspaceship.percievedx
        self.rect.y = self.y-globals.playerspaceship.percievedy # The platform moves, the player stays stationary, so that the screen can scroll
        self.image.fill(self.colour)
        return
    def draw(self):
        globals.screen.blit(self.image,(self.rect.x,self.rect.y))
        return
class Objective(Barrier):
    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)
        self.colour = (255,255,0)
        return
class SpawnPoint(Barrier):
    def __init__(self,coords,width,height):
        self.x, self.y = coords
        super().__init__(self.x,self.y,width,height)
        self.colour = (0,255,0)
        self.rect.centerx, self.rect.centery = coords
        return
    def update(self):
        self.rect.centerx = self.x-globals.playerspaceship.percievedx
        self.rect.centery = self.y-globals.playerspaceship.percievedy # The platform moves, the player stays stationary, so that the screen can scroll
        self.image.fill(self.colour)
        return
class Destroyable(Barrier):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.colour = (255,0,0)
        return