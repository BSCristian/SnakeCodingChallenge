import pygame
import sys
from snake import Snake
from food import Food


window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Serpilica")
fps = pygame.time.Clock()

score = 0

snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.changeDirection("R")
            if event.key == pygame.K_LEFT:
                snake.changeDirection("L")
            if event.key == pygame.K_UP:
                snake.changeDirection("U")
            if event.key == pygame.K_DOWN:
                snake.changeDirection("D")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    foodPosition = food.generateFood()

    if snake.move(foodPosition):
        score += 100
        food.setFoodEaten(True)

    window.fill(pygame.Color(241, 90, 33))

    for position in snake.body:
        pygame.draw.rect(window, pygame.Color(255,255,255), pygame.Rect(position[0], position[1], 10, 10))

    pygame.draw.rect(window, pygame.Color(0,123,255), pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))

    if snake.checkDead():
        pygame.quit()
        sys.exit()

    pygame.display.set_caption("Serpilica | Scor:" + str(score))
    pygame.display.flip()
    fps.tick(12)
