import pygame
from pygame.locals import *
import globalvariables as globals
class Button():
    """Basic class to draw buttons. Buttons can be compared against a position (typically of the mouse pointer) to detect interaction, or simply used to display text without interaction."""
    # Draws a button with the given width and height, at a position offset from the center of the screen, which allows for the change of resolutions
    def __init__(self,width,height,position,surface,text,size,buttoncolour=(50,50,50),textcolour=(255,255,255),font="Nougat"):
        self.buttoncolour = buttoncolour
        x,y = position
        self.rectangle = pygame.Rect(0,0,width,height)
        self.rectangle.center = (globals.dimensions[0]/2+x,globals.dimensions[1]/2+y)
        pygame.draw.rect(surface, buttoncolour, self.rectangle, border_radius = 15)
        font = pygame.font.Font(f'resources/fonts/{font}.ttf', size)
        self.textobject = font.render(text, True, textcolour)
        # Draws the text in the center of the rectangle, whilst offsetting the text by the width of the text, so that it remains centered, instead of being offset to the bottom right.
        self.textw = self.rectangle.centerx - self.textobject.get_width()/2
        self.texth = self.rectangle.centery - self.textobject.get_height()/2
        surface.blit((self.textobject), (self.textw,self.texth))
        return
    def interacts(self, mouseposition): # I probably should have just made it a sprite and used sprite collision code.
        mx,my = mouseposition
        topx,topy = self.rectangle.topleft
        bottomx,bottomy = self.rectangle.bottomright
        # Checks if the position of the mouse is inside the bounds of the rectangle
        if ((mx>=topx and my>=topy) and (mx<=bottomx and my<=bottomy)):
            return True # There was definitely a better way to do this.
        else:
            return False
    def draw(self,surface):
        pygame.draw.rect(surface, self.buttoncolour, self.rectangle, border_radius = 15)
        surface.blit((self.textobject), (self.textw,self.texth))
        return