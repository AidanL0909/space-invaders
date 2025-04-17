
import stddraw
import math

class Enemies:

    def __init__(self,x,y,speed = 0.005):
        
        self.x = x
        self.y = y
        self.active = True
        self.speed = speed
        self.rad = 0.05

    def update(self):
        self.y -= self.speed
        if self.y < 0 or self.y > 1:
            self.active = False

    def draw(self):
        if self.active:
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.filledCircle(self.x, self.y, self.rad)

    def check_collision(self, bullet):
        distance = math.sqrt((self.x - bullet.x) ** 2 + (self.y - bullet.y) ** 2)
        return distance < (self.rad + bullet.rad)

