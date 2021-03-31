from pygame import font
import globalvariables as globals
import buttons
class settingsScreen():
    def __init__(self) -> None:
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.music = buttons.Button(300,100,[-250,0],globals.screen, f"{globals.languagesdict['musicvol']}: {str(globals.audioHandler.musicvolume)}",25,font='Roboto-Regular')
        self.sfx = buttons.Button(300,100,[250,0],globals.screen, f"{globals.languagesdict['sfxvol']}: {str(globals.audioHandler.sfxvolume)}",25,font='Roboto-Regular')
        self.musicleft = buttons.Button(50,50,[-450,0],globals.screen, "<",25,font='Roboto-Regular')
        self.musicright = buttons.Button(50,50,[-50,0],globals.screen, ">",25,font='Roboto-Regular')
        self.sfxright = buttons.Button(50,50,[450,0],globals.screen, ">",25,font='Roboto-Regular')
        self.sfxleft = buttons.Button(50,50,[50,0],globals.screen, "<",25,font='Roboto-Regular')
    def displaySettings(self):
        globals.screen.blit(globals.backgroundpicture, (0,0))
        self.backbutton.draw(globals.screen)
        self.music = buttons.Button(300,100,[-250,0],globals.screen, f"{globals.languagesdict['musicvol']}: {str(globals.audioHandler.musicvolume)}",25,font='Roboto-Regular')
        self.sfx = buttons.Button(300,100,[250,0],globals.screen, f"{globals.languagesdict['sfxvol']}: {str(globals.audioHandler.sfxvolume)}",25,font='Roboto-Regular')
        self.musicleft.draw(globals.screen)
        self.musicright.draw(globals.screen)
        self.sfxleft.draw(globals.screen)
        self.sfxright.draw(globals.screen)
    def updateSettings(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"
        if self.musicleft.interacts(mouseposition):
            if globals.audioHandler.musicvolume > 0:
                globals.audioHandler.musicvolume -= 1
                globals.audioHandler.update()
        if self.musicright.interacts(mouseposition):
            if globals.audioHandler.musicvolume < 10:
                globals.audioHandler.musicvolume += 1
                globals.audioHandler.update()
        if self.sfxleft.interacts(mouseposition):
            if globals.audioHandler.sfxvolume > 0:
                globals.audioHandler.sfxvolume -= 1
                globals.audioHandler.update()
        if self.sfxright.interacts(mouseposition):
            if globals.audioHandler.sfxvolume < 10:
                globals.audioHandler.sfxvolume += 1
                globals.audioHandler.update()
            