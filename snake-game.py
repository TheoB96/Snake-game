import pygame
import sys
import random

# Window size
WIDTH = 400
HEIGHT = 400

# Snake block size
BLOCK_SIZE = 20

# FPS
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Set up the clock
clock = pygame.time.Clock()

# Initialize the snake
snake = [(200, 200)]

# Initialize the apple
apple = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)

# Initialize the direction
direction = (0, -1)

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        # Quit if the player closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Change the direction of the snake based on the keys the player presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)

    # Move the snake
    snake.insert(0, (snake[0][0] + direction[0] * BLOCK_SIZE, snake[0][1] + direction[1] * BLOCK_SIZE))

    # Check if the snake has run into a wall or itself
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or snake[0][1] < 0 or snake[0][1] >= HEIGHT or snake[0] in snake[1:]):
        pygame.quit()
        sys.exit()

    # Check if the snake has eaten the apple
    if snake[0] == apple:
        # Generate a new apple
        apple = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        # Remove the tail of the snake
        snake.pop()

    # Clear the window
    window.fill(BLACK)

    # Draw the snake and the apple
    for block in snake:
        pygame.draw.rect(window, GREEN, pygame)
