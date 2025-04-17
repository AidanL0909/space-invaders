import stddraw
import time 
import math 

class ShooterMovement:
    def __init__(self):
        self.x = 50
        self.y = 10
        self.size = 5
        self.speed = 0.5
        self.direction = 0 # -1: Left, 0: Stop moving, 1: Right
        self.angle = 90 # The shooter line starts at the vertical position of 90 degrees
        self.angulardirection = 0 # -1: Rotate left, 0: Stop rotating, 1: Rotate right
        self.linelength = 15

    def shooterMovement(self):
        if self.direction == -1 and self.x > self.size:
            self.x -= self.speed
        if self.direction == 1 and self.x < 100-self.size:
            self.x += self.speed

        if self.angulardirection == 1 and self.angle < 180:
            self.angle += self.speed*2
        if self.angulardirection == -1 and self.angle > 0:
            self.angle -= self.speed*2

    def drawshooter(self):
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledCircle(self.x, self.y, self.size)
        radians = math.radians(self.angle)
        endlinex = self.x + self.linelength * math.cos(radians)
        endliney = self.y + self.linelength * math.sin(radians)
        stddraw.setPenColor(stddraw.WHITE)
        stddraw.line(self.x, self.y, endlinex, endliney)


    def moveleft(self):
        self.direction = -1    
    def moveright(self):
        self.direction = 1
    def stopmoving(self):
        self.direction = 0
    def rotateleft(self):
        self.angulardirection = 1
    def rotateright(self):
        self.angulardirection = -1
    def stoprotating(self):
        self.angulardirection = 0
