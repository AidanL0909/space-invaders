import stdio
import stddraw
from Ship import ship
from enemies import Enemies
import time

def menu():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1)
    stddraw.setFontSize(22)
    stddraw.text(0.5,0.8,"PRESS SPACE KEY TO START")
    stddraw.setFontSize(16)
    stddraw.text(0.5,0.5,"[a] to go left, [d] to go right, [q] turret left, [e] turret right, [space] to shoot")
    return stddraw.show(0)

def help():
    stddraw.clear(stddraw.BLACK)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.setXscale(0,1)
    stddraw.setYscale(0,1)
    stddraw.setFontSize(22)
    stddraw.text(0.5,0.8,"PAUSED")
    stddraw.setFontSize(16)
    stddraw.text(0.5,0.5,"[a] to go left, [d] to go right, [q] turret left, [e] turret right, [space] to shoot")
    stddraw.text(0.5,0.2, "Press [p] to unpause")
    stddraw.text(0.5,0.1, "Press [v] to quit")
    return stddraw.show(0)


def main():

    Ship = ship()

    menu()

    while True:
        if stddraw.hasNextKeyTyped():
            i = stddraw.nextKeyTyped()
            if i == ' ':   
                stddraw.clear(stddraw.BLACK)  
                Ship.draw()
                break
                
            
        stddraw.show(10) 

    
    enemies = []
    last_enemy_spawn = time.time()
    spawn_interval = 2.0 

    paused = False
    while True:
        stddraw.clear(stddraw.BLACK)

        current_time = time.time()
        
        if current_time - last_enemy_spawn >= spawn_interval:
            enemies.append(Enemies(x=0.1, y=0.9))
            last_enemy_spawn = current_time

        if stddraw.hasNextKeyTyped():
            i = stddraw.nextKeyTyped()

            if i == 'p':
                paused = not paused

            if i == 'v':
                break

            elif not paused:

                if i == 'a':   
                    Ship.moveLeft()

                elif i == 'd':
                    Ship.moveRight()

                elif i == 'q':
                    Ship.turLeft() 

                elif i == 'e':
                    Ship.turRight()

                elif i == ' ':
                    Ship.shoot()
        if paused:
            help()
            continue
        Ship.updateBullets(enemies)
    

        for enemy in enemies[:]:
            enemy.update()
            if not enemy.active:
                enemies.remove(enemy)
            else:
                enemy.draw()

        

        
        Ship.draw()   
        stddraw.show(10) 
        
                        

        
        
        


    



if __name__ == "__main__":main()


