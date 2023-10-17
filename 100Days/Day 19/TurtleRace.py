import random
from turtle import Turtle, Screen

is_race_on = False


screen = Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race Game")


user_bet = screen.textinput("Bet the turtles", "Which turtle do you think will win? Enter a color:")

colores = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

goal = Turtle()
goal.penup()
goal.goto(250, -220)
goal.pendown()
goal.goto(250, 220)

goal2 = Turtle()
goal2.penup()
goal2.goto(270, -220)
goal2.pendown()
goal2.goto(270, 220)

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(1)
    new_turtle.color(colores[i])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=y_positions[i])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 250:
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                screen.textinput("Winner!", f"The {winning_color} turtle wins! You guessed it right!")
            else:
                screen.textinput("You lost!", f"The {winning_color} turtle wins! You guessed wrong.")
            is_race_on = False
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
