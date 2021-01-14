
import turtle
import random

turtle.getscreen()
t = turtle.Turtle()
motion = 1
wide = random.randrange(20, 50, 50)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    turtle.color(R, G, B)


for i in range(200):
    turtle.width(wide)
    turtle.down
    turtle.forward(motion)
    turtle.right(30)
    motion += 1
    turtle.backward(10)
    change_color()


