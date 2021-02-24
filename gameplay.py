import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
from spaceship import Spaceship
def playGame(level):
    globals.allobjects = pygame.sprite.Group()
    globals.gamestage = "game"
    globals.level = level
    print(level)
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship = Spaceship([500,500],"banana",50,0.1,0)
    globals.allobjects.add(globals.playerspaceship)
    return
def updatePlayer(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1,keys[pygame.K_LEFT]==1,keys[pygame.K_RIGHT]==1)
    return