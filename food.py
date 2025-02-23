import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.move()

    def move(self):
        """move the piece of food to a random place on screen"""
        random_x = random.randint(-14, 14)
        random_y = random.randint(-14, 14)
        self.goto(random_x * 20, random_y * 20)
