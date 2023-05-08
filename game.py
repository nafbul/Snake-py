import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the window dimensions
window_width = 600
window_height = 400

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Set the font
font_style = pygame.font.SysFont(None, 50)


def display_score(score):
    # Create a font object for displaying the score
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: " + str(score), True, black)
    game_window.blit(score_text, [0, 0])


def draw_snake(snake_block_size, snake_list):
    # Draw the snake on the screen
    for x in snake_list:
        pygame.draw.rect(game_window, black, [x[0], x[1], snake_block_size, snake_block_size])


def game_over_screen(score):
    # Create a font object for displaying the game over message
    game_over_font = pygame.font.SysFont(None, 50)
    game_over_text = game_over_font.render("Game Over", True, black)

    # Create a font object for displaying the score
    score_font = pygame.font.SysFont(None, 30)
    score_text = score_font.render("Score: " + str(score), True, black)

    # Display the game over message and score on the screen
    game_window.blit(game_over_text, [window_width / 2 - game_over_text.get_width() / 2, 100])
    game_window.blit(score_text, [window_width / 2 - score_text.get_width() / 2, 200])

    # Update the screen
    pygame.display.update()


def game_loop():
    # Set the game variables
    game_over = False
    game_close = False
    x1 = window_width / 2
    y1 = window_height / 2
    snake_block_size = 10
    x1_change = 0
    y1_change = 0
    snake_list = []
    snake_length = 1
    snake_speed = 15
    foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
    score = 0

    # Set the clock
    clock = pygame.time.Clock()

    # Start the game loop
    while not game_over:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Update the snake's position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake has collided with the food
        if x1 == foodx and             y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            snake_length += 1
            score += 10
            snake_speed += 0.5

        # Fill the screen with white color
        game_window.fill(white)

        # Draw the food on the screen
        pygame.draw.rect(game_window, green, [foodx, foody, snake_block_size, snake_block_size])

        # Update the snake's position
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake has collided with itself or with the screen's boundaries
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        if x1 < 0 or x1 >= window_width or y1 < 0 or y1 >= window_height:
            game_close = True

        # Draw the snake on the screen
        draw_snake(snake_block_size, snake_list)

        # Display the score on the screen
        display_score(score)

        # Update the screen
        pygame.display.update()

        # Check if the game is over
        if game_close:
            game_over_screen(score)
            time.sleep(2)
            game_over = True

        # Set the speed of the game
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()

    # Quit the program
    quit()

# Set the window dimensions and title
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Start the game loop
game_loop()

