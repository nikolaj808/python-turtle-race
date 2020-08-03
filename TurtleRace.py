from turtle import *
from random import randint
from time import sleep

t = Turtle()
t.speed(0)
t.penup()
t.goto(-140, 140)
for step in range(16):
    t.write(step, align='center')
    t.right(90)
    t.forward(10)
    for line in range(11):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
    t.backward(230)
    t.left(90)
    t.forward(20)

t.penup()

#ada
ada = Turtle()
ada.speed(1)
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.right(360)
ada.pendown()

#bob
bob = Turtle()
bob.speed(1)
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 50)
bob.right(360)
bob.pendown()

#glen
glen = Turtle()
glen.speed(1)
glen.color('green')
glen.shape('turtle')
glen.penup()
glen.goto(-160, 0)
glen.right(360)
glen.pendown()

#seth
seth = Turtle()
seth.speed(1)
seth.color('yellow')
seth.shape('turtle')
seth.penup()
seth.goto(-160, -50)
seth.right(360)
seth.pendown()

def playGame():
    while True:
        ada.forward(randint(1, 5))
        bob.forward(randint(1, 5))
        glen.forward(randint(1, 5))
        seth.forward(randint(1, 5))
        if (ada.xcor() >= 145.0):
            t.forward(20)
            t.write("Ada won!", font=("Arial", 12, "normal"))
            break
        elif (bob.xcor() >= 145.0):
            t.forward(20)
            t.write("Bob won!", font=("Arial", 12, "normal"))
            break
        elif (glen.xcor() >= 145.0):
            t.forward(20)
            t.write("Glen won!", font=("Arial", 12, "normal"))
            break
        elif (seth.xcor() >= 145.0):
            t.forward(20)
            t.write("Seth won!", font=("Arial", 12, "normal"))
            break
playGame()

question = input('Ready to quit?')