from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()
timmy.color("green")
i = 0
while i < 4:
    timmy.forward(50)
    timmy.right(90)
    i += 1
screen.exitonclick()