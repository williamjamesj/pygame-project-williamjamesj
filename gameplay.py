import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
from spaceship import Spaceship
import math
def playGame(level):
    globals.allobjects = pygame.sprite.Group()
    globals.gamestage = "game"
    globals.level = level
    print(level)
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship = Spaceship([500,500],"banana",10,0.1,0,2)
    globals.allobjects.add(globals.playerspaceship)
    return
def updatePlayer(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1,keys[pygame.K_LEFT]==1,keys[pygame.K_RIGHT]==1)
    if globals.debug:
        font = pygame.font.Font('Nougat.ttf', 50)
        textobject = font.render(f"Speed: {str(math.ceil(globals.playerspaceship.speed))}", True, (255,0,0))
        globals.screen.blit(textobject, (500,0))
    return