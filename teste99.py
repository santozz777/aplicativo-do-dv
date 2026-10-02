from turtle import *
title("NIIN KM")
setup(width=600, height=670)
bgcolor('black')
pencolor('red')
x=0
y=0
speed(0)
penup()
goto(0, 200)
pendown()
while(True):
    forward(x)
    right(y)
    x+=3
    y+=1
    if y==210:
        break
    hideturtle()

done()