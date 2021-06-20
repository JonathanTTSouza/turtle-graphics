"""
Turtle race
"""

from turtle import Turtle, Screen
import random


def new_turtle(height, turtle_color):
    name = Turtle()
    name.shape("turtle")
    name.penup()
    name.setposition(x=-230, y=height)
    name.color(turtle_color)
    return name


screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

initial_y = -75
turtle_list = []
for color in colors:
    turtle_list.append(new_turtle(height=initial_y, turtle_color=color))
    initial_y += 25


race_on = True
while race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            race_on = False
        movement_speed = random.randint(0, 10)
        turtle.forward(movement_speed)

if winner == user_bet:
    print(f"You win! The winning turtle is {winner}")
else:
    print(f"You lose! The winning turtle is {winner}")

screen.exitonclick()
