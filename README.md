# Snake-py
This code is a simple implementation of the classic Snake game using the Pygame library in Python.

The game is played on a rectangular game window with dimensions of 600x400 pixels. The snake moves around the game window and eats food, which makes it grow longer. If the snake collides with itself or with the boundaries of the game window, the game is over.

The code initializes Pygame and sets up the game window dimensions and title. It also defines colors for the snake, food, and background. The font style and sizes for displaying the score and game over message are set using the SysFont method.

The main game loop is defined in the function game_loop(). The loop continually checks for user input to change the direction of the snake's movement, updates the position of the snake and the food, and redraws the screen. The function draw_snake() is called to draw the snake on the screen using a list of the snake's body positions.

If the snake collides with itself or the screen boundaries, the game is over. The function game_over_screen() is called to display the game over message and the final score. After a two-second delay, the program exits.

The game can be started by calling the game_loop() function from outside of the function definition, which starts the game loop and runs the game. was made with python and the pygame library. The code works by
