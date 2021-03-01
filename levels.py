import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import Spaceship
import math
from obstacle import Barrier
def levelone():
    globals.playerspaceship = Spaceship([0,-500],"yellowspaceship",10,0.1,0,2)
    globals.allobjects.add(globals.playerspaceship)
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.allnonplayers.add(Barrier(0,0,1000,100)) # The one going left to right
    globals.allnonplayers.add(Barrier(-100,0,100,1000))
def playLevel(level):
    if level == 1:
        levelone()