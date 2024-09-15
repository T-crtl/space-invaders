from turtle import Turtle

class Fire(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_fire(position)

    def create_fire(self, position):
        self.shape("square")
        self.color("red")
        self.speed("fastest")
        self.shapesize(stretch_len=0.2, stretch_wid=1)
        self.penup()
        self.goto(position)

    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
