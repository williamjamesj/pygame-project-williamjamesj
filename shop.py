import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class shopScreen():
    def __init__(self):
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.arrows = [pygame.image.load("resources/arrow_left.png"),pygame.image.load("resources/arrow_right.png")]
        self.spaceships = [["yellowspaceship"],["greenspaceship"]] # The lists store ships in order: appearance,maxspeed,acceleration,turnspeed,firerate
        self.spaceshipimages = []
        for i in self.spaceships:
            self.spaceshipimages.append(pygame.image.load(f"resources/spaceships/{i[0]}/shop.png"))
        self.currentship = 0
    def displayShop(self):
        if self.currentship>len(self.spaceships)-1:
            self.currentship = 0
        if self.currentship<0:
            self.currentship = len(self.spaceships)-1
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.backbutton.draw(globals.screen)
        self.leftbutton = buttons.Button(100,100,[-400,-100],globals.screen,"<",100)
        self.rightbutton = buttons.Button(100,100,[-100,-100],globals.screen,">",100)
        shiprect = self.spaceshipimages[self.currentship].get_rect()
        shiprect.center = (globals.dimensions[0]/2-250,globals.dimensions[1]/2-100)
        globals.screen.blit(self.spaceshipimages[self.currentship], shiprect)
        buttons.Button(500,100,[200,-300],globals.screen,f"{globals.languagesdict['coins']}: {'{:,}'.format(globals.coins)}",75) # Comma formatting from https://stackoverflow.com/questions/5180365/python-add-comma-into-number-string.
        
    def updateShop(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"
        if self.leftbutton.interacts(mouseposition):
            self.currentship -= 1
        if self.rightbutton.interacts(mouseposition):
            self.currentship += 1