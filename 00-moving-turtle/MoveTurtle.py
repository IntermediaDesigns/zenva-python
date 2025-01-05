import turtle

# Turtle screen
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.pensize(2)
colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Steps to move turtle

# Forward moves in pixels
turtle.forward(50)
# turn turtle on degrees (90 deg for square, 120 triangle)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Exit turtle
turtle.exitonclick()
turtle.done()
