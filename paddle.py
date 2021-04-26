from turtle import Turtle,Screen


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x)

    def move_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

        else:
            self.goto(self.xcor(), 250)

    def move_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)

        else:
            self.goto(self.xcor(), -250)
