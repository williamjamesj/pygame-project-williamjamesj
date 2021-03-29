import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class shopScreen():
    def __init__(self):
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.spaceships = [["yellowspaceship",10,0.1,3,1,0,0],["redspaceship",15,0.2,5,2,20000,2],["bigspaceship",20,0.1,1,0.2,30000,5]] # The lists store ships in this order: appearance,maxspeed,acceleration,turnspeed,firerate
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
        self.leftbutton = buttons.Button(100,100,[100-globals.dimensions[0]/2,-100],globals.screen,"<",100)
        self.rightbutton = buttons.Button(100,100,[400-globals.dimensions[0]/2,-100],globals.screen,">",100)
        if self.spaceships[self.currentship][0] == globals.playercurrentship[0]:
            purchasetext = globals.languagesdict['selected']
        elif self.spaceships[self.currentship][0]  in globals.ownedShips:
            purchasetext = globals.languagesdict['select']
        else:
            purchasetext = f"{'{:,}'.format(self.spaceships[self.currentship][5])} {globals.languagesdict['coins']}"
        self.purchaseselect = buttons.Button(450,100,[250-globals.dimensions[0]/2,globals.dimensions[1]/2-250],globals.screen,purchasetext,75)
        shiprect = self.spaceshipimages[self.currentship].get_rect()
        shiprect.center = (250,globals.dimensions[1]/2-100)
        globals.screen.blit(self.spaceshipimages[self.currentship], shiprect)
        buttons.Button(500,100,[globals.dimensions[0]/2-250,100-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['coins']}: {'{:,}'.format(globals.coins)}",75) # Comma formatting from https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string.
        # The displays of the stats of the relevant ship:
        buttons.Button(500,60,[globals.dimensions[0]/2-250,250-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['name']}: {globals.languagesdict[self.spaceships[self.currentship][0]]}",50)
        buttons.Button(500,60,[globals.dimensions[0]/2-250,315-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['maximumspeed']}: {str(self.spaceships[self.currentship][1])}",50)
        buttons.Button(500,60,[globals.dimensions[0]/2-250,380-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['acceleration']}: {str(self.spaceships[self.currentship][2]*10)}",50)
        buttons.Button(500,60,[globals.dimensions[0]/2-250,445-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['turnspeed']}: {str(self.spaceships[self.currentship][3])}",50)
        buttons.Button(500,60,[globals.dimensions[0]/2-250,510-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['firerate']}: {str(1/self.spaceships[self.currentship][4])}",50)
        buttons.Button(500,60,[globals.dimensions[0]/2-250,575-globals.dimensions[1]/2],globals.screen,f"{globals.languagesdict['shielding']}: {str(self.spaceships[self.currentship][6])}",50)
    def updateShop(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"
        if self.leftbutton.interacts(mouseposition):
            self.currentship -= 1
        if self.rightbutton.interacts(mouseposition):
            self.currentship += 1
        if self.purchaseselect.interacts(mouseposition):
            if self.spaceships[self.currentship][0] == globals.playercurrentship[0]:
                pass
            elif self.spaceships[self.currentship][0] in globals.ownedShips:
                globals.playercurrentship = self.spaceships[self.currentship]
            else:
                if globals.coins >= self.spaceships[self.currentship][5]:
                    globals.coins -= self.spaceships[self.currentship][5]
                    globals.ownedShips.append(self.spaceships[self.currentship][0])