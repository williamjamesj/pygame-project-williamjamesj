import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
import gameplay as game
# All of the buttons are in this array for easy access
def levelSelector(): 
    globals.screen.blit(globals.backgroundpicture, (0,0)) # Make the screen just the background
    unlockedlistbg = []
    unlockedlistfont = []
    for i in range(1,10):
        if globals.unlockedlevel >= i:
            unlockedlistbg.append((255,255,255))
            unlockedlistfont.append((0,0,0))
        else:
            unlockedlistbg.append((50,50,50))
            unlockedlistfont.append((255,255,255))
    # This took far too long and there was definitely a better way to do this.
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,-100],globals.screen, "1",50,unlockedlistbg[0],unlockedlistfont[0])) 
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,-100],globals.screen, "2",50,unlockedlistbg[1],unlockedlistfont[1]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,-100],globals.screen, "3",50,unlockedlistbg[2],unlockedlistfont[2]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,0],globals.screen, "4",50,unlockedlistbg[3],unlockedlistfont[3]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,0],globals.screen, "5",50,unlockedlistbg[4],unlockedlistfont[4]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,0],globals.screen, "6",50,unlockedlistbg[5],unlockedlistfont[5]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[-100,100],globals.screen, "7",50,unlockedlistbg[6],unlockedlistfont[6]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[0,100],globals.screen, "8",50,unlockedlistbg[7],unlockedlistfont[7]))
    globals.levelbuttonArray.append(buttons.Button(75,75,[100,100],globals.screen, "9",50,unlockedlistbg[8],unlockedlistfont[8]))
    globals.levelbuttonArray.append(buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)) # Back button offset 100 pixels from the bottom of the screen
    return
def displayMenu():
    # Play Button = 0
    globals.screen.blit(globals.backgroundpicture, (0,0))
    buttons.Button(0,0,[0,-300],globals.screen,globals.languagesdict["gamename"],200)
    globals.buttonArray.append(buttons.Button(400,100,[0,-75],globals.screen,globals.languagesdict["play"],100))
    globals.buttonArray.append(buttons.Button(400,100,[0,50],globals.screen,globals.languagesdict["instructions"],75))
    globals.buttonArray.append(buttons.Button(400,100,[0,175],globals.screen,globals.languagesdict["settings"],100))
    globals.buttonArray.append(buttons.Button(400,100,[0,300],globals.screen,globals.languagesdict["quit"],100))
    globals.levelbuttonArray = []
    return
def displayInstructions():
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.instructionsbackbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
def displaySettings():
    globals.screen.blit(globals.backgroundpicture, (0,0))
    globals.settingsbuttons.append(buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100))
def displayLevelOver():
    globals.screen.blit(globals.backgroundpicture, (0,0))
    buttons.Button(600,100,[0,-100],globals.screen, f"{globals.languagesdict['time']}: {math.floor(globals.leveltime/1000)} {globals.languagesdict['seconds']}",100,(255,255,255),(0,0,0))
    buttons.Button(800,100,[0,100],globals.screen, f"{globals.languagesdict['coinsgained']}: {math.floor(globals.coinsgained)}",100,(255,255,255),(0,0,0))
    globals.leveloverbackbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
def checkingMenu(position):
    if (globals.buttonArray[0].interacts(position)):
        globals.gamestage = "levelselect"
        globals.levelbuttonArray = [] # Clears the previous inhabitants of the array
    if (globals.buttonArray[1].interacts(position)):
        globals.gamestage = "instructions"
        globals.levelbuttonArray = [] # Clears the previous inhabitants of the array
    if (globals.buttonArray[2].interacts(position)):
        globals.gamestage = "settings"
        globals.levelbuttonArray = [] # Clears the previous inhabitants of the array
    if (globals.buttonArray[3].interacts(position)):
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
    elif(globals.levelbuttonArray[1].interacts(position)):
        game.playGame(2)
        return
    elif(globals.levelbuttonArray[2].interacts(position)):
        game.playGame(3)
        return
    elif(globals.levelbuttonArray[3].interacts(position)):
        game.playGame(4)
        return
    elif(globals.levelbuttonArray[4].interacts(position)):
        game.playGame(5)
        return
    elif(globals.levelbuttonArray[5].interacts(position)):
        game.playGame(6)
        return
    elif(globals.levelbuttonArray[6].interacts(position)):
        game.playGame(7)
        return
    elif(globals.levelbuttonArray[7].interacts(position)):
        game.playGame(8)
        return
    elif(globals.levelbuttonArray[8].interacts(position)):
        game.playGame(9)
        return
def checkingInstructions(position):
    if (globals.instructionsbackbutton.interacts(position)):
        globals.gamestage = "menu"
        globals.buttonArray = []
    return
def checkingSettings(position):
    if (globals.settingsbuttons[0].interacts(position)):
        globals.gamestage = "menu"
        globals.buttonArray = []
    return
def checkingLevelOver(position):
    if (globals.leveloverbackbutton.interacts(position)):
        globals.gamestage = "levelselect"
        globals.buttonArray = []
    return