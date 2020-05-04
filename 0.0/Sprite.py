# import python module
import pygame as pg
Vector2D = pg.math.Vector2

# import local module
from config import *

debug1 = 0

class souldier(pg.sprite.Sprite):
    # Get souldier type, rank and race
    def __init__(self, Game, sldrType = None, sldrRank = None ,sldrRace = None): 
        pg.sprite.Sprite.__init__(self)
        self.imageOriginal = Game.listofImage[sldrType]
        self.image = self.imageOriginal
        self.rect = self.imageOriginal.get_rect()
        self.game = Game
        self.sldrType = sldrType
        self.sldrRace = sldrRace
        self.sldrRank = sldrRank
        self.calculateOtherTraits()
        """========================= define Useble Variable =========================="""
        self.targetCoordinat = None
        self.targetAngle = None
        self.direction = Vector2D(1,0)
        self.position = Vector2D(0,0)
        self.steer =  0
        
        self.speed = 0
        '''
        self.swicth = {'HorseAcher':self.charge,
                  'HorseSword':self.charge,
                  'Tanker':self.shieldWall
                  }
        '''
    def place(self,x=None,y=None):
        # if data x is Vector
        if type(x) == Vector2D:
            self.position = x
        elif (type(x) == tuple) and (len(x) == 2):
            self.position = Vector2D(x)
        # data x,y is regular number
        elif (x!=None) and (y!=None):
            self.position = Vector2D(x,y)
        self.game.allDrawSprite.add(self)
            
    def calculateOtherTraits(self):
        # Calcutalation aal trairrts the soulder maght be have
        self.maxHealth = 100        # maximum health 
        self.maxStamina = 100       # maximum stamina
        self.power = 100            # 
        self.defRange = 50
        self.defMele = 100
        self.atkRange = 0
        self.atkMele = 12
        self.moral = 100
        self.solidMovement = 20
        self.moveSpeed = 16
        self.turnSpeed = 30
        self.hidingSkill = 10
        self.push = 50
        self.weight = 120
        self.tier = 3
        self.buildCost = 5300
        self.upKeep = 3500
        self.warKeep = 4000
        
    def rotate(self, steer):
        steer = steer*self.turnSpeed*self.game.dt
        self.direction = self.direction.rotate(steer)
        
        
    def moveTo(self, target):
        self.target = target
        self.targetCoordinat = cekCoordinatType(target)
        self.targerDirection = (self.position -  self.targetCoordinat).normalize()
        self.targetAngle = self.direction.angle_to(self.targerDirection)
        
    def collide_with_solid(self):
        pass
        
    def update(self):
        if debug1:
            print('target: ' ,self.targetCoordinat, '\t\tself.pos: ',self.position)
            print('angle: ' ,self.targetAngle, '\tself.dir: ',self.direction)
            print('==============================================================\n\n\n\n')
    
        self.rotate(self.steer)
        self.direction = self.direction.normalize()
        self.angle = Vector2D.as_polar(self.direction)[1]
        self.position += self.direction*self.speed*self.moveSpeed*self.game.dt
        self.image = pg.transform.rotozoom(self.imageOriginal, 
                                           -self.angle, self.game.scale)
        self.rect = self.image.get_rect()
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)
        
    def charge(self):
        pass
    
    def shieldWall(self):
        pass
        
        
class Player(souldier):
    def __init__(self,Game):
        self.game = Game
        souldier.__init__(self, self.game, sldrType = 'HorseSword',sldrRank = 2, sldrRace = 'Minang')
        self.place(WIDTH/2,HEIGHT/2)
        
class Item(pg.sprite.Sprite):
    def __init__(self,Game, x = None, y = None, itemType = 'Banner', itemCode = '1'):
        pg.sprite.Sprite.__init__(self)
        self.game = Game
        itemName = itemType+itemCode
        self.image = self.game.listofImage[itemName]
        self.rect = self.image.get_rect()
        self.getItemPlacementType(itemType)
    
    '''========== Get Placement Type =========='''
    def getItemPlacementType(self,itemType):
        if itemType == 'Banner':
            pass
    
    def Place(self,x = None, y = None):
        '''========== Get Koordinat =========='''
        self.position = cekCoordinatType(x,y)
        '''========== Place the Item in Exact Koordinat =========='''
        self.rect.midbottom = self.position
        self.game.allDrawSprite.add(self)
        
""" ======================= ADitional Function ======================="""
def cekCoordinatType(x = None, y = None):
    coordinat = Vector2D()
    """
    ''' ============ Debugging porpose ============ '''
    try:
        print(pg.sprite.Sprite in x.__class__.__mro__)
    except:
        pass
    """
    if type(x) == Vector2D:
        coordinat = x
    elif (type(x) == tuple) and (len(x) == 2):
        coordinat = Vector2D(x)
    # data x,y is regular number
    elif (x!=None) and (y!=None):
        coordinat = Vector2D(x,y)
    # elif x == pg.sprite.Sprite:
    elif pg.sprite.Sprite in x.__class__.__mro__:
        coordinat = x.position
    
    return coordinat
        
# end