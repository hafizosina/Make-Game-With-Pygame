'''============================= IMPORT PYTHON MODULE ========================='''
import pygame as pg
import random
import os
vec2D = pg.math.Vector2

'''============================= IMPORT LOCAL MODULE ========================='''
from settings import *
         
class Sprite(pg.sprite.Sprite):
    def __init__(self, Game, img, x = None,  y = None):
        pg.sprite.Sprite.__init__(self)
        self.game = Game
        self.position = vec2D(0,0) 
        self.direction = vec2D(-1,0).normalize()
        self.screen  =  self.game.screen

        '''=========================initial Sprite image and rect======================'''
        self.imageOri = img
        self.image = self.imageOri
        self.rect = self.image.get_rect()
        if x != None and y != None:
            self.position = vec2D(x,y)
        self.rect.center = (self.position)
        
    def update(self, camera = None):
        self.rect.center = self.position
        
class Souldier(Sprite):
    def __init__(self, Game, Type = 'SwordMan', Rank = 1 ,Race = 'Indo'): 
        self.game = Game # this not actual Game Clas this is gameType class
        self.Type = Type
        self.Race = Race
        self.Rank = Rank
        img = self.game.spriteImageList[self.Type]
        
        '''============================ INITIAL SPRITE CLASS =========================='''
        Sprite.__init__(self, Game, img)
        
    def Move(self, direction = vec2D(0,0)):
        direction = direction.normalize()
        print('Move ', direction)
        if self.direction != direction:
            self.position += self.direction+direction

class Character(Souldier):
    def __init__(self, Game , Name = "Unkown", Race = 'Indo'):
        self.game = Game
        self.Name = Name
        self.Race = Race
        self.Type = 'HorseSword'
        # rank for lord count in diferent way like : mecenary, merchat, lord, etc 
        self.Rank = 20
        
        '''========================== INITIAL SOULDIER CLASS =========================='''
        Souldier.__init__(self, Game, self.Type, self.Rank, self.Race)
 

class Player(Character):
    def __init__(self, Game, Name = 'Player', Race = 'Indo'):
        self.game = Game
        self.Race = Race
        self.Name = Name
		
        '''========================== INITIAL SOULDIER CLASS =========================='''
        Character.__init__(self, Game, self.Name, self.Race)
        
      
        
        
        
#end