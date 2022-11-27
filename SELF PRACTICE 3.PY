#PROGRAM TO DRAW A RED COLOR THICK PEN ON A YELLOW BACKGROUND
import turtle
turtle.bgcolor("yellow")
turtle.color("red")
turtle.pensize(10)
for angle in range(0,360,30):
    turtle.seth(angle)
    turtle.circle(100)
