"""Даны катеты прямоугольного треугольника. Определить его
гипотенузу"""
from random import randint
from math import sqrt
import turtle


a, b = randint(-400, 400), randint(-400, 400)

title = f"Triangle: {a=}, {b=}, c={sqrt(a**2 + b**2)}"
print(title)

turtle.reset()
turtle.title(title)
turtle.speed(0)

for i in range(4):
    turtle.forward(420)
    turtle.stamp()
    turtle.goto(0, 0)
    turtle.right(90)
    

turtle.color("blue")
turtle.pensize(3)
turtle.goto(0, a)
turtle.goto(b, 0)
turtle.goto(0, 0)
turtle.hideturtle()
