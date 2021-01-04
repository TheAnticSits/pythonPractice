
import turtle
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)


for i in range(500):
    i += 11
    def fun_drawing():

        turtle.forward(i)
        turtle.right(48)
        change_color()


    fun_drawing()

