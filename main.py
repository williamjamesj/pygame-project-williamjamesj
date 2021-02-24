import pygame
from pygame.locals import *
from menu import displayMenu, checkingMenu, levelSelector, checkingLevel
import globalvariables as globals
from gameplay import updatePlayer
import os, sys
import math
# Defaults to Fullscreen Resolution
globals.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# Retrieves the size of the fullscreen window, important for properly positioning things on the screen
info = pygame.display.Info()
globals.dimensions = [info.current_w, info.current_h] # Dimensions of the screen
# Saves the current stage in the game
pygame.display.set_caption('My Space Game')
pygame.init() # initializes all of the pygame functionality including fonts
FPS = 60
fpsClock = pygame.time.Clock()
menurendered = False
levelrendered = False
globals.backgroundpicture = pygame.image.load("background.jpg")
while globals.running: # The main loop can be stopped from any file
    '''Main Loop - Always running'''
    for event in pygame.event.get():
        if event.type == QUIT:
            globals.running = False
        # Checks if any buttons have been pressed in the menu stage.
        elif (globals.gamestage == "menu" and event.type == MOUSEBUTTONDOWN):
            checkingMenu(pygame.mouse.get_pos())
        elif (globals.gamestage == "levelselect" and event.type == MOUSEBUTTONDOWN):
            checkingLevel(pygame.mouse.get_pos())
    if globals.gamestage == "game": # Loops while the player is playing the game, at the top of the elif list because it is the most performance hungry.
        updatePlayer(pygame.key.get_pressed())
        globals.allobjects.draw(globals.screen)
    elif globals.gamestage =="menu" and not menurendered: # Loops while the player is in menu.
        displayMenu()
        menurendered = True # Means that the menu will only be drawn once so that the performance isn't being impeded by redrawing the background.
        levelrendered = False
    elif globals.gamestage == "levelselect" and not levelrendered:
        levelSelector()
        levelrendered = True
    else:
        if not globals.gamestage == "menu":
            menurendered = False
        elif not globals.gamestage == "levelselect":
            levelrendered = False
    if globals.debug:
        font = pygame.font.Font('Nougat.ttf', 50)
        textobject = font.render(str(math.ceil(fpsClock.get_fps())), True, (255,0,0))
        globals.screen.blit(textobject, (0,0))
    pygame.display.flip()
    fpsClock.tick(FPS)
    #print(fpsClock.get_fps())