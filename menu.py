import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
import gameplay as game
# All of the buttons are in this array for easy access
class MenuObject():
    def __init__(self):
        self.menuButtonArray = [] # All of the buttons used in the main menu.
        self.levelbuttonArray = [] # All of the buttons used in the level selector.
        self.settingsButtonArray = [] # All of the buttons used in the settings screen.
        self.leveloverbackbutton = None # The back button displayed to take the player back to the levelselector, once they have completed a level.
        self.instructionsbackbutton = None # The back button for the instructions screen, it is the only button on the screen so it does not require an array.
    def levelSelector(self): 
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
        self.levelbuttonArray.append(buttons.Button(75,75,[-100,-100],globals.screen, "1",50,unlockedlistbg[0],unlockedlistfont[0])) 
        self.levelbuttonArray.append(buttons.Button(75,75,[0,-100],globals.screen, "2",50,unlockedlistbg[1],unlockedlistfont[1]))
        self.levelbuttonArray.append(buttons.Button(75,75,[100,-100],globals.screen, "3",50,unlockedlistbg[2],unlockedlistfont[2]))
        self.levelbuttonArray.append(buttons.Button(75,75,[-100,0],globals.screen, "4",50,unlockedlistbg[3],unlockedlistfont[3]))
        self.levelbuttonArray.append(buttons.Button(75,75,[0,0],globals.screen, "5",50,unlockedlistbg[4],unlockedlistfont[4]))
        self.levelbuttonArray.append(buttons.Button(75,75,[100,0],globals.screen, "6",50,unlockedlistbg[5],unlockedlistfont[5]))
        self.levelbuttonArray.append(buttons.Button(75,75,[-100,100],globals.screen, "7",50,unlockedlistbg[6],unlockedlistfont[6]))
        self.levelbuttonArray.append(buttons.Button(75,75,[0,100],globals.screen, "8",50,unlockedlistbg[7],unlockedlistfont[7]))
        self.levelbuttonArray.append(buttons.Button(75,75,[100,100],globals.screen, "9",50,unlockedlistbg[8],unlockedlistfont[8]))
        self.levelbuttonArray.append(buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)) # Back button offset 100 pixels from the bottom of the screen
        return
    def displayMenu(self):
        # Play Button = 0
        globals.screen.blit(globals.backgroundpicture, (0,0))
        buttons.Button(0,0,[0,-300],globals.screen,globals.languagesdict["gamename"],200)
        self.menuButtonArray.append(buttons.Button(300,75,[0,-75],globals.screen,globals.languagesdict["play"],75))
        self.menuButtonArray.append(buttons.Button(300,75,[0,25],globals.screen,globals.languagesdict["instructions"],50))
        self.menuButtonArray.append(buttons.Button(300,75,[0,125],globals.screen,globals.languagesdict["shop"],75))
        self.menuButtonArray.append(buttons.Button(300,75,[0,225],globals.screen,globals.languagesdict["settings"],75))
        self.menuButtonArray.append(buttons.Button(300,75,[0,325],globals.screen,globals.languagesdict["quit"],75))
        self.levelbuttonArray = []
        return
    def displayInstructions(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.instructionsbackbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        buttons.Button(1000,40,[0,50-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionone"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,100-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructiontwo"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,150-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionthree"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,200-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionfour"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,250-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionfive"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,300-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionsix"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,400-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionseven"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,450-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructioneight"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,500-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionnine"],30,font="Roboto-Regular")
        buttons.Button(1000,40,[0,550-globals.dimensions[1]/2],globals.screen,globals.languagesdict["instructionten"],30,font="Roboto-Regular")
        return
    def displaySettings(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.settingsButtonArray.append(buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100))
        return
    def displayLevelOver(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        buttons.Button(600,100,[0,-100],globals.screen, f"{globals.languagesdict['time']}: {math.floor(globals.leveltime/1000)} {globals.languagesdict['seconds']}",100,(255,255,255),(0,0,0))
        buttons.Button(800,100,[0,100],globals.screen, f"{globals.languagesdict['coinsgained']}: {math.floor(globals.coinsgained)}",100,(255,255,255),(0,0,0))
        self.leveloverbackbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        return
    def checkingMenu(self,position):
        if (self.menuButtonArray[0].interacts(position)):
            globals.gamestage = "levelselect"
            self.levelbuttonArray = [] # Clears the previous inhabitants of the array
        if (self.menuButtonArray[1].interacts(position)):
            globals.gamestage = "instructions"
            self.levelbuttonArray = []
        if (self.menuButtonArray[2].interacts(position)):
            globals.gamestage = "shop"
            self.levelbuttonArray = []
        if (self.menuButtonArray[3].interacts(position)):
            globals.gamestage = "settings"
            self.levelbuttonArray = []
        if (self.menuButtonArray[4].interacts(position)):
            globals.running = False
        return
    def checkingLevel(self,position):
        if (self.levelbuttonArray[-1].interacts(position)):
            globals.gamestage = "menu"
            globals.menuButtonArray = [] # Clears the previous inhabitants of the array
        elif(self.levelbuttonArray[0].interacts(position)):
            game.playGame(1)
        elif(self.levelbuttonArray[1].interacts(position)):
            game.playGame(2)
        elif(self.levelbuttonArray[2].interacts(position)):
            game.playGame(3)
        elif(self.levelbuttonArray[3].interacts(position)):
            game.playGame(4)
        elif(self.levelbuttonArray[4].interacts(position)):
            game.playGame(5)
        elif(self.levelbuttonArray[5].interacts(position)):
            game.playGame(6)
        elif(self.levelbuttonArray[6].interacts(position)):
            game.playGame(7)
        elif(self.levelbuttonArray[7].interacts(position)):
            game.playGame(8)
        elif(self.levelbuttonArray[8].interacts(position)):
            game.playGame(9)
        return
    def checkingInstructions(self,position):
        if (self.instructionsbackbutton.interacts(position)):
            globals.gamestage = "menu"
            self.menuButtonArray = []
        return
    def checkingSettings(self,position):
        if (self.settingsButtonArray[0].interacts(position)):
            globals.gamestage = "menu"
            self.menuButtonArray = []
        return
    def checkingLevelOver(self,position):
        if (self.leveloverbackbutton.interacts(position)):
            globals.gamestage = "levelselect"
            self.menuButtonArray = []
        return