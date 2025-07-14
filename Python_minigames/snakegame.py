import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

font = pygame.font.SysFont("Arial", 35)

def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [WIDTH // 6, HEIGHT // 3])

def gameLoop():
    game_over = False
    game_close = False

    x = WIDTH // 2
    y = HEIGHT // 2
    x_change = 0
    y_change = 0

    snake = []
    length = 1

    food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill((0, 0, 0))
            message("Game Over! Press Q-Quit or C-Play Again", (255, 0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        win.fill((50, 150, 50))

        pygame.draw.rect(win, (255, 0, 0), [food_x, food_y, snake_block, snake_block])

        head = []
        head.append(x)
        head.append(y)
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        for part in snake[:-1]:
            if part == head:
                game_close = True

        for block in snake:
            pygame.draw.rect(win, (0, 0, 255), [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
