from turtle import Turtle, Screen
from random import random

timmy = Turtle()
screen = Screen()
timmy.pencolor()


i = 3
while i < 10:
    timmy.pencolor(random(), random(), random())
    j = 0
    while j < i:
        timmy.right(360//i)
        timmy.forward(100)
        j += 1
    i += 1

screen.exitonclick()