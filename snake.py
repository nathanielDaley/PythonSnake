from turtle import Turtle

SNAKE_TURTLES_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

class Snake:
    def __init__(self):
        self.snake_turtles = []
        self.create_snake()
        self.snake_head = self.snake_turtles[0]

    def create_snake(self):
        for position in SNAKE_TURTLES_STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake, position is where to place the new segment"""
        tim = Turtle("square")
        tim.speed("fastest")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake_turtles.append(tim)

    def extend(self):
        """extends the snake by adding a new segment at the current last segments position"""
        # we can put it at the last segments position because the movement function will make sure the snake "extends"
        self.add_segment(self.snake_turtles[-1].position())

    def move(self):
        # This loop makes the "tail"(all snake turtles except the last) follow the "head"(the last snake turtle)
        # range("start index", "last index", "step  distance") !note last index is not inclusive
        for snake_num in range(len(self.snake_turtles) - 1, 0, -1):
            next_snake = self.snake_turtles[snake_num - 1]
            new_x_coordinate = next_snake.xcor()
            new_y_coordinate = next_snake.ycor()

            self.snake_turtles[snake_num].goto(new_x_coordinate, new_y_coordinate)

        # moves the "head" forward
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
