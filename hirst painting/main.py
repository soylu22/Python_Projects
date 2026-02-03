import turtle
import random

try:
    import colorgram  # optional; not required for this script
except Exception:
    colorgram = None


def main():
    eli = turtle.Turtle()
    screen = turtle.Screen()
    eli.speed("fastest")
    eli.hideturtle()
    turtle.colormode(255)
    eli.penup()

    rgb_colors = [
        (255, 0, 0),     # red
        (0, 255, 0),     # green
        (0, 0, 255),     # blue
        (255, 255, 0),   # yellow
        (139, 80, 53),
        (185, 163, 125),
        (138, 166, 176),
        (60, 111, 134),
        (17, 42, 73),
        (139, 62, 88),
    ]

    eli.setheading(220)
    eli.forward(300)
    eli.setheading(0)

    for _ in range(10):
        eli.dot(20, random.choice(rgb_colors))
        eli.forward(50)

    for _ in range(9):
        eli.setheading(90)
        eli.forward(50)
        eli.setheading(180)
        eli.forward(500)
        eli.setheading(0)
        for _ in range(10):
            eli.dot(20, random.choice(rgb_colors))
            eli.forward(50)

    screen.exitonclick()


if __name__ == "__main__":
    main()