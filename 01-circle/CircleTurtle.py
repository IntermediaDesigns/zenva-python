import turtle

# Setup turtle canvas screen
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.pensize(2)
colors = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan']
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Steps to make circles
turtle.circle(50)
turtle.forward(100)
turtle.circle(50)


# Exit turtle
screen.exitonclick()
turtle.done()