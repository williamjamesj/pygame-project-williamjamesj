from pygame import font, mouse
import globalvariables as globals
import buttons
import localisation
class settingsScreen():
    def __init__(self): # Define all of the buttons that can be drawn.
        self.backbutton = buttons.Button(300,100,[0,globals.dimensions[1]/2-100],globals.screen, globals.languagesdict["back"],100)
        self.music = buttons.Button(300,100,[-250,0],globals.screen, f"{globals.languagesdict['musicvol']}: {str(globals.audioHandler.musicvolume)}",25,font='Roboto-Regular')
        self.sfx = buttons.Button(300,100,[250,0],globals.screen, f"{globals.languagesdict['sfxvol']}: {str(globals.audioHandler.sfxvolume)}",25,font='Roboto-Regular')
        self.settingsstage = "music"
        self.musicleft = buttons.Button(50,50,[-450,0],globals.screen, "<",25,font='Roboto-Regular')
        self.musicright = buttons.Button(50,50,[-50,0],globals.screen, ">",25,font='Roboto-Regular')
        self.sfxright = buttons.Button(50,50,[450,0],globals.screen, ">",25,font='Roboto-Regular')
        self.sfxleft = buttons.Button(50,50,[50,0],globals.screen, "<",25,font='Roboto-Regular')
        self.musicOption = buttons.Button(300,100,[-350,globals.dimensions[1]/2*-1+100],globals.screen, globals.languagesdict['musicsettings'],40)
        self.languageOption = buttons.Button(300,100,[0,globals.dimensions[1]/2*-1+100],globals.screen, globals.languagesdict['languagesettings'],40)
        self.creditsOption = buttons.Button(300,100,[350,globals.dimensions[1]/2*-1+100],globals.screen, globals.languagesdict['credits'],40)
        self.englishButton = buttons.Button(200,100,[-200,0],globals.screen, globals.languagesdict['english'],40)
        self.spanishButton = buttons.Button(200,100,[200,0],globals.screen, globals.languagesdict['spanish'],40)
        return
    def displaySettings(self):
        globals.screen.blit(globals.backgroundpicture, (0,0)) # Draw the elements that will remain constant across settings screens, such as the navigation and back buttons.
        self.backbutton.draw(globals.screen)
        self.musicOption.draw(globals.screen)
        self.languageOption.draw(globals.screen)
        self.creditsOption.draw(globals.screen)
        if self.settingsstage == "music": # Display the relevant settings screen.
            self.displayMusicOptions()
        elif self.settingsstage == "lang":
            self.displayLanguageOptions()
        elif self.settingsstage == "credits":
            self.displayCredits()
        return
    def displayMusicOptions(self): # Just display two labels with the volumes on them, and two buttons each to control both of the volumes. 
        self.music = buttons.Button(300,100,[-250,0],globals.screen, f"{globals.languagesdict['musicvol']}: {str(globals.audioHandler.musicvolume)}",25,font='Roboto-Regular')
        self.sfx = buttons.Button(300,100,[250,0],globals.screen, f"{globals.languagesdict['sfxvol']}: {str(globals.audioHandler.sfxvolume)}",25,font='Roboto-Regular')
        self.musicleft.draw(globals.screen)
        self.musicright.draw(globals.screen)
        self.sfxleft.draw(globals.screen)
        self.sfxright.draw(globals.screen)
        return
    def updateSettings(self,mouseposition):
        if self.backbutton.interacts(mouseposition):
            globals.gamestage = "menu"
        elif self.musicOption.interacts(mouseposition):
            self.settingsstage = "music"
        elif self.languageOption.interacts(mouseposition):
            self.settingsstage = "lang"
        elif self.creditsOption.interacts(mouseposition):
            self.settingsstage = "credits"
        elif self.settingsstage == "music":
            self.checkMusicOptions(mouseposition)
        elif self.settingsstage == "lang":
            self.checkLanguageOptions(mouseposition)
        return
    def checkMusicOptions(self,mouseposition):
        if self.musicleft.interacts(mouseposition):
            if globals.audioHandler.musicvolume > 0: # This stops the volume going into the negatives, which would presumably result in an error.
                globals.audioHandler.musicvolume -= 1
                globals.audioHandler.update() # Always call this, otherwise the audioHandler will not change the volume until the next song plays.
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
        return
    def checkLanguageOptions(self,mouseposition):
        if self.englishButton.interacts(mouseposition):
            localisation.setlang("english")
            globals.lang = "english"
            localisation.readtexts()
            print(globals.languagesdict)
            self.__init__() # Reloads all of the buttons on the screen, so that the language is changed.
        elif self.spanishButton.interacts(mouseposition):
            localisation.setlang("spanish")
            globals.lang = "spanish"
            localisation.readtexts()
            print(globals.languagesdict)
            self.__init__()
        return
    def displayLanguageOptions(self):
        self.englishButton.draw(globals.screen)
        self.spanishButton.draw(globals.screen)
        return
    def displayCredits(self):
        buttons.Button(1000,50,[0,-150],globals.screen,globals.languagesdict["creditsone"],25,font='Roboto-Regular')
        buttons.Button(1000,50,[0,-75],globals.screen,globals.languagesdict["creditstwo"],25,font='Roboto-Regular')
        buttons.Button(250,55,[0,0],globals.screen,globals.languagesdict["music"],50,font='Roboto-Regular')
        buttons.Button(1000,50,[0,75],globals.screen,globals.languagesdict["creditsthree"],25,font='Roboto-Regular')
        buttons.Button(1000,50,[0,150],globals.screen,globals.languagesdict["creditsfour"],25,font='Roboto-Regular')
        return