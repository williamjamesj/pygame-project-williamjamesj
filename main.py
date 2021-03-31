from audio import AudioHandler
from shop import shopScreen
import pygame
from pygame.locals import *
from menu import MenuObject
import globalvariables as globals
from gameplay import updateGame
import os, sys
import math
import localisation
from persistantdata import load,save
from settings import settingsScreen
# Sets the language to whatever is stored in resources/localisation/lastlang and reads that language to globals.languagesdict
localisation.readlang()
localisation.readtexts()
# Defaults to Fullscreen Resolution 
pygame.display.set_caption('Cosmoracer')
pygame.display.set_icon(pygame.image.load("resources/icon.png"))
globals.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN|pygame.NOFRAME) # Both of these options ensure compatibility across systems.
# globals.screen = pygame.display.set_mode((1024,768)) # The display resolution that is minimum.
# Retrieves the size of the fullscreen window, important for properly positioning things on the screen
info = pygame.display.Info()
globals.dimensions = [info.current_w, info.current_h] # Dimensions of the screen
# Saves the current stage in the game
pygame.init() # initializes all of the pygame functionality including fonts and audio
FPS = 60
fpsClock = pygame.time.Clock()
globals.backgroundpicture = pygame.image.load("resources/background.jpg")
globals.coins,globals.unlockedlevel,globals.ownedShips,globals.playercurrentship,musicvol,sfxvol = load()
globals.ownedShips = globals.ownedShips.split('/')
globals.playercurrentship = globals.playercurrentship.split('/')
shop = shopScreen()
menu = MenuObject()
endsong = USEREVENT + 3
pygame.mixer.music.set_endevent(endsong) # This was helpful for the event handling with music https://nerdparadise.com/programming/pygame/part3
globals.audioHandler = AudioHandler()
globals.audioHandler.musicvolume = musicvol
globals.audioHandler.sfxvolume = sfxvol
globals.audioHandler.nextSong()
settings = settingsScreen()
while globals.running: # The main loop can be stopped from any file
    '''Main Loop - Always running, until the game stops.'''
    if globals.gamestage == "game": # Loops while the player is playing the game, at the top of the elif list because it should be prioritised.
        updateGame(pygame.key.get_pressed())
        globals.leveltimer.tick()
        globals.leveltime += globals.leveltimer.get_time()
    elif globals.gamestage =="menu": # Loops while the player is in menu.
        menu.displayMenu()
    elif globals.gamestage == "levelselect":
        menu.levelSelector()
    elif globals.gamestage == "instructions":
        menu.displayInstructions()
    elif globals.gamestage == "settings":
        settings.displaySettings()
    elif globals.gamestage == "levelover":
        menu.displayLevelOver()
    elif globals.gamestage == "shop":
        shop.displayShop()
    for event in pygame.event.get():
        if event.type == QUIT:
            globals.running = False
        # Checks if any buttons have been pressed in the menu stage.
        elif (globals.gamestage == "menu" and event.type == MOUSEBUTTONDOWN):
            menu.checkingMenu(pygame.mouse.get_pos())
        elif (globals.gamestage == "levelselect" and event.type == MOUSEBUTTONDOWN):
            menu.checkingLevel(pygame.mouse.get_pos())
        elif (globals.gamestage == "instructions" and event.type == MOUSEBUTTONDOWN):
            menu.checkingInstructions(pygame.mouse.get_pos())
        elif (globals.gamestage == "settings" and event.type == MOUSEBUTTONDOWN):
            settings.updateSettings(pygame.mouse.get_pos())
        elif (globals.gamestage == "levelover" and event.type == MOUSEBUTTONDOWN):
            menu.checkingLevelOver(pygame.mouse.get_pos())
        elif (globals.gamestage == "shop" and event.type == MOUSEBUTTONDOWN):
            shop.updateShop(pygame.mouse.get_pos())
        elif event.type == USEREVENT + 1 and globals.gamestage == "game":
            globals.playerspaceship.canshoot = True
        elif event.type == USEREVENT + 2:
            globals.playerspaceship.firerate = globals.playerspaceship.originalfirerate
        elif event.type == USEREVENT + 3:
            globals.audioHandler.nextSong()
    if globals.debug:
        font = pygame.font.Font('resources/fonts/Nougat.ttf', 50)
        textobject = font.render(str(math.ceil(fpsClock.get_fps())), True, (255,0,0))
        globals.screen.blit(textobject, (0,0))
    pygame.display.flip()
    fpsClock.tick(FPS)
newShip = []
for i in globals.playercurrentship:
    newShip.append(str(i))
save(globals.coins,globals.unlockedlevel,globals.ownedShips,newShip,globals.audioHandler.musicvolume,globals.audioHandler.sfxvolume)
sys.exit()