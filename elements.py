"""
NAME: Jinjing Zhang
SEMESTER: spring 2023

Game Elements including snake(class Snake) ，food(class Food)
"""
from turtle import Turtle
import random


class Snake:
    """
    class:Snake
    methods: add_body, build_snake, enlarge, move, left, right, up, down
    """
    def __init__(self):
        """self.snake_body default to an empty list"""
        self.snake_body = []
        self.build_snake()

    def add_body(self, point):
        """add new_body to snake_body"""
        # shape square default size 20*20
        new_body = Turtle(shape="square")
        new_body.color("white")
        new_body.penup()
        new_body.goto(point)
        self.snake_body.append(new_body)

    def build_snake(self):
        """build the snake body in the game, using add_body method"""
        # use tuples since starting_points are fixed
        starting_points = [(20, 0), (0, 0), (-20, 0)]
        for point in starting_points:
            self.add_body(point)

    def enlarge(self):
        """add one more body part into the snake_body"""
        # Turtle class position() to get the position of the last snake body's current position(point)
        self.add_body(self.snake_body[-1].position())

    def move(self):
        """use for loop to adjust the location of the snake_body, and move by 20"""
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def up(self):
        """up - 90 degree. Edge case: cannot turn opposite direction"""
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        """down - 270 degree. Edge case: cannot turn opposite direction"""
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        """left - 180 degree. Edge case: cannot turn opposite direction"""
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        """right - 0 degree. Edge case: cannot turn opposite direction"""
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def reset(self):
        """move the old snake_body out of the screen and reset a new snake_body """
        for body in self.snake_body:
            body.goto(1200, 1200)
        self.snake_body.clear()
        self.build_snake()


class Food(Turtle):
    """
    class: Food
    methods: replenish_food
    """
    def __init__(self):
        """Food class also inherit the Turtle class"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("orange")
        # shapesize of circle 20*20
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")
        self.replenish_food()

    def replenish_food(self):
        """create new food at a random point once the old one has been hit by the snake"""
        random_x = random.randint(-350, 350)
        random_y = random.randint(-330, 320)
        self.goto(random_x, random_y)
