# 5001-final-project
Snake Game


Introduction:

This is a classic Snake game where the player controls a snake on the screen. The objective is to score points by letting the snake eat food that randomly appears on the screen. There is no limit to the amount of food that can be eaten.

However, the game will be over if the snake hits the wall or its own body. The challenging part of the game is that the snake's body length increases as the player scores more points.

The game records the player's current score and displays it on the screen. Additionally, the game also stores the player's best score in a file.



How to Play:

Use the arrow keys to control the snake's movement: up, down, left, and right.

The snake will move in the direction of the last arrow key pressed.

Eat as much food as possible to increase your score.

Avoid hitting the wall or the snake's body, or the game will be over.



Files Explanations:

main.py: This file contains the main game logic and can be run to play the game.

elements.py: This file contains the Snake and Food classes, which are the properties of the game elements.

score_manager.py: This file contains the Score class, which manages the player's score during the game. 
It also includes functions to save the best score to a file and load the best score from a file. 
The file data.txt is used to store the best score, which defaults to 0.

test_elements.py: This file contains unit tests for the Snake and Food classes.

test_score.py: This file contains tests for the save_best_score_to_file and load_best_score_from_file functions in the Score class. 
Note that the Score class can be tested by playing the game.



Now it is time to challenge yourself! Have fun 👻👻👻
