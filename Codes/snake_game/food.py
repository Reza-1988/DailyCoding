from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_random = random.randint(-280, 280)
        y_random = random.randint(-280, 280)
        self.goto(x=x_random, y=y_random)
