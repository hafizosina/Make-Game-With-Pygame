#importing python module
import pygame as pg
import random
import os
Vector2D = pg.math.Vector2

#importing local module
from config import*

class Map:
    def __init__(self):
        self.data = []
    def load(self):
        mapData = []
        with open('tes.map', 'rt') as f:
            dataString = f.read()
        dataString = dataString.split(';')
        for eachData in dataString:
            mapData.append(eachData.split(','))
        for datas in mapData:
            print(datas)
    

# class Camera:
    # def __init__(self, width, height):
        # self.camera = pg.Rect(0, 0, width, height)
        # self.width = width
        # self.height = height

    # def apply(self, entity):
        # return entity.rect.move(self.camera.topleft)

    # def update(self, target):
        # x = -target.rect.x + int(WIDTH / 2)
        # y = -target.rect.y + int(HEIGHT / 2)

        # self.camera = pg.Rect(x, y, self.width, self.height)
        
    # def getPos(self):
        # return self.camera.x, self.camera.y
        
if __name__=='__main__':
    mapFunc = Map()
    mapFunc.load()