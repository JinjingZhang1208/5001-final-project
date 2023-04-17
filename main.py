"""
--------------------------
Final Project: Snake Game

In order to keep playing , snake should not hit the wall or hit its body part.
--------------------------
STUDENT: Jinjing Zhang
SEMESTER: Spring 2023
"""
from turtle import Screen
from elements import Snake, Food
from score_manager import Score
import time
import sys


def play_again():
    """Ask the user if they want to play again"""
    screen = Screen()
    screen.listen()
    while True:
        play = screen.textinput("Game Over", "Do you want to play again? enter Y to continue, others exit").lower()
        if play == "y":
            screen.clear()
            main()
        else:
            sys.exit()


def hit_the_wall(snake_head_x, snake_head_y):
    """check to see if snake hits the wall. End the game and ask user if they want to play again if hits the wall."""
    if snake_head_x > 380 or snake_head_x < -380 or snake_head_y > 330 or snake_head_y < -330:
        return True


def main():
    """main function that execute all functions and set the game page"""
    screen = Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.title("Snake Game👻")
    # turn animation off
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_over = False
    while not game_over:
        # turn the animation on
        screen.update()
        # Suspend execution for 0.1 second
        time.sleep(0.1)
        snake.move()

        # add the snake size and add score when it eats a food target
        if snake.snake_body[0].distance(food) < 15:
            food.replenish_food()
            snake.enlarge()
            score.add_score()

        # check to see if we need to update the best score when hit the wall and ask the user if he wants to play again
        if hit_the_wall(snake.snake_body[0].xcor(), snake.snake_body[0].ycor()):
            score.reset()
            play_again()

        # check to see if we need to update the best score when hit the snake body itself and ask the user
        # if they want to play again
        for snake_body in snake.snake_body[1:]:
            if snake.snake_body[0].distance(snake_body) < 10:
                score.reset()
                play_again()

    screen.exitonclick()


if __name__ == "__main__":
    main()
