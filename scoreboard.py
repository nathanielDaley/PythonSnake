from logging import exception
from turtle import Turtle


INITIAL_X_POSITION = 0
INITIAL_Y_POSITION = 260
GAME_OVER_X_POSITION = 0
GAME_OVER_Y_POSITION = 0
GAME_OVER_TEXT = "GAME OVER"
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
COLOR = "white"
INITIAL_SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = INITIAL_SCORE
        self.high_score = self.get_high_score_from_file()
        self.hideturtle()
        self.color(COLOR)
        self.penup()
        self.goto(INITIAL_X_POSITION, INITIAL_Y_POSITION)
        self.write_score()

    def increase_score(self):
        """adds one to the score"""
        self.score += 1
        self.write_score()

    def write_score(self):
        """writes the score to the screen"""
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_file()
        self.score = 0
        self.write_score()

    def get_high_score_from_file(self):
        try:
            with open("data.txt") as file:
                score_from_file = file.read()
                if score_from_file == "":
                    return 0
                return int(score_from_file)
        except Exception as e:
            return 0

    def write_high_score_to_file(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))