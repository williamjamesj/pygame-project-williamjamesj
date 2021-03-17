import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import Spaceship
import math
from obstacle import Barrier, Destroyable,Objective, SpawnPoint
def levelone():
    globals.spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(globals.spawnPointLocation,50,50)
    globals.playerspaceship = Spaceship(globals.spawnPointLocation,"yellowspaceship",10,0.1,0,3)
    globals.allobjects.add(globals.playerspaceship)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.allnonplayers.add(Barrier(500,300,50,600)) # Wall 1
    globals.allnonplayers.add(Barrier(200,100,50,600)) # Wall 2
    globals.allnonplayers.add(Barrier(-100,300,50,600)) # Wall 3
    globals.allnonplayers.add(Barrier(-400,100,50,600)) # Wall 4
    globals.allnonplayers.add(Barrier(-800,650,400,50)) # Wall 5
    globals.allnonplayers.add(Barrier(-1000,0,2000,100)) # Top
    globals.allnonplayers.add(Barrier(-1100,0,100,1000)) # Left
    globals.allnonplayers.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.allnonplayers.add(Barrier(1000,0,100,1000)) # Right
    globals.wincondition = Objective(-900,200,50,50)
def leveltwo():
    globals.spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(globals.spawnPointLocation,50,50)
    globals.playerspaceship = Spaceship(globals.spawnPointLocation,"yellowspaceship",10,0.1,0,3)
    globals.allobjects.add(globals.playerspaceship)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.allnonplayers.add(Barrier(500,300,50,600)) # Wall 1
    globals.destroyables.add(Destroyable(500,100,50,200)) # Wall 1 Destroyable
    globals.allnonplayers.add(Barrier(200,100,50,600)) # Wall 2
    globals.destroyables.add(Destroyable(200,700,50,200)) # Wall 2 Destroyable
    globals.allnonplayers.add(Barrier(-100,300,50,600)) # Wall 3
    globals.destroyables.add(Destroyable(-100,100,50,200)) # Wall 3 Destroyable
    globals.allnonplayers.add(Barrier(-400,100,50,600)) # Wall 4
    globals.destroyables.add(Destroyable(-400,700,50,200)) # Wall 4 Destroyable
    globals.allnonplayers.add(Barrier(-800,650,400,50)) # Wall 5
    globals.allnonplayers.add(Barrier(-1000,0,2000,100)) # Top
    globals.allnonplayers.add(Barrier(-1100,0,100,1000)) # Left
    globals.allnonplayers.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.allnonplayers.add(Barrier(1000,0,100,1000)) # Right
    globals.wincondition = Objective(-900,200,50,50)
def levelthree():
    print("level three")
def levelfour():
    print("level four")
def levelfive():
    print("level five")
def levelsix():
    print("level six")
def levelseven():
    print("level seven")
def leveleight():
    print("level eight")
def levelnine():
    print("level nine")
def playLevel(level):
    globals.level = level
    if level == 1:
        globals.gamestage = "game"
        levelone()
    elif level == 2 and globals.unlockedlevel>=2:
        globals.gamestage = "game"
        leveltwo()
    elif level == 3 and globals.unlockedlevel>=3:
        levelthree()
    elif level == 4 and globals.unlockedlevel>=4:
        levelfour()
    elif level == 5 and globals.unlockedlevel>=5:
        levelfive()
    elif level == 6 and globals.unlockedlevel>=6:
        levelsix()
    elif level == 7 and globals.unlockedlevel>=7:
        levelseven()
    elif level == 8 and globals.unlockedlevel>=8:
        leveleight()
    elif level == 9 and globals.unlockedlevel>=9:
        levelnine()
    else:
        globals.gamestage = "levelselect"