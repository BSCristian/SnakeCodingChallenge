class Snake():
    def __init__(self):
        self.x = 50
        self.y = 50

        self.body = [(50, 50), (50, 40), (50,30), (50,20)]
        self.direction = "R"

    def move(self, foodPosition):
        if self.direction == "R": 
            self.x += 10

        if self.direction == "L":
            self.x -= 10

        if self.direction == "U":
            self.y -= 10

        if self.direction == "D":
            self.y += 10

        self.body.insert(0, (self.x, self.y))

        if self.x == foodPosition[0] and self.y == foodPosition[1]:
            return True

        self.body.pop()
        return False


    def changeDirection(self, newDirection):
        if newDirection == "R" and not self.direction == "L":
            self.direction = "R"

        if newDirection == "L" and not self.direction == "R":
            self.direction = "L"

        if newDirection == "U" and not self.direction == "D":
            self.direction = "U"

        if newDirection == "D" and not self.direction == "U":
            self.direction = "D"

    def checkDead(self):
        if self.x > 290 or self.x < 0 or self.y > 290 or self.y < 0:
            return True

        for bodyPart in self.body[1:]:
            if (self.x, self.y) == bodyPart:
                return True

        return False
