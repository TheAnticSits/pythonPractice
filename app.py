
import turtle
import random

turtle.getscreen()
t = turtle.Turtle()
motion = 1
def move_turtle():
    move = random.random()
    return move

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


for i in range(200):
    turtle.width(move_turtle())
    turtle.down
    turtle.forward(motion)
    turtle.right(5)
    motion += 1
    turtle.backward(10)
    change_color()
    turtle.left(random.random())


