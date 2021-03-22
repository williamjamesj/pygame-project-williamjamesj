import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class shopScreen():
    def __init__(self):
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.arrows = [pygame.image.load("resources/arrow_left.png"),pygame.image.load("resources/arrow_right.png")]
        self.spaceships = ["yellowspaceship","greenspaceship"]
        self.spaceshipimages = []
        for i in self.spaceships:
            self.spaceshipimages.append(pygame.image.load(f"resources/spaceships/{i}/shop.png"))
        self.currentship = 0
    def displayShop(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.backbutton.draw(globals.screen)
        self.leftbutton = buttons.Button(100,100,[-400,-200],globals.screen,"<",100)
        self.rightbutton = buttons.Button(100,100,[-100,-200],globals.screen,">",100)
        shiprect = self.spaceshipimages[self.currentship].get_rect()
        shiprect.center = (globals.dimensions[0]/2-250,globals.dimensions[1]/2-200)
        globals.screen.blit(self.spaceshipimages[0], shiprect)
        
    def updateShop(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"