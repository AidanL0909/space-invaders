import stddraw
import math
import time
from bullet import Bullet

class ship:

    def __init__(self):
        self.x = 0.5
        self.y = 0.1
        self.speed = 0.05
        self.rad = 0.1
        self.turAng = 0
        self.turSpeed = 0.1
        self.turlen = 0.15
        self.turwid = 0.01
        self.bullets = []
        self.score = 0

    def draw(self):
        stddraw.setPenColor(stddraw.RED)
        stddraw.filledCircle(self.x,self.y,self.rad)
        stddraw.setPenRadius(self.turwid)
        stddraw.setPenColor(stddraw.BLUE)

        endX = self.x + self.turlen * math.sin(self.turAng)
        endY = self.y + self.turlen * math.cos(self.turAng)

        stddraw.line(self.x,self.y,endX,endY)

        for i in self.bullets:
            i.draw()
        stddraw.text(0.9,0.9,f"Score = {self.score}")
        stddraw.show(0)

    def moveLeft(self):
        self.x -= self.speed
        if self.x < self.rad:
            self.x = self.rad

    def moveRight(self):
        self.x += self.speed
        if self.x > 1 - self.rad:
            self.x = 1 - self.rad

    def turLeft(self):
        self.turAng -= self.turSpeed
        if self.turAng < -0.5*math.pi:
            self.turAng = -0.5*math.pi

    def turRight(self):
        self.turAng += self.turSpeed
        if self.turAng > 0.5*math.pi:
            self.turAng = 0.5*math.pi

    def shoot(self):
        startX = self.x
        startY = self.y
        turretTX = startX + self.turlen * math.sin(self.turAng)
        turretTY = startY + self.turlen * math.cos(self.turAng)
        i = Bullet(turretTX, turretTY, self.turAng)
        self.bullets.append(i)

    def updateBullets(self, enemies):
        for i in self.bullets[:]:  
            i.newP()
            if not i.going:
                self.bullets.remove(i)
                continue
            for enemy in enemies[:]:
                if enemy.active and i.going and enemy.check_collision(i):
                    enemy.active = False
                    i.going = False
                    self.bullets.remove(i)
                    self.score += 1
                    break 
    
            
            
            

