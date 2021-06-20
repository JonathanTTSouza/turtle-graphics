from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    return turtle.forward(10)


def move_backwards():
    return turtle.back(10)


def move_left():
    return turtle.left(5)


def move_right():
    return turtle.right(5)


def clear_sketch():
    turtle.setposition(0, 0)
    turtle.setheading(0)
    return turtle.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_sketch)

screen.exitonclick()
