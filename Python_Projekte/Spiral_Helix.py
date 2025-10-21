#! /usr/bin/env python3

import turtle
loadWindow = turtle.Screen()
turtle.speed(10)
 
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
 
turtle.exitonclick()