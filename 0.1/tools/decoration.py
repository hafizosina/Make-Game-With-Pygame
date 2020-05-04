'''============================= IMPORT PYTHON MODULE ========================='''
import pygame as pg
import random
import os
vec2D = pg.math.Vector2

'''============================= IMPORT LOCAL MODULE ========================='''
from settings import *

class drawImage(pg.sprite.Sprite):
    def __init__(self, Surfaces, x, y):
        '''============================= INIT ========================='''
        pg.sprite.Sprite.__init__(self)
        self.imageOriginal = Surfaces
        self.image = pg.transform.rotozoom(self.imageOriginal,0,1)
        self.rect = self.image.get_rect()
        
        '''============================= Placing ========================='''
        self.rect.x = x
        self.rect.y = y
        
class buttonOldWay(pg.sprite.Group):
    def __init__(self):
        try:
            self.font = pg.font.Font('arial',20)
        except:
            self.font = pg.font.Font(None, 20)
        
        pg.sprite.Group.__init__(self)
        self.iL = None
        self.iM = None
        self.iR = None
        self.hover = False
    
    def setImage(self, left,mid,right):
        self.iL = left
        self.iM = mid
        self.iR = right
    def makeButton(self, x, y, t, s = None, **kwarg):
        self.x, self.y, self.t  = x,y,t
        if self.iM == None:
            for i in range(t):
                pass
        if self.iM != None:
            if (self.iL != None) and (self.iR != None):
                self.add(drawImage(self.iL, self.x ,self.y))
                for i in range(t-1):
                    x = self.x + (self.iL.get_size()[0]*(i+1))
                    self.add(drawImage(self.iM, x, self.y))
                x = self.x + (self.iL.get_size()[0]*t) 
                self.add(drawImage(self.iR, x, self.y))
        return self
    
    def event(self, camera = None):
        self.hover = False
        mousePosition = pg.mouse.get_pos()
        if camera!= None:
            cameraPosition = camera.getPos()
            mousePosition = ( mousePosition[0] - cameraPosition[0], mousePosition[1] - cameraPosition[1])
        for sprite in self:
            if sprite.rect.collidepoint(mousePosition):
                self.hover = True   
                
class button(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.iL = None
        self.iM = None
        self.iR = None
        self.hover = False
        self.font_name = pg.font.match_font('constantia')
        self.font = pg.font.Font(self.font_name, 20)
        # self.font.set_bold(1)
    def setImage(self, left,mid,right):
        self.iL = left
        self.iM = mid
        self.iR = right
        self.tilesize = self.iM.get_size()[0]
    def makeButton(self, x, y, t, s = None, **kwarg):
        if self.iM == None:
            for i in range(t):
                pass
        if self.iM != None:
            if (self.iL != None) and (self.iR != None):
                self.x, self.y, self.t  = x,y,t
                h = self.tilesize
                w = self.tilesize*(t+1)
                self.oriImage = pg.Surface((w, h))
                self.oriImage.set_colorkey((0,0,0))
                self.oriImage.blit(self.iL, (0, 0))
                for i in range(t-1):
                    x = self.tilesize*(i+1)
                    self.oriImage.blit(self.iM, (x, 0))
                x = self.tilesize*t
                self.oriImage.blit(self.iR, (x, 0))
        self.rect = self.oriImage.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        if s != None:
            text = self.font.render(s, True, (58, 28, 18))
            text_rect = text.get_rect()
            text_rect.center = (w//2,h//2)
            self.oriImage.blit(text, text_rect)
        self.image = self.oriImage
        self.rect = self.oriImage.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        return self
    
    def event(self, camera = None):
        self.hover = False
        mousePosition = pg.mouse.get_pos()
        if camera!= None:
            cameraPosition = camera.getPos()
            mousePosition = ( mousePosition[0] - cameraPosition[0], mousePosition[1] - cameraPosition[1])
        if self.rect.collidepoint(mousePosition):
            self.hover = True   
        if self.hover:
            self.image = pg.transform.scale(self.oriImage,(int(self.tilesize*self.t*1.2), int(self.tilesize*1.2)))
        elif not self.hover:
            self.image = self.oriImage
            
# end