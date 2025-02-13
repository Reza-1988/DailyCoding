from turtle import Turtle

nets_positions = [(0, -250), (0, -150), (0, -50), (0,50), (0,150), (0, 250)]
class Net():
    def __init__(self):
        self.nets = []
        self.create_net()

    def create_net(self):
        for position in nets_positions:
            new_net = Turtle()
            new_net.penup()
            new_net.shape("square")
            new_net.color("white")
            new_net.shapesize(stretch_wid=3, stretch_len=0.5)
            new_net.penup()
            new_net.goto(position)
            self.nets.append(new_net)