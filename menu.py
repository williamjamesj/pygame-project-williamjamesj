import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
import gameplay as game
# All of the buttons are in this array for easy access
def levelSelector(): 
    globals.screen.blit(globals.backgroundpicture, (0,0)) # Make the screen just the background
    # This took far too long and there was definitely a better way to do this.
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,-100],globals.screen, "1",50)) 
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,-100],globals.screen, "2",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,-100],globals.screen, "3",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,0],globals.screen, "4",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,0],globals.screen, "5",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,0],globals.screen, "6",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,100],globals.screen, "7",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,100],globals.screen, "8",50))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,100],globals.screen, "9",50))
    globals.levelbuttonArray.append(buttons.Button(200,100,[0,globals.dimensions[1]/2-100],globals.screen, "Back",100)) # Back button offset 100 pixels from the bottom of the screen
    return
def displayMenu():
    # Play Button = 0
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.buttonArray.append(buttons.Button(200,100,[0,-75],globals.screen,"Play",100))
    globals.buttonArray.append(buttons.Button(200,100,[0,75],globals.screen,"Quit",100))
    globals.levelbuttonArray = []
    return
def checkingMenu(position):
    if (globals.buttonArray[0].interacts(position)):
        globals.gamestage = "levelselect"
        globals.levelbuttonArray = [] # Clears the previous inhabitants of the array
    if (globals.buttonArray[1].interacts(position)):
        globals.running = False
        return
def checkingLevel(position):
    if (globals.levelbuttonArray[-1].interacts(position)):
        globals.gamestage = "menu"
        globals.buttonArray = [] # Clears the previous inhabitants of the array
        return
    elif(globals.levelbuttonArray[0].interacts(position)):
        game.playGame(1)
        return