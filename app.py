import random

name = input("What is your name? ")
age = input("What is your age? ")
languages = random.randint(0, 5)

def sayhi(name, age):
    print("Hello " + name + ",")
    print("You are " + age + " years old.")
    print("My guess is you know " + str(languages) + " programming languages.")

sayhi(name, age)