import random
import turtle

race_is_on = False
# tim = turtle.Turtle(shape="turtle")
screen = turtle.Screen()
screen.setup(width= 500, height= 400)
bet = screen.textinput(title= "Bet on turtle", prompt= "Pick a color of a turtle to bet: ")
colors = ["blue", "red", "green", "yellow", "grey", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]
all_turtle = []

for i in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-235, y= y_position[i])
    new_turtle.color(colors[i])
    all_turtle.append(new_turtle)

if bet:
    race_is_on = True

while race_is_on:

    for turtle in all_turtle:
        rand_dis = random.randint(1, 10)
        turtle.forward(rand_dis)

        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if bet == winning_color:
                print(f"You won!, {winning_color} is the fastest!")
            else:
                print(f"You Lost!, {winning_color} is the fastest!")


screen.exitonclick()