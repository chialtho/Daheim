#! /usr/bin/env python3

import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

def draw():
    for i in range(4):
        pen.forward(30)
        pen.left(90)
    pen.forward(30)

if __name__=="__main__":
    sc.setup(300, 300) #x,y
    pen.speed(100)
    for i in range(-4,4):
        pen.up()
        pen.setpos(-125, 30 * i)
        pen.down()
        for j in range(8):
            if (i+j)%2 == 0:
                col = "#000033"
            else:
                col = "#FFFFFF"
            pen.fillcolor(col)
            pen.begin_fill()
            draw()
            pen.end_fill()
    pen.hideturtle()
    turtle.done()