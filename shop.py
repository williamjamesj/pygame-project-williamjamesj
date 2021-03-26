import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class shopScreen():
    def __init__(self):
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.spaceships = [["yellowspaceship",10,0.1,3,1,0],["greenspaceship",10,0.1,3,0.5,100000]] # The lists store ships in order: appearance,maxspeed,acceleration,turnspeed,firerate
        self.spaceshipimages = []
        for i in self.spaceships:
            self.spaceshipimages.append(pygame.image.load(f"resources/spaceships/shopimages/{i[0]}.png"))
        self.currentship = 0
    def displayShop(self):
        if self.currentship>len(self.spaceships)-1:
            self.currentship = 0
        if self.currentship<0:
            self.currentship = len(self.spaceships)-1
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.backbutton.draw(globals.screen)
        self.leftbutton = buttons.Button(100,100,[100-globals.dimensions[0]/2,-200],globals.screen,"<",100)
        self.rightbutton = buttons.Button(100,100,[400-globals.dimensions[0]/2,-200],globals.screen,">",100)
        if self.spaceships[self.currentship][0] == globals.playercurrentship[0]:
            purchasetext = "Selected"
        elif self.spaceships[self.currentship][0]  in globals.ownedShips:
            purchasetext = "Select"
        else:
            purchasetext = f"{self.spaceships[self.currentship][5]} Coins"
        self.purchaseselect = buttons.Button(400,100,[300-globals.dimensions[0]/2,globals.dimensions[1]/2-250],globals.screen,purchasetext,75)
        shiprect = self.spaceshipimages[self.currentship].get_rect()
        shiprect.center = (250,globals.dimensions[1]/2-200)
        globals.screen.blit(self.spaceshipimages[self.currentship], shiprect)
        buttons.Button(500,100,[globals.dimensions[0]/2-300,100-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['coins']}: {'{:,}'.format(globals.coins)}",75) # Comma formatting from https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string.
        
    def updateShop(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"
        if self.leftbutton.interacts(mouseposition):
            self.currentship -= 1
        if self.rightbutton.interacts(mouseposition):
            self.currentship += 1