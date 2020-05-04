import pygame as pg
vec2 = pg.math.Vector2

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.target = vec2(0,0)

    def apply(self, entity):
        # entity  =  ,ove backgorund!
        # move the entity relatif to target
        return entity.rect.move(self.camera.topleft)
        
    def makeFocus(self):
        self.focus = pg.Rect((self.width//2), (self.height//2),10,10)
        return self.focus
    
    def moveSmooth(self, x, y, speed):
        if self.target == vec2(0,0):
            self.speed = speed
            self.target =  vec2(x,y)
            # self.focus = self.focus.move(x,y)
    
    def update(self, target , dt):
        if target == self.focus:
            if self.target != vec2(0,0):
                self.steer = self.target.normalize()*self.speed*dt*5
                if self.target.length() > self.steer.length():
                    self.focus = self.focus.move(self.steer.x, self.steer.y)
                    self.target -= self.steer
                elif self.target.length() <= self.steer.length():
                    self.focus = self.focus.move(self.target.x, self.target.y)
                    self.target = vec2(0,0)
                else:
                    print('unkwon error')
        # draw target in mid
        if type(target) == object:
            x = -target.rect.x + (self.width // 2)
            y = -target.rect.y + (self.height // 2)
        elif type(target) == pg.math.Vector2:
            x = -target.x + int(self.width / 2)
            y = -target.y + int(self.height / 2)
        elif type(target) == pg.Rect:
            x = -target.x + int(self.width / 2)
            y = -target.y + int(self.height / 2)
        else:
            print('new Type : ', type(target))

        self.camera = pg.Rect(x, y, self.width, self.height)
        
    def getPos(self):
        return self.camera.x, self.camera.y