from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 150)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(0, 250)
        self.write(f'score board', align='center', font=('Courier', 30, 'normal'))

    def leftPoint(self):
        self.l_score += 1
        self.update_score()

    def rightPoint(self):
        self.r_score += 1
        self.update_score()
