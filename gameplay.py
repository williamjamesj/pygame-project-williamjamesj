import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import PlayerSpaceship
import math
from obstacle import Barrier, Destroyable
from levels import *
from levels import playLevel
def playGame(level):
    globals.leveltime = 0 # Starts the counter of how long the player has taken to complete the level.
    globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2 # The player will always be displayed in the exact center of the screen.
    # Initialize all of the sprite groups.
    globals.allobjects = pygame.sprite.Group()
    globals.walls = pygame.sprite.Group()
    globals.bullets = pygame.sprite.Group()
    globals.destroyables = pygame.sprite.Group()
    globals.enemySpaceships = pygame.sprite.Group()
    globals.optionalEnemySpaceships = pygame.sprite.Group()
    globals.enemyBullets = pygame.sprite.Group()
    globals.powerups = pygame.sprite.Group()
    playLevel(level)
    globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate
    return
def updateGame(keys):
    globals.screen.blit(globals.backgroundpicture, (0,0))
    if keys[pygame.K_ESCAPE]==1:
        globals.gamestage = "levelselect"
    globals.playerspaceship.update(keys[pygame.K_UP]==1 or keys[pygame.K_w],keys[pygame.K_DOWN]==1 or keys[pygame.K_s],keys[pygame.K_LEFT]==1 or keys[pygame.K_a],keys[pygame.K_RIGHT] or keys[pygame.K_d]==1,keys[pygame.K_SPACE] or keys[pygame.K_TAB])
    '''Update and draw EVERYTHING'''
    globals.walls.update()
    globals.wincondition.update()
    globals.destroyables.update()
    globals.spawnPoint.update()
    globals.bullets.update()
    globals.enemySpaceships.update()
    globals.optionalEnemySpaceships.update()
    globals.enemyBullets.update()
    globals.powerups.update()
    globals.wincondition.draw()
    globals.spawnPoint.draw()
    globals.playerspaceship.draw(globals.screen)
    globals.walls.draw(globals.screen)
    globals.bullets.draw(globals.screen)
    globals.destroyables.draw(globals.screen)
    globals.enemySpaceships.draw(globals.screen)
    globals.optionalEnemySpaceships.draw(globals.screen)
    globals.enemyBullets.draw(globals.screen)
    globals.powerups.draw(globals.screen)
    if globals.debug: # Show speed, position and timer for debug purposes. 
        font = pygame.font.Font('resources/fonts/Nougat.ttf', 50)
        textobject = font.render(f"Speed: {str(math.ceil(globals.playerspaceship.speed))}", True, (255,0,0))
        globals.screen.blit(textobject, (500,0))
        textobject = font.render(f"XY: {str(math.ceil(globals.playerspaceship.percievedx)),str(math.ceil(globals.playerspaceship.percievedy))} Timer: {math.floor(globals.leveltime/1000)}", True, (255,0,0))
        globals.screen.blit(textobject, (1000,0))
    if pygame.sprite.collide_mask(globals.playerspaceship,globals.wincondition) is not None:
        if len(globals.enemySpaceships)==0:
            globals.coinsgained = globals.level*1000-math.floor(globals.leveltime)/100*globals.level # Calculates the coins gained from the level.
            if globals.coinsgained<100: # Stops the player from recieving less than 100 coins, so that there is no chance of getting negative coins.
                globals.coinsgained = 100
            globals.coins+=math.floor(globals.coinsgained)
            if globals.level==globals.unlockedlevel:
                globals.unlockedlevel+=1 # Unlocks the next level.
            globals.gamestage = "levelover"
    """Wall/Destroyable - Bullet Collision Checking"""
    for wall in globals.walls:
        for bullet in globals.bullets:
            if pygame.sprite.collide_mask(wall,bullet) is not None:
                bullet.kill()
        for enemyBullet in globals.enemyBullets:
            if pygame.sprite.collide_mask(wall,enemyBullet) is not None:
                enemyBullet.kill()
    for destroyable in globals.destroyables:
        for bullet in globals.bullets:
            if pygame.sprite.collide_mask(destroyable,bullet) is not None:
                bullet.kill()
                destroyable.kill()
        for enemyBullet in globals.enemyBullets:
            if pygame.sprite.collide_mask(destroyable,enemyBullet) is not None:
                enemyBullet.kill()
                destroyable.kill()
    for i in globals.powerups: # Check if the player has recieved a powerup
        if pygame.sprite.collide_mask(i,globals.playerspaceship) is not None:
            i.kill()
            globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate/10
            pygame.time.set_timer(USEREVENT + 2, 10000)
            globals.playerspaceship.canshoot = True
    enemies = [] # A list of all enemies that can be shot.
    for i in globals.optionalEnemySpaceships:
        enemies.append(i)
    for i in globals.enemySpaceships:
        enemies.append(i)
    for bullet in globals.bullets:
        for spaceship in enemies:
            if pygame.sprite.collide_mask(bullet,spaceship) is not None:
                spaceship.kill() # Destroy both the bullet and the spaceship that it hit.
                bullet.kill()
                globals.audioHandler.playSound('explosion')
    walls = []
    for i in globals.walls:
        walls.append(i)
    for enemy in enemies:
        for wall in walls:
            if pygame.sprite.collide_mask(wall,enemy) is not None:
                enemy.kill()
                globals.audioHandler.playSound('explosion')
    listeronitony = [] # Everything that can kill the player.
    for i in globals.walls: # These for loops go and identify everything that will destroy the player's ship on collision. 
        listeronitony.append(i)
    for i in globals.destroyables:
        listeronitony.append(i)
    for i in globals.enemyBullets:
        listeronitony.append(i)
    for i in listeronitony: # Collision between obstacles and player.
        if pygame.sprite.collide_mask(globals.playerspaceship,i) is not None:
            if i in globals.enemyBullets or i in globals.destroyables: # Make sure the bullet is destroyed, so that the bullets don't infinitely damage.
                i.kill()
            globals.playerspaceship.shields -= 1
    if globals.playerspaceship.shields <= 0: # Only destroy the spaceship if it has reached 0 shields.
        globals.audioHandler.playSound('explosion') 
        globals.bullets.empty()
        globals.playerspaceship.speed = 0
        globals.playerspaceship.direction = 0
        globals.playerspaceship.canshoot = True
        globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate
        globals.leveltime = 0
        playGame(globals.level)
    if globals.playerspaceship.shields > 1:
        globals.screen.blit(pygame.font.Font('resources/fonts/Roboto-Regular.ttf', 50).render(f"Shields: {globals.playerspaceship.shields}", True, (255,0,0)), (0,0))
    return