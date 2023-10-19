

from turtle import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.updateScoreBoard()
        self.hideturtle()


    def updateScoreBoard(self):
        self.write(f'Your score is: {self.score}', align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER :(', align='center', font=('Arial', 20, 'normal'))


    def addPoints(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()