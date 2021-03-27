import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import PlayerSpaceship
import math
from obstacle import Barrier, Destroyable
from levels import *
from levels import playLevel
def playGame(level):
    globals.leveltimer = pygame.time.Clock()
    globals.leveltime = 0
    globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2
    globals.allobjects = pygame.sprite.Group()
    globals.walls = pygame.sprite.Group()
    globals.bullets = pygame.sprite.Group()
    globals.destroyables = pygame.sprite.Group()
    globals.enemySpaceships = pygame.sprite.Group()
    globals.enemyBullets = pygame.sprite.Group()
    globals.powerups = pygame.sprite.Group()
    playLevel(level)
    return
def updateGame(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    if keys[pygame.K_ESCAPE]==1:
        globals.gamestage = "levelselect"
    globals.playerspaceship.update(keys[pygame.K_UP]==1,keys[pygame.K_DOWN]==1,keys[pygame.K_LEFT]==1,keys[pygame.K_RIGHT]==1,keys[pygame.K_SPACE])
    globals.walls.update()
    globals.wincondition.update()
    globals.destroyables.update()
    globals.spawnPoint.update()
    globals.bullets.update()
    globals.enemySpaceships.update()
    globals.enemyBullets.update()
    globals.powerups.update()
    globals.wincondition.draw()
    globals.spawnPoint.draw()
    if globals.playerspaceship.shields > 1:
        globals.screen.blit(pygame.font.Font('resources/fonts/Roboto-Regular.ttf', 50).render(f"Shields: {globals.playerspaceship.shields}", True, (255,255,255)), (0,0))
    if globals.debug:
        font = pygame.font.Font('resources/fonts/Nougat.ttf', 50)
        textobject = font.render(f"Speed: {str(math.ceil(globals.playerspaceship.speed))}", True, (255,0,0))
        globals.screen.blit(textobject, (500,0))
        textobject = font.render(f"XY: {str(math.ceil(globals.playerspaceship.percievedx)),str(math.ceil(globals.playerspaceship.percievedy))} Timer: {math.floor(globals.leveltime/1000)}", True, (255,0,0))
        globals.screen.blit(textobject, (1000,0))
    if pygame.sprite.collide_mask(globals.playerspaceship,globals.wincondition) is not None:
        if len(globals.enemySpaceships)==0:
            globals.coinsgained = globals.level*1000-math.floor(globals.leveltime)/100*globals.level
            if globals.coinsgained<100:
                globals.coinsgained = 100
            globals.coins+=math.floor(globals.coinsgained)
            if globals.level==globals.unlockedlevel:
                globals.unlockedlevel+=1
            globals.gamestage = "levelover"
    pygame.sprite.groupcollide(globals.bullets,globals.destroyables,True,True) # Destroys any platforms that are shot and can be shot.
    pygame.sprite.groupcollide(globals.bullets,globals.walls,True,False) # Destroys any bullet that hits a platform.
    pygame.sprite.groupcollide(globals.enemyBullets,globals.walls,True,False) # Destroys any enemy's bullet that hits a platform.
    # Enemies can't destroy platforms or destroyables.
    for i in globals.powerups:
        if pygame.sprite.collide_mask(i,globals.playerspaceship) is not None:
            i.kill()
            globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate/10
            pygame.time.set_timer(USEREVENT + 2, 10000)
            globals.playerspaceship.canshoot = True
    for bullet in globals.bullets:
        for spaceship in globals.enemySpaceships:
            if pygame.sprite.collide_mask(bullet,spaceship) is not None:
                spaceship.kill()
                bullet.kill()
    listeronitony = [] # Everything that can kill the player.
    for i in globals.walls:
        listeronitony.append(i)
    for i in globals.destroyables:
        listeronitony.append(i)
    for i in globals.enemyBullets:
        listeronitony.append(i)
    for i in listeronitony: # Collision between obstacles and player.
        if pygame.sprite.collide_mask(globals.playerspaceship,i) is not None:
            if i in globals.enemyBullets or i in globals.destroyables:
                i.kill()
            globals.playerspaceship.shields -= 1
    if globals.playerspaceship.shields <= 0:
        globals.bullets.empty()
        globals.playerspaceship.speed = 0
        globals.playerspaceship.direction = 0
        globals.playerspaceship.canshoot = True
        globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate
        globals.leveltime = 0
        playGame(globals.level)
            
    return