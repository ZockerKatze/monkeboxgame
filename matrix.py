import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Effect")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 30)

# Create columns for the "rain"
columns = WIDTH // 20
drops = [0] * columns

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the "Matrix" effect
    for i in range(columns):
        char = chr(random.randint(33, 126))  # Random printable characters
        char_surface = font.render(char, True, GREEN)
        x = i * 20
        y = drops[i] * 20
        screen.blit(char_surface, (x, y))

        # Reset drop to top of screen and keep scrolling down
        if drops[i] * 20 > HEIGHT or random.random() > 0.975:
            drops[i] = 0
        drops[i] += 1

    # Update the display
    pygame.display.flip()

    # Set frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
