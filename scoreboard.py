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
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """writes game over in the middle of the screen"""
        self.goto(GAME_OVER_X_POSITION, GAME_OVER_Y_POSITION)
        self.write(GAME_OVER_TEXT, align=ALIGNMENT, font=FONT)