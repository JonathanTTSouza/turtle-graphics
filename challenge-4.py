"""
Random walk, random color
"""
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
timmy.pensize(width=5)
timmy.speed("fastest")
# TODO 1 Random walk
# TODO 2 Random color each walk
# TODO 3 Increasing Thickness each walk
for _ in range(1000000):
    coin = random.randint(0, 1)

    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    timmy.color((red, green, blue))

    if coin == 0:
        timmy.right(90)
    elif coin == 1:
        timmy.left(90)
    timmy.forward(5)

screen = Screen()
screen.exitonclick()
