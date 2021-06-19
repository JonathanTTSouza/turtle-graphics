"""
Spirograph
"""

from turtle import Turtle, Screen
import random


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue


timmy = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("black")
timmy.speed("fast")

count = 1
for _ in range(int(360/10)):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(10)

screen.exitonclick()
