import math
import stddraw

class Bullet:

    def __init__(self,x,y,a,speed = 0.01):

        self.x = x
        self.y = y
        self.sx = speed*math.sin(a)
        self.sy = speed*math.cos(a)
        self.rad = 0.01
        self.going = True

    def newP(self):

        self.x += self.sx
        self.y += self.sy

        if self.x < 0 or self.x > 1 or self.y < 0 or self.y > 1:
            self.going = False

    def draw(self):

        if self.going:
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.filledCircle(self.x, self.y, self.rad)