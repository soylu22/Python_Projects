from turtle import Turtle, Screen
import random


turtle = Turtle()
screen = Screen()
turtle.shape("turtle")

# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

colors = ["red", "orange", "yellow", "green", "blue",
             "indigo", "violet", "pink", "cyan", "magenta"]

turtle.speed("fastest")
def to_stop(stop_when_circle):
    for i in range(int(360 / stop_when_circle)):
        turtle.color(random.choice(colors))
        turtle.setheading(turtle.heading() + stop_when_circle)
        turtle.circle(100)
to_stop(5)

# angle = 360
# for n in range(1, 11):
#     new_ang = angle / n
#     colors = ["red", "orange", "yellow", "green", "blue",
#               "indigo", "violet", "pink", "cyan", "magenta"]
#     turtle.pencolor(random.choice(colors))
#     for _ in range(n):
#
#         turtle.circle(100)
#         turtle.right(new_ang)
#         turtle.circle(100)
# turtle.pensize(15)
# turtle.speed("fastest")
#
# colors = ["red", "orange", "yellow", "green", "blue",
#              "indigo", "violet", "pink", "cyan", "magenta"]
# directions = [90, 120, 180, 230, 270, 310, 360]
# for _ in range(200):
#     turtle.pencolor(random.choice(random_color()))
#     turtle.forward(50)
#     turtle.setheading(random.choice(directions))





# def move_up():
    # turtle.forward(100)
    # for i in range(100):
        # turtle.right(90)
        # turtle.forward(100)
    #
    # for i in range(50):
    #     turtle.pendown()
    #     turtle.forward(5)
    #     turtle.penup()
    #     turtle.forward(5)

# '''
# turtle move and bend in 360/n, and increment n every time
#  after 1 round
#  '''
#
# # num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# angle = 360
# for n in range(3, 11):
#     new_ang = angle / n
#     colors = ["red", "orange", "yellow", "green", "blue",
#               "indigo", "violet", "pink", "cyan", "magenta"]
#     turtle.pencolor(random.choice(colors))
#     for _ in range(n):
#
#         turtle.forward(100)
#         turtle.right(new_ang)






screen.exitonclick()

