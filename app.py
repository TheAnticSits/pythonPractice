
import turtle
import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)

canvas = turtle.Screen()
turtle.pensize(10)

for i in range(300):
    i += 11
    def fun_drawing():

        turtle.forward(i)
        turtle.right(48)
        change_color()

        if i % 13 == 0:
            canvas.bgcolor("red")
        elif i % 23 == 0:
            canvas.bgcolor("orange")
        elif i % 34 == 0:
            canvas.bgcolor("yellow")
        elif i % 54 == 0:
            canvas.bgcolor("purple")
        elif i % 39 == 0:
            canvas.bgcolor("green")
        else:
            canvas.bgcolor("black")

    fun_drawing()

