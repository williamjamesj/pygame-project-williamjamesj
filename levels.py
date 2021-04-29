import random
import pygame
from pygame.locals import *
import globalvariables as globals
from spaceship import BossSpaceship, EnemySpaceship, PlayerSpaceship
import math
from obstacle import Barrier, Destroyable,Objective, SpawnPoint, powerUp
def spawnPlayer(spawnPointLocation):
        globals.playerspaceship = PlayerSpaceship(spawnPointLocation,globals.playercurrentship[0],globals.playercurrentship[1],globals.playercurrentship[2],0,globals.playercurrentship[3],globals.playercurrentship[6],firerate=globals.playercurrentship[4])
        globals.playerspaceship.firerate = globals.playercurrentship[4]
def levelone():
    spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.walls.add(Barrier(500,300,50,600)) # Wall 1
    globals.walls.add(Barrier(200,100,50,600)) # Wall 2
    globals.walls.add(Barrier(-100,300,50,600)) # Wall 3
    globals.walls.add(Barrier(-400,100,50,600)) # Wall 4
    globals.walls.add(Barrier(-800,650,450,50)) # Wall 5
    globals.walls.add(Barrier(-1000,0,2000,100)) # Top
    globals.walls.add(Barrier(-1100,0,100,1000)) # Left
    globals.walls.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.walls.add(Barrier(1000,0,100,1000)) # Right
    globals.wincondition = Objective(-900,200,50,50)
    return
def leveltwo():
    spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.walls.add(Barrier(500,300,50,600)) # Wall 1
    globals.destroyables.add(Destroyable(500,100,50,200)) # Wall 1 Destroyable
    globals.walls.add(Barrier(200,100,50,600)) # Wall 2
    globals.destroyables.add(Destroyable(200,700,50,200)) # Wall 2 Destroyable
    globals.walls.add(Barrier(-100,300,50,600)) # Wall 3
    globals.destroyables.add(Destroyable(-100,100,50,200)) # Wall 3 Destroyable
    globals.walls.add(Barrier(-400,100,50,600)) # Wall 4
    globals.destroyables.add(Destroyable(-400,700,50,200)) # Wall 4 Destroyable
    globals.walls.add(Barrier(-800,650,450,50)) # Wall 5
    globals.walls.add(Barrier(-1000,0,2000,100)) # Top
    globals.walls.add(Barrier(-1100,0,100,1000)) # Left
    globals.walls.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.walls.add(Barrier(1000,0,100,1000)) # Right
    globals.wincondition = Objective(-900,200,50,50)
    return
def levelthree():
    spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.walls.add(Barrier(-1000,0,2000,100)) # Top
    globals.walls.add(Barrier(-1100,0,100,1000)) # Left
    globals.walls.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.walls.add(Barrier(1000,0,100,1000)) # Right
    globals.walls.add(Barrier(650,300,50,400)) # Barrier
    globals.enemySpaceships.add(EnemySpaceship((0,400),"greenspaceship",10,0.1,0,0,100,450))
    globals.enemySpaceships.add(EnemySpaceship((0,600),"greenspaceship",10,0.1,0,0,100,450))
    globals.powerups.add(powerUp(800,200,50,50))
    globals.wincondition = Objective(-900,200,50,50)
    return
def levelfour():
    spawnPointLocation = (800,325)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.playerspaceship.direction = 90
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    # Walls
    globals.walls.add(Barrier(-1000,-100,2000,100)) # Top
    globals.walls.add(Barrier(-1100,-100,100,900)) # Left
    globals.walls.add(Barrier(-1000,700,2000,100)) # Bottom
    globals.walls.add(Barrier(1000,-100,100,900)) # Right
    globals.walls.add(Barrier(550,200,450,20)) # Spawn Protection Top
    globals.walls.add(Barrier(550,400,450,20)) # Spawn Protection Bottom
    globals.walls.add(Barrier(-400,200,20,200)) # Final Obstacle
    # Destroyables
    globals.destroyables.add(Destroyable(350,200,200,20)) # 1 Top
    globals.destroyables.add(Destroyable(350,400,200,20)) # 1 Bottom
    globals.destroyables.add(Destroyable(0,200,200,20)) # 2 Top
    globals.destroyables.add(Destroyable(0,400,200,20)) # 2 Bottom
    globals.destroyables.add(Destroyable(-350,200,200,20)) # 3 Top
    globals.destroyables.add(Destroyable(-350,400,200,20)) # 3 Bottom
    # Enemies
    globals.optionalEnemySpaceships.add(EnemySpaceship([450,100],"orangespaceship",0,0,0,0,100)) # 1 Top
    globals.optionalEnemySpaceships.add(EnemySpaceship([450,500],"orangespaceship",0,0,0,0,100)) # 1 Bottom
    globals.optionalEnemySpaceships.add(EnemySpaceship([100,100],"orangespaceship",0,0,0,0,100)) # 2 Top
    globals.optionalEnemySpaceships.add(EnemySpaceship([100,500],"orangespaceship",0,0,0,0,100)) # 2 Bottom
    globals.optionalEnemySpaceships.add(EnemySpaceship([-250,100],"orangespaceship",0,0,0,0,100)) # 3 Top
    globals.optionalEnemySpaceships.add(EnemySpaceship([-250,500],"orangespaceship",0,0,0,0,100)) # 3 Bottom
    globals.wincondition = Objective(-900,300,50,50)
    return
def levelfive():
    spawnPointLocation = (800,500)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.screen.blit(globals.backgroundpicture, (0,0)) 
    globals.walls.add(Barrier(500,300,50,600)) # Wall 1
    globals.destroyables.add(Destroyable(500,100,50,200)) # Wall 1 Destroyable
    globals.enemySpaceships.add(EnemySpaceship([400,800],"greenspaceship",0,0,0,0,200)) # Section 1 Enemy
    globals.walls.add(Barrier(200,100,50,600)) # Wall 2
    globals.destroyables.add(Destroyable(200,700,50,200)) # Wall 2 Destroyable
    globals.enemySpaceships.add(EnemySpaceship([50,200],"greenspaceship",0,0,0,0,175)) # Section 2 Enemy
    globals.walls.add(Barrier(-100,300,50,600)) # Wall 3
    globals.destroyables.add(Destroyable(-100,100,50,200)) # Wall 3 Destroyable
    globals.enemySpaceships.add(EnemySpaceship([-250,800],"greenspaceship",0,0,0,0,125)) # Section 3 Enemy
    globals.walls.add(Barrier(-400,100,50,600)) # Wall 4
    globals.destroyables.add(Destroyable(-400,700,50,200)) # Wall 4 Destroyable
    globals.enemySpaceships.add(EnemySpaceship([-900,600],"greenspaceship",0,0,0,0,75)) # Final Enemy
    globals.walls.add(Barrier(-800,650,450,50)) # Wall 5
    globals.walls.add(Barrier(-1000,0,2000,100)) # Top
    globals.walls.add(Barrier(-1100,0,100,1000)) # Left
    globals.walls.add(Barrier(-1000,900,2000,100)) # Bottom
    globals.walls.add(Barrier(1000,0,100,1000)) # Right
    globals.wincondition = Objective(-900,200,50,50)
    return
def levelsix():
    spawnPointLocation = (0,0)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.wincondition = Objective(-2000,150,50,50)
    globals.walls.add(Barrier(-900,-600,1000,50)) # Top Tunnel Top Wall
    globals.walls.add(Barrier(-900,-600,50,300)) # Left Tunnel Top Wall
    globals.walls.add(Barrier(-600,-350,500,50))  # Top Tunnel Bottom Wall
    globals.walls.add(Barrier(-150,-350,50,1050)) # Left Initial Tunnel Wall
    globals.walls.add(Barrier(100,-600,50,900)) # Right Initial Tunnel Wall
    globals.walls.add(Barrier(-150,300,300,50)) # Bottom Initial Tunnel Wall
    globals.walls.add(Barrier(-2250,650,2100,50)) # Bottom Box Wall
    globals.walls.add(Barrier(-2250,-350,1350,50)) # Top Box Wall
    globals.walls.add(Barrier(-2250,-350,50,1050)) # Right Box Wall
    globals.destroyables.add(Destroyable(-850,-350,250,50)) # Destroyable Segment
    globals.powerups.add(powerUp(-750,-500,50,50)) # Rapid Fire Power Up
    globals.powerups.add(powerUp(-750,150,50,50)) # Rapid Fire Power Up
    globals.walls.add(Barrier(-900,-150,50,200)) # Barrier 1
    globals.walls.add(Barrier(-900,300,50,200)) # Barrier 2
    # Enemies
    globals.enemySpaceships.add(EnemySpaceship([-1200,-50],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1200,400],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1350,0],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1350,350],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1500,50],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1500,300],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1650,100],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1650,250],"greenspaceship",0,0,0,0,150))
    globals.enemySpaceships.add(EnemySpaceship([-1800,175],"greenspaceship",0,0,0,0,20))
    return
def levelseven():
    spawnPointLocation = (0,0)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.playerspaceship.direction = 90
    globals.wincondition = Objective(-2100,1000,50,50)
    globals.optionalEnemySpaceships.add(EnemySpaceship([0,500],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([0,-500],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([500,0],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([-500,0],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([500,500],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([-500,500],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([500,-500],"orangespaceship",10,0.1,0,0,100))
    globals.optionalEnemySpaceships.add(EnemySpaceship([-500,-500],"orangespaceship",10,0.1,0,0,100))
    globals.walls.add(Barrier(-600,600,1200,50))
    globals.walls.add(Barrier(-600,-600,1200,50))
    globals.walls.add(Barrier(600,-600,50,1250))
    globals.walls.add(Barrier(-600,-600,50,500))
    globals.walls.add(Barrier(-600,150,50,1050))
    globals.destroyables.add(Destroyable(-600,-100,50,250))
    globals.walls.add(Barrier(-2250,-150,1650,50))
    globals.walls.add(Barrier(-2250,-150,50,1350))
    globals.walls.add(Barrier(-2250,1200,1700,50))
    return
def leveleight():
    spawnPointLocation = (-500,0)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.playerspaceship.direction = 90
    globals.walls.add(Barrier(-7800,-500,8000,50))
    globals.walls.add(Barrier(-7800,500,8000,50))
    globals.walls.add(Barrier(200,-500,50,1050))
    globals.walls.add(Barrier(-7850,-500,50,1050))
    globals.wincondition = Objective(-7500,0,50,50)
    globals.powerups.add(powerUp(-800,0,50,50))
    for i in range(-400,400):
        if random.randint(0,150) == 0:
            globals.enemySpaceships.add(EnemySpaceship([100,i],"greenspaceship",10,0.1,0,0,100,brakingdistance=300))
    for i in range(-400,400):
        if random.randint(0,300) == 0:
            globals.optionalEnemySpaceships.add(EnemySpaceship([-7500,i],"orangespaceship",10,0.1,0,0,100,brakingdistance=300))
    for i in range(1000,7000):
        if i%100 ==0:
            globals.destroyables.add(Destroyable(i*-1,-450,25,950))
    return
def levelnine():
    spawnPointLocation = (0,0)
    globals.spawnPoint = SpawnPoint(spawnPointLocation,50,50)
    spawnPlayer(spawnPointLocation)
    globals.playerspaceship.direction = 270
    globals.wincondition = Objective(-854205,769865,50,50) # Good luck finding that one. Instead, the level is complete upon the death of the boss.
    globals.boss = BossSpaceship([1500,500],"bigboy",0,0,0,0,20,shield=50)
    globals.powerups.add(powerUp(500,0,50,50))
    globals.powerups.add(powerUp(600,700,50,50))
    globals.walls.add(Barrier(-300,-200,2300,50))
    globals.walls.add(Barrier(-300,200,800,50))
    globals.walls.add(Barrier(-300,-200,50,400))
    globals.walls.add(Barrier(500,200,50,1000))
    globals.walls.add(Barrier(500,1200,1500,50))
    globals.walls.add(Barrier(2000,-200,50,1450))
    globals.walls.add(Barrier(800,500,75,400))
    return
def playLevel(level):
    globals.level = level
    if level == 1:
        globals.gamestage = "game"
        levelone()
    elif level == 2 and globals.unlockedlevel>=2:
        globals.gamestage = "game"
        leveltwo()
    elif level == 3 and globals.unlockedlevel>=3:
        globals.gamestage = "game"
        levelthree()
    elif level == 4 and globals.unlockedlevel>=4:
        globals.gamestage = "game"
        levelfour()
    elif level == 5 and globals.unlockedlevel>=5:
        globals.gamestage = "game"
        levelfive()
    elif level == 6 and globals.unlockedlevel>=6:
        globals.gamestage = "game"
        levelsix()
    elif level == 7 and globals.unlockedlevel>=7:
        globals.gamestage = "game"
        levelseven()
    elif level == 8 and globals.unlockedlevel>=8:
        globals.gamestage = "game"
        leveleight()
    elif level == 9 and globals.unlockedlevel>=9:
        globals.gamestage = "game"
        levelnine()
    else:
        globals.gamestage = "levelselect"
    return