import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
GREEN = (0, 200, 0)

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.5
jump_strength = -8

pipes = []
pipe_width = 60
pipe_gap = 150
pipe_speed = 3
score = 0

def create_pipe():
    top_height = random.randint(100, 300)
    return [WIDTH, top_height]

running = True
pipes.append(create_pipe())

while running:
    clock.tick(60)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_vel = jump_strength

    bird_y += bird_vel
    bird_vel += gravity

    # Bird
    pygame.draw.circle(win, BLUE, (80, int(bird_y)), 20)

    # Pipes
    for pipe in pipes:
        pipe[0] -= pipe_speed
        pygame.draw.rect(win, GREEN, (pipe[0], 0, pipe_width, pipe[1]))
        pygame.draw.rect(win, GREEN, (pipe[0], pipe[1] + pipe_gap, pipe_width, HEIGHT - pipe[1] - pipe_gap))

        if pipe[0] + pipe_width == 80:
            score += 1

    # Remove off-screen pipes
    if pipes[0][0] < -pipe_width:
        pipes.pop(0)
    if pipes[-1][0] < WIDTH - 200:
        pipes.append(create_pipe())

    # Score
    text = font.render(str(score), True, (0, 0, 0))
    win.blit(text, (WIDTH // 2, 50))

    # Collision
    for pipe in pipes:
        if 80 + 20 > pipe[0] and 80 - 20 < pipe[0] + pipe_width:
            if bird_y - 20 < pipe[1] or bird_y + 20 > pipe[1] + pipe_gap:
                print("Game Over")
                running = False

    if bird_y > HEIGHT or bird_y < 0:
        print("Game Over")
        running = False

    pygame.display.update()

pygame.quit()
