import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up ball properties
ball_radius = 20
x, y = WIDTH // 2, HEIGHT // 2
vel_x, vel_y = 5, 3

# Set up clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    x += vel_x
    y += vel_y

    # Bounce off walls
    if x - ball_radius <= 0 or x + ball_radius >= WIDTH:
        vel_x *= -1
    if y - ball_radius <= 0 or y + ball_radius >= HEIGHT:
        vel_y *= -1

    # Draw everything
    win.fill(WHITE)
    pygame.draw.circle(win, RED, (x, y), ball_radius)
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
