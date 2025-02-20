from turtle import Screen, Turtle
from snake import Snake
import time

GAME_SPEED = 0.05

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake")
# Stops the screen from performing its normal rendering and animations
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

game_running = True
while game_running:
    # Delays the next render and code processing by 1 second
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()




screen.exitonclick()