import random

class Food():
    def __init__(self):
       self.x = random.randrange(1, 30) * 10
       self.y = random.randrange(1, 30) * 10
       self.eaten = False
       
    
    def generateFood(self):
        if self.eaten:
            self.x = random.randrange(1, 30) * 10
            self.y = random.randrange(1, 30) * 10
            self.eaten = False

        return (self.x, self.y)

    def setFoodEaten(self, isEaten):
        self.eaten = isEaten

