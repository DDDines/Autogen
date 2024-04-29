# filename: snake_game.py

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SNAKE_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_direction = (0, 0)

# Food initial position
food = (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE - 1) * SNAKE_SIZE, random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE - 1) * SNAKE_SIZE)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    snake_head = (snake[0][0] + snake_direction[0] * SNAKE_SIZE, snake[0][1] + snake_direction[1] * SNAKE_SIZE)
    snake.insert(0, snake_head)

    if snake_head == food:
        food = (random.randint(0, SCREEN_WIDTH // SNAKE_SIZE - 1) * SNAKE_SIZE, random.randint(0, SCREEN_HEIGHT // SNAKE_SIZE - 1) * SNAKE_SIZE)
    else:
        snake.pop()

    if snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT:
        running = False

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.draw.rect(screen, WHITE, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()