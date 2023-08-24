### Snake Game


##Introduction:##

This is a classic Snake game where the player controls a snake on the screen. The objective is to score points by letting the snake eat food that randomly appears on the screen. There is no limit to the amount of food that can be eaten.

However, the game will be over if the snake hits the wall or its own body. The challenging part of the game is that the snake's body length increases as the player scores more points.

The game records the player's current score and displays it on the screen. Additionally, the game also stores the player's best score in a file.



## Files Overview

- `main.py`: Run this file to play the game and experience the core game logic.
- `elements.py`: Defines the Snake and Food classes, representing game elements.
- `score_manager.py`: Manages the player's score during the game, including saving and loading the best score. Best score is stored in `data.txt`.
- `test_elements.py`: Contains unit tests for the Snake and Food classes.
- `test_score.py`: Holds tests for the save_best_score_to_file and load_best_score_from_file functions in the Score class. You can also evaluate the Score class by playing the game.

## Getting Started

1. Run `main.py` to start the Snake game.
2. Use arrow keys for navigation.
3. Aim for the highest score and challenge yourself to improve!

Now it's time to dive in and have some fun! 👾🐍🎮

