from turtle import Turtle, Screen
from random import random

timmy = Turtle()
screen = Screen()
timmy.pensize(10)

i = 9
while i < 1000:
    # 0 - 1
    timmy.pencolor(random(), random(), random())
    generated_number = random()
    if generated_number <= 0.25:
        timmy.right(90)
        timmy.forward(10)
    elif generated_number <= 0.50:
        timmy.left(90)
        timmy.forward(10)
    elif generated_number <= 0.75:
        timmy.forward(10)
    else:
        timmy.left(180)
        timmy.forward(10)
    timmy.forward(10)
    i += 1

screen.exitonclick()