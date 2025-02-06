import turtle as t
import random


t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
tim.hideturtle()

color_list = [(132, 164, 202), (225, 150, 101), (30, 43, 64), (201, 135, 147), (163, 59, 49), (236, 212, 87),
              (43, 101, 147), (136, 182, 161), (150, 63, 72), (51, 41, 45), (160, 32, 29), (172, 28, 32), (60, 115, 99),
              (59, 48, 45), (231, 162, 167), (216, 82, 72), (236, 167, 157), (36, 61, 55), (14, 96, 71), (33, 60, 107),
              (171, 188, 220), (197, 96, 105), (105, 126, 159), (18, 83, 105), (174, 200, 188), (34, 150, 209)]


def forward_dot():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


for i in range(10):
    forward_dot()
    tim.backward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()