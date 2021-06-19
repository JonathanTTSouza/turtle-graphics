"""
Draws a dashed square
"""
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
for _ in range(4):
    for _ in range(15):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
    timmy.left(90)
screen = Screen()
screen.exitonclick()
