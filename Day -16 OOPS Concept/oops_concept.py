# import another_module
# print(another_module.another_variable)

# import turtle

from turtle import Turtle, Screen

# timmy = turtle.Turtle()
timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('tomato')
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()