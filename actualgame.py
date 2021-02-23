import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
from spaceship import Spaceship
def playGame(level):
    globals.gamestage = "game"
    globals.level = level
    print(level)
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship = Spaceship([500,500],"banana",10,2,2)
def updatePlayer(keys):
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1)