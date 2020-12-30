import turtle
import random
from turtle import Turtle

turtle = Turtle()

turtle.speed(10)

turtle.up()
turtle.right(90)
turtle.forward(400)
turtle.left(180)
turtle.down()


def draw_circle():

    for j in range(6):
        def change_color():
            R = random.random()
            B = random.random()
            G = random.random()
            turtle.color(R, G, B)

        for i in range(120):
            turtle.down()
            turtle.forward(50)
            turtle.left(8)
            turtle.up()
            turtle.backward(40)
            turtle.down()
            turtle.right(5)
            change_color()

        turtle.up()
        turtle.right(55)
        turtle.forward(70)



draw_circle()