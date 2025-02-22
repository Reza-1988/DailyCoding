from turtle import Turtle
MOVE_DISTANCE = 20
X_Y_STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for x_y in X_Y_STARTING_COORDINATES:
            self.add_square(x_y)


    def add_square(self, x_y):
       square = Turtle(shape="square")
       square.color("white")
       square.penup()
       square.goto(x_y)
       self.squares.append(square)


    def extend(self):
       self.add_square(self.squares[-1].position())



    def move(self):
        for square_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)