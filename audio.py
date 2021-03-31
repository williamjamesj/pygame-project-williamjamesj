import pygame
from pygame.locals import *
import os
import random
class AudioHandler():
    def __init__(self):
        self.musiclist = []
        for i in os.listdir("resources/music"):
            self.musiclist.append(i)
        random.shuffle(self.musiclist)
        self.currentsong = 0
        self.musicvolume = 10
        self.sfxvolume = 10
        self.soundDict = {}
        self.soundDict['laser'] = pygame.mixer.Sound('resources/sounds/laser.mp3')
        self.soundDict['explosion'] = pygame.mixer.Sound('resources/sounds/explosion.mp3')
        return
    def playSound(self,sound):
        self.soundDict[sound].set_volume(self.sfxvolume/10)
        self.soundDict[sound].stop()
        self.soundDict[sound].play()
        return
    def nextSong(self):
        self.currentsong += 1
        if self.currentsong >= len(self.musiclist):
            self.currentsong -= len(self.musiclist)
        pygame.mixer.music.load(f"resources/music/{self.musiclist[self.currentsong]}")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.musicvolume/10)
        return
    def update(self):
        pygame.mixer.music.set_volume(self.musicvolume/10)
# if __name__ == "__main__":
#     pygame.mixer.init()
#     audioni = AudioHandler()