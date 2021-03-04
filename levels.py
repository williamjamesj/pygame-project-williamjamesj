import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import Spaceship
import math
from obstacle import Barrier,Objective
def levelone():
    globals.playerspaceship = Spaceship([800,500],"yellowspaceship",10,0.1,0,2)
    globals.allobjects.add(globals.playerspaceship)
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.allnonplayers.add(Barrier(-1000,0,2000,100)) # Top
    globals.allnonplayers.add(Barrier(-1100,0,100,1000)) # Left
    globals.allnonplayers.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.allnonplayers.add(Barrier(1000,0,100,1000)) # Right
    globals.allnonplayers.add(Barrier(500,250,50,650))
    globals.wincondition = (Objective(-900,200,50,50))
def playLevel(level):
    if level == 1:
        levelone()