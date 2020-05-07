'''============================= IMPORT PYTHON MODULE ========================='''
import pygame as pg
import random
import os
vec2D = pg.math.Vector2

'''============================= IMPORT LOCAL MODULE ========================='''
from settings import *
from tools.decoration import *
from tools.sprite import *

debug0 = 0 # debug if mouse hover main menu
debug1 = 0 # debug camera

class mainMenu:
    def __init__(self, Game):

        self.game = Game
        self.isLoad = False
        self.isBegin = False
        
        
        self.mainButton = {}
        self.playButton = {}
        
        '''============================= DEFINE SPRITE GROUPS} ========================='''
        self.allMainMenuSprite = pg.sprite.Group()
        self.allPlayMenuSprite = pg.sprite.Group()
        
        self.isDraw = {'mainMenu' : False, 'playMenu' : False}
        self.choose = 'mainMenu'
        self.run = {'mainMenu': self.begin, 'playMenu': self.playMenu, 'exitGame':self.exitGame}
        
    def load(self):
        imageDir = os.path.join(self.game.mainDir,image,mainMenuImageDir)
        try:        
            address = {imageName : os.path.join(imageDir,mainMenuImageList[imageName]) 
                       for imageName in mainMenuImageList}
            
            self.liImage = {name : pg.image.load(address[name]).convert_alpha() 
                                for name in address}
            
            self.isLoad = True
        
        except Exception as e:
            self.Error = e
            print(e)
            self.isLoad = False
    def event(self):
        self.cekLoad()
        if self.isLoad and not self.isBegin:
            self.begin()
            
        # for i in self.mainButton:
            # self.mainButton[i].event(self.game.Camera)
        # for i in self.playButton:
            # self.playButton[i].event(self.game.Camera)
        
        
        # for sprite in self.allPlayMenuSprite:
            # sprite.event(self.game.Camera)
        # for sprite in self.allMainMenuSprite:
            # sprite.event(self.game.Camera)
            
        if pg.mouse.get_focused():
            mousePosition = pg.mouse.get_pos()
            hover = None
            if (self.choose == 'mainMenu') and (mousePosition[1]>self.game.height-(32*7)) and (mousePosition[0]>self.game.width - 32*6) :
                if pg.mouse.get_pressed()[0] and self.mainButton[0].hover:
                    self.choose = 'playMenu'
                    self.game.Camera.moveSmooth(-self.game.width,0,55)
                if pg.mouse.get_pressed()[0] and self.mainButton[3].hover:
                    self.choose = 'exitGame'
            if (self.choose == 'playMenu') and (mousePosition[1]> self.game.height-(32*7)) and (mousePosition[0] < 32*6):
                if pg.mouse.get_pressed()[0] and self.playButton[3].hover:
                    self.choose = 'mainMenu'
                    self.game.Camera.moveSmooth(self.game.width,0,55)
                if pg.mouse.get_pressed()[0] and self.playButton[0].hover:
                    self.game.runType = 'combatSystem'
                    self.destroy()
                
    def update(self):
        if self.game.runType == 'mainMenu':
            self.run[self.choose]()
            self.allPlayMenuSprite.update(self.game.Camera)
            self.allMainMenuSprite.update(self.game.Camera)
            # self.game.allDrawSprite.update()
            self.game.Camera.update(self.game.Camera.focus, self.game.dt)
        
        
        if debug1:
            message = self.game.Camera.getPos()
            print(message)
        
    def draw(self):
        self.game.screen.fill(RED)
        for sprite in self.allPlayMenuSprite:
            self.game.screen.blit(sprite.image, self.game.Camera.apply(sprite))
        for sprite in self.allMainMenuSprite:
            self.game.screen.blit(sprite.image, self.game.Camera.apply(sprite))
	
    def destroy(self):
        self.isLoad = False
        self.isBegin = False
        self.choose = 'mainMenu'
        self.listofImage = {}
        self.mainButton = []
        self.playButton = []
        # self.game.allDrawSprite.empty()
        self.allMainMenuSprite.empty()
        self.allPlayMenuSprite.empty()
    def cekLoad(self):
        if not self.isLoad:
            self.load()
    
    def begin(self):
        self.isBegin = True
        '''============================= DRAW MENU ========================='''
        if not self.isDraw['mainMenu']:
            text = ['Play', 'Settings', 'About', 'Exit']
            left = self.liImage['woodpointW']
            mid = self.liImage['woodmid']
            right = self.liImage['woodendE']
            image = self.liImage['woodmid']
            imageSize = image.get_size()
            for j in range(4):
                self.mainButton[j] = button()
                self.mainButton[j].setImage(left, mid, right)
                offset = random.randint(0,25)
                x = self.game.width-(imageSize[0]*6 + offset)
                y = int(self.game.height-(imageSize[0]*7))+(imageSize[0]*j*1.5)
                self.mainButton[j].makeButton(x, y, 6, text[j])
                self.allMainMenuSprite.add(self.mainButton[j])
                
            self.isDraw['mainMenu'] = True
            # self.game.allDrawSprite.add(self.allMainMenuSprite)
            
    def playMenu(self):
        if not self.isDraw['playMenu']:
            text = ['Combat System', 'Draw Map', 'Flocking', 'Back >>']
            left = self.liImage['woodendW']
            mid = self.liImage['woodmid']
            right = self.liImage['woodpointE']
            image = self.liImage['woodmid']
            imageSize = image.get_size()
            for j in range(4):
                self.playButton[j] = button()
                self.playButton[j].setImage(left, mid, right)
                offset = random.randint(0,25)
                x = -self.game.width-offset
                y = int(self.game.height-(imageSize[0]*7))+(imageSize[0]*j*1.5)
                self.playButton[j].makeButton(x, y, 6, text[j])
                self.allPlayMenuSprite.add(self.playButton[j])
            
            self.isDraw['playMenu'] = True
            # self.game.allDrawSprite.add(self.allPlayMenuSprite)
            
    def exitGame(self):
        self.destroy()
        self.game.Running = False
        
class flocking:
    def __init__(self):
        self.isLoad = False
        self.isBegin = False
        
    def begin(self):
        pass
		
    def load(self):
        pass
		
    def event(self):
        self.cekLoad()
        if self.isLoad and not self.isBegin:
            self.begin()
        
    def update(self):
        pass
	
    def draw(self):
        pass
	
    def changeAndDestroy(self):
        pass
	
    def cekLoad(self):
        if not self.isLoad:
            self.game.load('flocking')
        

class drawMap:
    def __init__(self):
        self.isLoad = False
        self.isBegin = False
		
    def begin(self):
        pass
        
    def load():
        pass
		
    def event(self):
        self.cekLoad()
        if self.isLoad and not self.isBegin:
            self.begin()
        
    def update(self):
        pass
	
    def draw(self):
        pass
	
    def changeAndDestroy(self):
        pass
	
    def cekLoad(self):
        if not self.isLoad:
            self.game.load('drawMap')

class combatSystem:
    def __init__(self, Game):
        self.isLoad = False
        self.isBegin = False
        self.game = Game
        self.screen = self.game.screen
        self.pause = False
        
        '''====================DEFINE SPRITE GROUPS==================='''
        self.allSpriteGroup = pg.sprite.Group()
        
    def begin(self):
        self.isBegin = True
        self.Player = Player(self)
        screenSize = self.screen.get_size()
        self.Player.position  = vec2D(screenSize[0]//2,screenSize[1]//2)
        self.allSpriteGroup.add(self.Player)
    def load(self):
        imageDir = os.path.join(self.game.mainDir,image,spriteImageDir)
        try:        
            address = {imageName : os.path.join(imageDir,spriteImageList[imageName]) 
                       for imageName in spriteImageList}
            
            self.spriteImageList = {name : pg.image.load(address[name]).convert_alpha() 
                                for name in address}
            self.isLoad = True
            
        except Exception as e:
            self.Error = e
            print(e)
            self.isLoad = False
            
    def event(self):
        self.cekLoad()
        # next itme we sould be break loopoing of failing in loading
        if self.isLoad and not self.isBegin:
            self.begin()
            
        self.pause = self.game.pause
        keys = pg.key.get_pressed()
        if not self.pause: # PLAY THE GAME
            arah  = vec2D(0,0)
            if keys[pg.K_w]:
                arah  += vec2D(0,-1)
            if keys[pg.K_s]:
                arah  += vec2D(0,1)
            if keys[pg.K_a]:
                arah  += vec2D(-1,0)
            if keys[pg.K_d]:
                arah  += vec2D(1,0)
            self.Player.moveVec = arah
                
        elif self.pause: # PAUSE THE GAME
            pass
    def update(self):
        
        if not self.pause:
            self.allSpriteGroup.update(self.game.Camera)
        elif self.pause:
            pass
	
    def draw(self):
        self.screen.fill(BLUE)
        '''
            even when game pause we still nedd to draw an lasted image to screen
        '''
        self.allSpriteGroup.draw(self.screen)
        if self.pause: # PAUSE THE GAME
            pass
            
    def destroy(self):
        self.allSpriteGroup.empty()
	
    def cekLoad(self):
        if not self.isLoad:
            self.load() 

class LoadingScreen:
    def __init__(self, Game):
        self.game = Game
        self.screen = self.game.screen
    def begin(self):
        pass
    def load(self):
        pass
        ''' MAYBE WE SUOOLD MOVE ALL LOAD DING FUNCTION TO HERE'''
    def event(self):
        pass
        
    def update(self):
        pass
	
    def draw(self):
        self.screen.fill(PINK)
        
    def destroy(self):
        pass
	
    def cekLoad(self):
        pass
