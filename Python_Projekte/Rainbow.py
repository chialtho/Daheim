#! /usr/bin/env python3

import turtle

sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col, rad, val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)

col = ['#AF62B7', '#712BAF', '#230EAF', '#0E9FAF', '#0EAF7F',
       '#0EAF33', '#69CD38', '#FFFF00', '#FF8C00', '#BD2323']

sc.setup(600, 600)
sc.bgcolor('black')

pen.right(90)
pen.width(10)
pen.speed(7)

for i in range(len(col)):
    semi_circle(col[i], 10*(i + 7), -10*(i+1))

pen.hideturtle()

turtle.done()