import turtle as t
import random

tim = t.Turtle()

#Here we are making changes in actual turtle module not turtle object
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


#colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#Python List
directions = [0, 90, 180, 270]

## Drawing different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)

# tim.pensize(15)
tim.speed(10)
#tim.speed("fastest")

# for _ in range(200):
#     #tim.color(random.choice(colors))
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# We cannot change the value of tuple as compared to Python lists
    # we can change a tuple to list like this list(my_tuple) 

#circle of radius 100
tim.circle(100)
tim.color(random_color())


screen = t.Screen()
screen.exitonclick()