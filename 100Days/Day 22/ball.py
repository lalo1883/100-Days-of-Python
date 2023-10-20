

from turtle import Turtle

class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.x_move = 10
        self.y_move = -10
        self.move_speed = .05

    def move(self):

        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
        # self.move_speed *= .8

    def bounce_paddle(self):
        # self.y_move *= -1
        self.x_move *= -1
        self.move_speed *= .95


    def reset_p(self):
        self.goto(0,0)
        self.move_speed = .05
        self.bounce_paddle()
