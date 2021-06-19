"""
Draws shapes from Triangle to Decagon
"""
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

count = 3
while count < 10:
    for _ in range(count):
        timmy.forward(100)
        timmy.right(360 / count)
    count += 1


screen = Screen()
screen.exitonclick()
