from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        newx = self.xcor()+self.xmove
        newy = self.ycor()+self.ymove
        self.goto(newx, newy)

    def bouncey(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.move_speed *= .9

    def reset(self):
        self.goto(0, 0)
        self.bouncex()
        self.move_speed = .1
