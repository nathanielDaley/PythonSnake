from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# how ofter the screen renders in seconds - higher is slower
GAME_SPEED = 0.1

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

# Create a piece of food for the snake to try to eat
food = Food()

scoreboard = Scoreboard()
scoreboard.write_score()

game_running = True
while game_running:
    # Delays the next render and code processing by 1 second
    screen.update()
    time.sleep(GAME_SPEED)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 1:
        food.move()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if(snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -290 or
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for turtle in snake.snake_turtles[1:]:
        if snake.snake_head.distance(turtle) < .1:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()