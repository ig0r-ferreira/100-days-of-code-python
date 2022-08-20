import colorgram
import turtle
import random


colors = colorgram.extract("image.png", 20)
rgb_colors = [color.rgb for color in colors if not all(value >= 240 for value in color.rgb)]

turtle.colormode(255)

sid = turtle.Turtle(shape="turtle", visible=False)
sid.penup()
sid.speed(0)

ini_x, ini_y = -250, -250
num_lines, num_dots_per_line, dot_size, gap = 10, 10, 20, 50

for _ in range(num_lines):
    sid.goto(ini_x, ini_y)

    for _ in range(num_dots_per_line):
        sid.dot(dot_size, random.choice(rgb_colors))
        sid.forward(gap)

    ini_y += gap

screen = turtle.Screen()
screen.mainloop()
