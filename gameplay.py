import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import Spaceship
import math
from obstacle import Barrier
from levels import playLevel
def playGame(level):
    globals.leveltimer = pygame.time.Clock()
    globals.leveltime = 0
    globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2
    globals.allobjects = pygame.sprite.Group()
    globals.allnonplayers = pygame.sprite.Group()
    globals.gamestage = "game"
    globals.level = level
    playLevel(level)
    return
def updatePlayer(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    if keys[pygame.K_ESCAPE]==1:
        globals.gamestage = "levelselect"
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1,keys[pygame.K_LEFT]==1,keys[pygame.K_RIGHT]==1)
    globals.allnonplayers.update()
    globals.wincondition.update()
    globals.wincondition.draw()
    globals.spawnPoint.update()
    globals.spawnPoint.draw()
    collisions = []
    if globals.debug:
        font = pygame.font.Font('resources/fonts/Nougat.ttf', 50)
        textobject = font.render(f"Speed: {str(math.ceil(globals.playerspaceship.speed))}", True, (255,0,0))
        globals.screen.blit(textobject, (500,0))
        textobject = font.render(f"XY: {str(math.ceil(globals.playerspaceship.percievedx)),str(math.ceil(globals.playerspaceship.percievedy))} Timer: {math.floor(globals.leveltime/1000)}", True, (255,0,0))
        globals.screen.blit(textobject, (1000,0))
    if pygame.sprite.collide_mask(globals.playerspaceship,globals.wincondition) is not None:
        globals.coinsgained = globals.level*1000-math.floor(globals.leveltime)/100
        if globals.coinsgained<100:
            globals.coinsgained = 100
        globals.coins+=globals.coinsgained
        if globals.level==globals.unlockedlevel:
            globals.unlockedlevel+=1
        globals.gamestage = "levelover"
    for i in globals.allnonplayers:
        if pygame.sprite.collide_mask(globals.playerspaceship,i) is not None:
            globals.playerspaceship.percievedx = globals.spawnPointLocation[0]
            globals.playerspaceship.percievedy = globals.spawnPointLocation[1]
            globals.playerspaceship.speed = 0
            globals.playerspaceship.direction = 0
            globals.leveltime = 0
    return