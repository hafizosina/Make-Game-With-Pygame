#importing python module
import pygame as pg
import random
import os
Vector2D = pg.math.Vector2

#importing local module
from config import *
from Sprite import *
from tools import *
import Tileset

debugFPS = 0

gameFolder = os.path.dirname(__file__)
imgFolder = os.path.join(gameFolder,imageDir)
tileFolder = os.path.join(gameFolder, tileDir)
mapFolder = os.path.join(gameFolder, mapDir)
class Game:
    def __init__(self):
        '''============================= INIT ========================='''
        self.Running = True
        pg.init()
        pg.mixer.init()
        pg.key.set_repeat(100,100)
        
        
        '''=========================== SETUP WINDOW ========================='''
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.scale = 1
        self.tileSize = int(self.scale*TILESIZE)
        
        """============= Define All Sprites Group ============"""
        self.allDrawSprite = pg.sprite.Group()
        self.allDrawTileset = pg.sprite.Group()
        self.allSolid = pg.sprite.Group()
        
        '''====================== ALL ADITIONAL VARIABLE ====================='''
        self.gameType = 'drawTile'
        self.offset = Vector2D(0,0)
        self.matchOffset = Vector2D(0,0)
        
        
        """===================== BEGIN ======================"""
        self.clock = pg.time.Clock()
        self.loadAsset('basic')
        self.loadAsset('map')
        self.firstwindow()
        
    def loadAsset(self,assetType):
        # make list of image. where image will be store
        address = {}
        if assetType == 'basic':
            
            
            # make empty local dict to store all file address wich already combine. 
            # make it in local cause i think this variabble doesn't need in global application
            
            
            # make class dict variablle to store all image will be loaded
            self.listofImage = {}
            
            # Join file name with directory address
            address = {imageName : os.path.join(imgFolder,listimage[imageName]) for imageName in listimage}
            
            self.listofImage = {name : pg.image.load(address[name]).convert_alpha() for name in address}
            """======================LOAD TILESET ================================"""
        if assetType == 'tileset':
            self.listofTile = {}
            address = {tileName : os.path.join(tileFolder,listtile[tileName]) for tileName in listtile}
        
        if assetType == 'map':
            '''================ LOAD MAP FILE FROM MAP DATA ==============='''
            #createEmptyMap()
            self.mapData = Map.load('tes.map')
            
                    
    def firstwindow(self):
        # fisrt window to come update
        # maybe menu or splashscreen
        #self.newSouldier = souldier(self,sldrType = 'Archer',sldrRank = 2, sldrRace = #'Minang')
        #self.oldSouldier = souldier(self,sldrType = 'SwordMan',sldrRank = 2, sldrRace = #'Minang')
        self.camera = Camera(WIDTH, HEIGHT)
        self.banner = Item(self)
        self.Player = Player(self)
        self.Player.place(WIDTH/2,HEIGHT/2)
        self.run()
        str()
        
    def run(self):
        while self.Running:
            self.dt = self.clock.tick(FPS) / 100
            if debugFPS:
                print('FPS: ',1/(self.dt),'\tDt: ',self.dt)
            self.event()
            self.update()
            self.draw()
        # game loop
      
    def update(self):
        # game loop - update
        self.tileSize = int(self.scale*TILESIZE)
        self.camera.update(self.Player)
        self.offset =  Vector2D(self.camera.getPos())
        self.allDrawSprite.update()
        self.allDrawTileset.update()
    def event(self):
        # read all event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.Running = False
            if event.type == pg.KEYDOWN:
                """================ FOR EASY QUIT ================="""
                if event.key == pg.K_ESCAPE:
                    self.Running = False
                if event.key == pg.K_p:
                    if self.gameType == 'battlefield':
                        self.gameType = 'drawTile'
                    elif self.gameType == 'drawTile':
                        self.gameType = 'battlefield'
                # if event.key == pg.ESC
            if self.gameType == 'battlefield':
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.Player.speed = -1
                    if event.key == pg.K_s:
                        self.Player.speed = 1
                    if event.key == pg.K_a:
                        self.Player.steer = -1
                    if event.key == pg.K_d:
                        self.Player.steer = 1
                if event.type == pg.KEYUP:
                    if event.key == pg.K_d or event.key == pg.K_a:
                        self.Player.steer = 0
                    if event.key == pg.K_w or event.key == pg.K_s:
                        self.Player.speed = 0
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.banner.Place(event.pos-self.offset)
                        self.Player.moveTo(self.banner)
                    if (event.button == 5) and (self.scale<SCROLLMAX):
                        self.scale += 0.1
                    if (event.button == 4) and (self.scale>SCROLLMIN):
                        self.scale -= 0.1
            if self.gameType == 'drawTile':
                pass
    def draw(self):
        # Game Loop - Draw
        self.screen.fill(DARKGREEN)
        if DRAWGRID:
            self.drawGrid()
            
        for sprite in self.allDrawTileset:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        for sprite in self.allDrawSprite:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # self.allDrawTileset.draw(self.screen)
        # self.allDrawSprite.draw(self.screen)
        pg.display.flip()
    def drawGrid(self):
        for x in range(0, WIDTH, self.tileSize):
            pg.draw.line(self.screen, WHITE, (x+(self.offset.x%self.tileSize), 0), (x+(self.offset.x%self.tileSize), HEIGHT))
        for y in range(0, HEIGHT, self.tileSize):
            pg.draw.line(self.screen, WHITE, (0, y+(self.offset.y%self.tileSize)), (WIDTH, y+(self.offset.y%self.tileSize)))



def createEmptyMap(name = 'tes', tesMode = True):
    stringEmptyMap = ''
    if not tesMode:
        for j in range(96):
            stringEmptyMap += ('00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,;00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,;00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,')
            stringEmptyMap += ';'
    elif tesMode:
        for i in range(16):
            for j in range(16):
                stringEmptyMap += '00'
                stringEmptyMap += ','
            stringEmptyMap += ';'
    name +='.map'
    with open(os.path.join(mapFolder, name), 'wt') as f:
        f.write(str(stringEmptyMap))
        
if __name__ == '__main__':
    g = Game()
    pg.quit()
