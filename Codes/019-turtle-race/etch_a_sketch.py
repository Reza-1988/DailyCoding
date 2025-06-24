import turtle as t


tim = t.Turtle()
screen = t.Screen()
tim.pensize(5)
tim.turtlesize(2)

def move_forwards():
    tim.setheading(0)
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.forward(10)

def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()