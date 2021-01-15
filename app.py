
import turtle
import random

turtle.getscreen()
t = turtle.Turtle()

def move_turtle():
    move = random.random()
    return move

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


def move_that_turtle():

    motion = 1

    for j in range(10):
        turtle.up()
        turtle.forward(motion)
        turtle.forward(motion)
        turtle.forward(motion)
        turtle.forward(motion)
        turtle.left(motion)
        if j % 5 == 0:
            motion = 1
            turtle.right(40)
            turtle.forward(50)

        turtle.down()

        for i in range(25):
            turtle.width(15)
            turtle.forward(motion)
            change_color()
            turtle.right(115)
            motion += 1
            turtle.backward(motion)
            change_color()
            turtle.left(random.random())


move_that_turtle()