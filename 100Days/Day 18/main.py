from turtle import *
import random
import colorgram

from turtle import *
import random

screen = Screen()

pen = Turtle()
pen.speed(0)

colores = ["red", "orange", "yellow", "green", "blue", "purple"]


def painting():
    for _ in range(10):
        for _ in range(10):
            pen.color(random.choice(colores))
            pen.dot(10)
            pen.penup()
            pen.forward(20)  # Ajusta el espacio entre los puntos
            pen.pendown()
        pen.left(170)
        pen.up()
        pen.forward(202)
        pen.right(170)
        pen.down()


painting()
screen.exitonclick()
