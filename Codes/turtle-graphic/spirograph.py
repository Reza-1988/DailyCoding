import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.pensize(5)
tim.speed("fastest")

sides = [0, 90, 180, 270]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def spirograph(size_graph):
    for _ in range(360 // size_graph):
        tim.color(random_colour())
        tim.setheading(tim.heading() + size_graph)
        tim.circle(100)

spirograph(10)

screen = t.Screen()
screen.exitonclick()