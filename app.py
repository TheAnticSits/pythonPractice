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

    for j in range(20):
        def change_color():
            R = random.random()
            B = random.random()
            G = random.random()
            turtle.color(R, G, B)

        def color_black():
            R = 0
            B = 0
            G = 0
            turtle.color(R, G, B)

        turtle.fillcolor(15, 15, 15)
        turtle.begin_fill()

        for i in range(30):

            color_black()
            turtle.down()
            turtle.forward(10)
            turtle.left(20)
            change_color()
            turtle.backward(3)
            turtle.down()
            turtle.right(5)

        turtle.end_fill()

        turtle.up()
        turtle.right(random.random())
        turtle.forward(random.randrange(10, 700))



draw_circle()