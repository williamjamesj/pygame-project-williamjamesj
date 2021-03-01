import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import Spaceship
import math
from obstacle import Barrier
from levels import playLevel
def playGame(level):
    globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2
    globals.allobjects = pygame.sprite.Group()
    globals.allnonplayers = pygame.sprite.Group()
    globals.gamestage = "game"
    globals.level = level
    playLevel(level)
    return
def updatePlayer(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1,keys[pygame.K_LEFT]==1,keys[pygame.K_RIGHT]==1)
    globals.allnonplayers.update()
    if globals.debug:
        font = pygame.font.Font('Nougat.ttf', 50)
        textobject = font.render(f"Speed: {str(math.ceil(globals.playerspaceship.speed))}", True, (255,0,0))
        globals.screen.blit(textobject, (500,0))
    for i in globals.allnonplayers:
        collisions = pygame.sprite.collide_mask(globals.playerspaceship,i)
    if collisions:
        print("collid")
    else:
        print("not collid")
    return