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
main.py - run main.py to play the game
elements.py - class Snake, class Food located here
score_manager.py - class Score, save_best_score_to_file, load_best_score_from_file located here
data.txt - file used to track the best_score, dafault to 0
test_elements.py - unitest the class Snake, class Food
test_score.py - test save_best_score_to_file, load_best_score_from_file functions. class Score can be checked by playing the game.
