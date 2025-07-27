# $! This is the star creater

import turtle # Headline(Main)

# For the color
turtle.Screen().bgcolor("green")

# $! Set up the screen
screen = turtle.Screen()#2

# $! Create the turtle
board = turtle.Turtle()#1

# First triangle for star
board.forward(100)#1
board.left(120)#2
board.forward(100)#3
board.left(120)#4
board.forward(100)#5

# $! Move to position for second triangle
board.penup()#1
board.right(150)#2
board.forward(50)#3
board.pendown()#4

# $! Second triangle for star
board.right(90) #1
board.forward(100)#2
board.right(120)#3
board.forward(100)#4
board.right(120)#5
board.forward(100)#6

# $! Finish
turtle.done()