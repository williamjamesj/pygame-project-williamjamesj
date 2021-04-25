from typing import NoReturn
from spaceship import DummySpaceship, PlayerSpaceship
from networking import ClientConnectionHandler, HostConnectionHandler
import pygame
from pygame.locals import *
import buttons
import globalvariables as globals
from pygame.locals import *

class MultiplayerMenu():
    def __init__(self):
        self.stringInput = ""
        self.ipLabel = buttons.Button(600,100,[0,75-globals.dimensions[1]/2],globals.screen, globals.languagesdict["ipaddress"],100)
        self.submitButton = buttons.Button(100,100,[400,200-globals.dimensions[1]/2],globals.screen, ">",100)
        self.backButton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.hostgame = buttons.Button(400,100,[0,150],globals.screen,globals.languagesdict["hostgame"],100)
        return
    def draw(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.ipLabel.draw(globals.screen)
        self.submitButton.draw(globals.screen)
        self.ipbar = buttons.Button(800,100,[-100,200-globals.dimensions[1]/2],globals.screen, self.stringInput,100)
        self.backButton.draw(globals.screen)
        self.hostgame.draw(globals.screen)
        return
    def clickUpdate(self,mouseposition):
        if self.submitButton.interacts(mouseposition):
            self.joinGame()
        elif self.backButton.interacts(mouseposition):
            globals.gamestage = "levelselect"
            globals.connecting = False
        elif self.hostgame.interacts(mouseposition):
            self.hostGame()
        return
    def keyUpdate(self,event): # https://stackoverflow.com/questions/46252905/on-screen-typing-in-pygame/46253506
        if event.key == K_BACKSPACE:
            self.stringInput = self.stringInput[:-1]
        elif event.key == K_RETURN:
            self.joinGame()
        else:
            self.stringInput += event.unicode
        return
    def hostGame(self):
        globals.allplayers = {}
        self.otherplayers = {}
        globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2
        globals.playerspaceship = PlayerSpaceship([globals.dimensions[0]/2,globals.dimensions[1]/2],globals.playercurrentship[0],globals.playercurrentship[1],globals.playercurrentship[2],0,globals.playercurrentship[3],globals.playercurrentship[6],firerate=globals.playercurrentship[4])
        globals.gamestage = "multiplayer"
        self.connection = HostConnectionHandler()
        return
    def joinGame(self):
        globals.allplayers = {}
        self.otherplayers = {}
        globals.playerorigin = globals.dimensions[0]/2,globals.dimensions[1]/2
        globals.playerspaceship = PlayerSpaceship([globals.dimensions[0]/2,globals.dimensions[1]/2],globals.playercurrentship[0],globals.playercurrentship[1],globals.playercurrentship[2],0,globals.playercurrentship[3],globals.playercurrentship[6],firerate=globals.playercurrentship[4])
        globals.gamestage = "multiplayer"
        self.connection = ClientConnectionHandler(self.stringInput)
        return
    def updateGame(self,keys):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        globals.allplayers[globals.name] = [globals.playerspaceship.percievedx,globals.playerspaceship.percievedy,globals.playerspaceship.direction]
        if keys[pygame.K_ESCAPE]==1:
            globals.gamestage = "levelselect"
            globals.connecting = False
        globals.playerspaceship.update(keys[pygame.K_UP]==1 or keys[pygame.K_w],keys[pygame.K_DOWN]==1 or keys[pygame.K_s],keys[pygame.K_LEFT]==1 or keys[pygame.K_a],keys[pygame.K_RIGHT] or keys[pygame.K_d]==1,keys[pygame.K_SPACE] or keys[pygame.K_TAB])
        globals.playerspaceship.draw(globals.screen)
        self.connection.sayHello()
        print(globals.allplayers)
        for i in globals.allplayers:
            if i == globals.name:
                pass
            elif i in self.otherplayers:
                self.otherplayers[i].x, self.otherplayers[i].y, self.otherplayers[i].direction = globals.allplayers[i]
                print("here")
            else:
                self.otherplayers[i] = DummySpaceship()
        for i in self.otherplayers:
            self.otherplayers[i].update()
            self.otherplayers[i].draw(globals.screen)
        return