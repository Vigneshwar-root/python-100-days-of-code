# from turtle import Turtle, Screen
import turtle as t;

tim = t.Turtle()
tim.shape("turtle")

tim.color("tomato")

# for _ in range(4):
#     print(_)
#     tim.right(90)
#     tim.forward(100)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


num_sides = 5
angle = 360 / num_sides

for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)
    print(angle)


screen = t.Screen()
screen.exitonclick()


