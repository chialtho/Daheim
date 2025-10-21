#! /usr/bin/env python3

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.speed(10)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

cv = turtle.getcanvas()
cv.postscript(file="file_name.ps", colormode='color')

turtle.done()