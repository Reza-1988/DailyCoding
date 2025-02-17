from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1
        self.update()


    def update(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"level: {self.level}", align="left", font=FONT)


    def level_up(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)