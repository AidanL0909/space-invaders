import stddraw
import math
import time 
from shooter import ShooterMovement
from bullets import BulletMovement
from enemies import Enemies

stddraw.setCanvasSize(800, 600) 
stddraw.setXscale(0,100)
stddraw.setYscale(0,100)

shooter = ShooterMovement()
score = 0
userquit = False

bulletsarr = []

def createEnemies():
    enemiesarr = []
    rows = 3
    coloumns = 6
    xstart = 20
    ystart = 90
    xspaces = 10
    yspaces = 10
    

    for i in range(rows):
        for j in range(coloumns):
            x = xstart + j * xspaces
            y = ystart - i * yspaces
            enemiesarr.append(Enemies(x,y))
    return enemiesarr

enemiesarr = createEnemies()

while not userquit:
    while stddraw.hasNextKeyTyped():
        uinput = stddraw.nextKeyTyped().lower()

        if uinput == "a":
            shooter.moveleft()  
        elif uinput == "d":
            shooter.moveright() 
        elif uinput == "s":
            shooter.stopmoving()  
        elif uinput == "e":
            shooter.rotateright()  
        elif uinput == "q":
            shooter.rotateleft()    
        elif uinput == "w":
            shooter.stoprotating()
        elif uinput == "x":
            userquit = True
        elif uinput == "p":
            radians = math.radians(shooter.angle)
            xbullet = shooter.x + shooter.linelength * math.cos(radians)
            ybullet = shooter.y + shooter.linelength * math.sin(radians)
            bulletsarr.append(BulletMovement(xbullet,ybullet,shooter.angle))


        
    directionchange = False
    for i in enemiesarr:
        i.enemyMovement()
        if i.x + i.size >= 100 or i.x - i.size <= 0:
            directionchange = True

    if directionchange:
        for i in enemiesarr:
           i.down() 

    
    shooter.shooterMovement()


    for i in bulletsarr[:]:
        i.bulletMovement()
        if i.offScreen():
            bulletsarr.remove(i)
    

    for i in bulletsarr[:]:
        for j in enemiesarr[:]:
            dx = i.x - j.x
            dy = i.y - j.y
            distance = (dx**2 + dy**2) ** 0.5 
            if distance < i.radius + j.size:
                bulletsarr.remove(i)
                enemiesarr.remove(j)
                score += 1

    
    for i in enemiesarr:
        dx = shooter.x - i.x
        dy = shooter.y - i.y
        distance = (dx**2 + dy**2)** 0.5
        if distance < shooter.size + i.size:
            stddraw.clear(stddraw.BLACK)
            stddraw.setFontSize(24)
            stddraw.text(50, 50, "Game Over")

            stddraw.setFontSize(18)
            stddraw.text(30,30, " Restarting in 5 seconds") 

            stddraw.show()
            time.sleep(5)

            shooter = ShooterMovement()
            bulletsarr = []
            enemiesarr = createEnemies()
            score = 0
            break
    


    stddraw.clear(stddraw.BLACK)
    shooter.drawshooter()

    for i in bulletsarr:
        i.drawBullets()

    for i in enemiesarr:
        i.drawEnemies()
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setFontSize(12)
    stddraw.text(5,98, f"Score: {score}")
    stddraw.show(1)
    time.sleep(0.01)
        
