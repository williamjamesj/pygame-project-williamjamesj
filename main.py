from shop import displayShop, updateShop
import pygame
from pygame.locals import *
from menu import checkingLevelOver, checkingSettings, displayLevelOver, displayMenu, checkingMenu, displaySettings, levelSelector, checkingLevel, displayInstructions, checkingInstructions
import globalvariables as globals
from gameplay import updateGame
import os, sys
import math
import localisation
from persistantdata import load,save
# Sets the language to whatever is stored in resources/localisation/lastlang and reads that language to globals.languagesdict
localisation.readlang()
localisation.readtexts()
# Defaults to Fullscreen Resolution 
pygame.display.set_caption('Cosmoracer')
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
globals.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN|pygame.NOFRAME) # Both of these options ensure compatibility across systems.
# globals.screen = pygame.display.set_mode((1024,768))
# Retrieves the size of the fullscreen window, important for properly positioning things on the screen
info = pygame.display.Info()
globals.dimensions = [info.current_w, info.current_h] # Dimensions of the screen
# Saves the current stage in the game
pygame.init() # initializes all of the pygame functionality including fonts
FPS = 60
fpsClock = pygame.time.Clock()
menurendered = False
levelrendered = False
instructionsrendered = False
settingsrendered = False
levelOverRendered = False
globals.backgroundpicture = pygame.image.load("resources/background.jpg")
globals.coins,globals.unlockedlevel = load()
while globals.running: # The main loop can be stopped from any file
    '''Main Loop - Always running, until the game stops.'''
    for event in pygame.event.get():
        if event.type == QUIT:
            globals.running = False
        # Checks if any buttons have been pressed in the menu stage.
        elif (globals.gamestage == "menu" and event.type == MOUSEBUTTONDOWN):
            checkingMenu(pygame.mouse.get_pos())
        elif (globals.gamestage == "levelselect" and event.type == MOUSEBUTTONDOWN):
            checkingLevel(pygame.mouse.get_pos())
        elif (globals.gamestage == "instructions" and event.type == MOUSEBUTTONDOWN):
            checkingInstructions(pygame.mouse.get_pos())
        elif (globals.gamestage == "settings" and event.type == MOUSEBUTTONDOWN):
            checkingSettings(pygame.mouse.get_pos())
        elif (globals.gamestage == "levelover" and event.type == MOUSEBUTTONDOWN):
            checkingLevelOver(pygame.mouse.get_pos())
        elif (globals.gamestage == "shop" and event.type == MOUSEBUTTONDOWN):
            updateShop(pygame.mouse.get_pos())
        elif event.type == USEREVENT + 1 and globals.gamestage == "game":
            globals.playerspaceship.canshoot = True
    if globals.gamestage == "game": # Loops while the player is playing the game, at the top of the elif list because it should be prioritised.
        updateGame(pygame.key.get_pressed())
        globals.playerspaceship.draw(globals.screen)
        globals.walls.draw(globals.screen)
        globals.bullets.draw(globals.screen)
        globals.destroyables.draw(globals.screen)
        globals.enemySpaceships.draw(globals.screen)
        globals.enemyBullets.draw(globals.screen)
        menurendered = True
        levelrendered = False
        globals.leveltimer.tick()
        globals.leveltime += globals.leveltimer.get_time()
    elif globals.gamestage =="menu" and not menurendered: # Loops while the player is in menu.
        displayMenu()
        menurendered = True # Means that the menu will only be drawn once so that the performance isn't being impeded by redrawing the background.
        levelrendered = False
        settingsrendered = False
    elif globals.gamestage == "levelselect" and not levelrendered:
        levelSelector()
        levelrendered = True
        levelOverRendered = False
    elif globals.gamestage == "instructions" and not instructionsrendered:
        displayInstructions()
        levelrendered = True
        menurendered = False
    elif globals.gamestage == "settings" and not instructionsrendered:
        displaySettings()
        levelrendered = True
        menurendered = False
    elif globals.gamestage == "levelover" and not levelOverRendered:
        displayLevelOver()
        levelOverRendered = True
        menurendered = False
        levelrendered = False
        instructionsrendered = False
    elif globals.gamestage == "shop":
        displayShop()
        levelOverRendered = False
        menurendered = False
        levelrendered = False
        instructionsrendered = False
    else:
        if not globals.gamestage == "menu":
            menurendered = False
        elif not globals.gamestage == "levelselect":
            levelrendered = False
        elif not globals.gamestage == "instructions":
            instructionsrendered = False
    if globals.debug:
        font = pygame.font.Font('resources/fonts/Nougat.ttf', 50)
        textobject = font.render(str(math.ceil(fpsClock.get_fps())), True, (255,0,0))
        globals.screen.blit(textobject, (0,0))
    pygame.display.flip()
    fpsClock.tick(FPS)
save(globals.coins,globals.unlockedlevel)