from turtle import Turtle, Screen
import random

painting_colors = [(201, 164, 112), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44), (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77), (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48)]

# TODO 1: 10 by 10 spots painting
# TODO 2: Spot size = 20
# TODO 3: Spaced apart by 50

screen = Screen()
screen.colormode(255)

# Initial position
turtle = Turtle()
turtle.penup()
height = -250
turtle.setposition(-250, -250)
for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(painting_colors))
        turtle.forward(50)
    height += 50
    turtle.setposition(-250, height)

turtle.hideturtle()
screen.exitonclick()
