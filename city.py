from turtle import *

speed(100)

def sky():
    screen = Screen()
    screen.setup(width=700, height=700)
    screen.bgcolor("skyblue")

def sun():
    penup()
    goto(200,200)
    pendown()
    pensize(1)
    color('yellow')
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()

def towers():
    pensize(2)
    color('DarkGray')
    penup()
    goto(-345,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(100)
        left(90)
        forward(400)
        left(90)
    end_fill()
    goto(-240,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(100)
        left(90)
        forward(300)
        left(90)
    end_fill()
    goto(-140,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(100)
        left(90)
        forward(500)
        left(90)
    end_fill()

def towers2():
    pensize(2)
    color('DarkGray')
    penup()
    goto(-35,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(100)
        left(90)
        forward(450)
        left(90)
    end_fill()
    goto(80,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(100)
        left(90)
        forward(380)
        left(90)
    end_fill()
    goto(185,-340)
    pendown()
    begin_fill()
    for i in range(2):

        forward(150)
        left(90)
        forward(500)
        left(90)
    end_fill()

def  road():
    begin_fill()
    penup()
    goto(-345,-340)
    pendown()
    color('black')
    forward(700)
    left(90)
    forward(10)
    left(90)
    forward(700)
    left(90)
    forward(10)
    left(90)
    end_fill()
    for i in range(1):
        color('white')
        goto(-345, -335)
        forward(700)


while True:
    a = input("Play or Exit: ")
    if a == 'exit':
        break  # Exit the loop if the user inputs 'exit'
    elif a == 'play':
        sky()
        sun()
        towers()
        towers2()
        road()
    else:
        print("Invalid input. Please enter 'play' or 'exit'.")

hideturtle()
exitonclick()

