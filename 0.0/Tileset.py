# import python module
import pygame as pg
Vector2D = pg.math.Vector2

# import local module
from config import *

class Wall(pg.sprite.Sprite):
    def __init__(self, Game, x, y): 
        self.groups = Game.allDrawTileset
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = Game
        self.tileSize = self.game.tileSize
        # self.groups = Game.allDrawTileset
        self.image = pg.Surface((self.tileSize, self.tileSize))
        self.image.fill(DARKRED)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * self.tileSize
        self.rect.y = y * self.tileSize
        
    def update(self):
        self.tileSize = self.game.tileSize
        self.image = pg.Surface((self.tileSize, self.tileSize))
        self.image.fill(DARKRED)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * self.tileSize
        self.rect.y = self.y * self.tileSize