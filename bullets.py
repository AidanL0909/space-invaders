import stddraw
import math 

class BulletMovement:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.speed = 1.0
        self.radius = 1
        self.angle = math.radians(angle)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed 
    def bulletMovement(self):
        self.x += self.dx
        self.y += self.dy
    def drawBullets(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x,self.y, self.radius)
    def offScreen(self):
        return self.x < 0 or self.x > 100 or self.y > 100
