#! /usr/bin/env python3

import turtle

tr = turtle.Turtle()

tr.pensize(5)

tr.color("#070F84")
tr.penup()
tr.goto(-110, -25)
tr.pendown()
tr.circle(45)

tr.color("black")
tr.penup()
tr.goto(0, -25)
tr.pendown()
tr.circle(45)

tr.color("#890535")
tr.penup()
tr.goto(110, -25)
tr.pendown()
tr.circle(45)

tr.color("#FFD700")
tr.penup()
tr.goto(-55, -75)
tr.pendown()
tr.circle(45)

tr.color("#7CFC00")
tr.penup()
tr.goto(55, -75)
tr.pendown()
tr.circle(45)

turtle.done()