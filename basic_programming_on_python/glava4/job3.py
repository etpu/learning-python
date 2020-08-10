"""Даны координаты на плоскости двух точек. Найти расстояние между этими точками."""
from random import randint
from math import hypot
import turtle as tl


a = randint(-400, 400), randint(-400, 400)
b = randint(-400, 400), randint(-400, 400)
dist = hypot(a[0] - b[0], a[1] - b[1])

title = f"Find distance: {a=}, {b=}, {dist=}"
print(title)

tl.reset()
tl.title(title)
tl.speed(0)

for i in range(4):
    tl.forward(420)
    tl.stamp()
    tl.goto(0, 0)
    tl.right(90)

tl.color("green")
tl.pensize(3)
tl.penup()
tl.goto(a)
tl.pendown()
tl.goto(b)
tl.hideturtle()
