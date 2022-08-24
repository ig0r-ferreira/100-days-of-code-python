from turtle import Turtle
from typing import Tuple


class Paddle(Turtle):
    def __init__(self, position: Tuple[float, float], color: str = "white"):
        super().__init__(shape="square")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(position)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(color)

    def go_up(self):
        if self.ycor() < (self.screen.canvheight - 70):
            self.forward(40)

    def go_down(self):
        if self.ycor() > -(self.screen.canvheight - 80):
            self.backward(40)
