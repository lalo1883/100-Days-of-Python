STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.go_to_start()

    def move_f(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_l(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_r(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def is_at_end(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
