from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 30, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-160, 320)
        self.shape("square")
        self.print_score()

    def print_score(self):
        self.write(f"Score {self.score}", align= ALIGN, font = FONT)

    def update_score(self):
        self.clear()
        self.score += 100
        self.print_score()