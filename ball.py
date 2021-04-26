from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.movement = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_top_bottom(self):
        self.y_move *= -1

    def bounce_on_paddle(self):
        self.x_move *= -1
        self.movement *= .85

    def ball_reset(self):
        self.goto(0, 0)
        self.movement = 0.1
        self.bounce_on_paddle()
