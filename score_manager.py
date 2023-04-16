"""
NAME: Jinjing Zhang
SEMESTER: spring 2023

score_manager includes score tracking (class Score), save_best_score_to_file, load_best_score_from_file
"""
from turtle import Turtle


class Score(Turtle):
    """
    class: Score (inherit Turtle)
    methods: update_score, add_score, reset
    """
    def __init__(self):
        """
        attributes:
        score:default to 0,
        best_score: loaded from the file,
        color: white
        """
        super().__init__()
        self.score = 0
        self.best_score = load_best_score_from_file("data.txt")
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """clear the screen first and print the current score and best score on the screen"""
        self.clear()
        self.write(f"Score: {self.score}    Best Score: {self.best_score}",
                   align='center', font=("Courier", 24, "normal"))

    def add_score(self):
        """add 1 point to the current score"""
        self.score += 1
        self.update_score()

    def reset(self):
        """update the best score and save it to the file if the current score is bigger than the
        best score recorded in the file"""
        if self.score > self.best_score:
            self.best_score = self.score
            save_best_score_to_file("data.txt", self.best_score)
        self.update_score()


def save_best_score_to_file(filename, best_score):
    """save the best_score to file"""
    with open(filename, 'w') as data:
        data.write(f'{best_score}')


def load_best_score_from_file(filename):
    """load the best_score recorded on the file"""
    with open(filename, 'r') as data:
        best_score = int(data.read())
        return best_score
