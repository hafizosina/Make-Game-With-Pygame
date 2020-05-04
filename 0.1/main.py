'''============================= IMPORT PYTHON MODULE ========================='''
import pygame as pg
import random
import os
vec2D = pg.math.Vector2

# this is not pygame base module
try:
    from pygame.my_modules import Camera
except :
    from tools.my_module import Camera

'''============================= IMPORT LOCAL MODULE ========================='''
from settings import *
from tools.gameType import *

'''============================= GLOBAL VARIABLE ========================='''
debugFPS = 0
debug0 = 0

class Game:
    def __init__(self):
        '''============================= INIT ========================='''
        self.Running = True
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100,100)
        
        
        '''=========================== SETUP WINDOW ========================='''
        self.width = WIDTH
        self.height = HEIGHT
        if FULLSCREEN:
            self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN)
            info = pg.display.Info()
            self.width = info.current_w
            self.height = info.current_h
        elif not FULLSCREEN:
            self.screen = pg.display.set_mode((self.width,self.height))
        pg.display.set_caption(TITLE)
        
        '''========================== SETUP ATTRIBUT ========================'''
        self.scale = 1
        self.tileSize = int(self.scale*TILESIZE)
        # self.scale and tilesize only use in draw grid. consider its later
        self.pause = False
        self.offset = vec2D(0,0)
        self.mainDir = os.path.dirname(__file__)
        self.runType = 'mainMenu'
        self.runTypeDict = {
                            'mainMenu':mainMenu, 
                            'flocking':flocking,
                            'drawMap':drawMap,
                            'combatSystem':combatSystem
                            }
                            
        '''============================= DEFINE SPRITE GROUPS} ========================='''
        # self.allDrawSprite = pg.sprite.Group()
        
        '''============================= BEGIN ============================='''
        self.SpalshLoading()
        self.run()
        
    def load(self):
        self.runChoice.load()
        
    def SpalshLoading(self):
        # NExt make Splash SCreen
        self.Camera = Camera(self.width, self.height)
        focus = self.Camera.makeFocus()
        self.runType = 'mainMenu'
        #i dont know why i do this mkae in split up dict
        self.runChoice = self.runTypeDict[self.runType](self)
        self.load() 
        # self.runChoice.begin()
    
    def run(self):
        while self.Running:
            self.dt = self.clock.tick(FPS) / 100
            if debugFPS:
                print('FPS: ',1/(self.dt),'\tDt: ',self.dt)
            self.event()
            self.update()
            self.draw()
    
    def event(self):
        pressed = pg.key.get_pressed()
        alt_held = pressed[pg.K_LALT] or pressed[pg.K_RALT]
        ctrl_held = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.Running = False
                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F4 and alt_held:
                    self.Running = False
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:        
                    if self.pause == True:
                        print('trun')
                        self.pause = False
                    elif self.pause == False:
                        print('tes')
                        self.pause = True
        self.runChoice.event()
        
    def update(self):
        if type(self.runChoice) != self.runTypeDict[self.runType]:
            self.runChoice = self.runTypeDict[self.runType](self)
        if self.runChoice.isLoad and self.runChoice.isBegin:
            self.runChoice.update()
        
    def draw(self):
        # will be no image until loading finish
        if self.runChoice.isLoad and self.runChoice.isBegin:
            self.runChoice.draw()
        if debug0:
            pg.draw.line(self.screen, RED, (-self.width, self.height//2), (self.width, self.height//2))
        if DRAWGRID and self.runType != 'mainMenu' :
            self.drawGrid()
        pg.display.flip()
            
            
    def drawGrid(self):
        for x in range(0, self.width, self.tileSize):
            pg.draw.line(self.screen, WHITE, (x+(self.offset.x%self.tileSize), 0), (x+(self.offset.x%self.tileSize), self.height))
        for y in range(0, self.height, self.tileSize):
            pg.draw.line(self.screen, WHITE, (0, y+(self.offset.y%self.tileSize)), (self.width, y+(self.offset.y%self.tileSize)))
    
    
if __name__ == '__main__':
    g = Game()
    pg.quit()