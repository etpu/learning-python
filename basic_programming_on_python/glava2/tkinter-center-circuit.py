import turtle
from math import pi

"""Рисуем многоугольники (круги) по центру экрана"""


side = int(input("Введите число сторон: "))
length = int(input("Введите длину стороны: "))

degree = 360/side

turtle.reset()
turtle.up()
turtle.goto(-length/2, (side*length)/(2*pi))
turtle.down()

for i in range(side):
    turtle.forward(length)
    turtle.right(degree)
    
