import stddraw

class Enemies:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2.5
        self.speed= 0.3
        self.direction = 1

    def enemyMovement(self):
        self.x += self.speed * self.direction

    def down(self):
        self.y -= 4
        self.direction *= -1

    def drawEnemies(self):
        stddraw.setPenColor(stddraw.YELLOW)
        stddraw.filledSquare(self.x,self.y, self.size)
