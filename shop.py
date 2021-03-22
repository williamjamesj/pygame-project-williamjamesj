import math
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
class shopScreen():
    def __init__(self):
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
    def displayShop(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.backbutton.draw(globals.screen)
        
    def updateShop(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"