from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_data.txt", "r") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.print_score()


    def print_score(self):
        self.clear()
        self.write(f"score : {self.score} High score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore_data.txt", "w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

