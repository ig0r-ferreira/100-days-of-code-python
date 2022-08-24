import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.setheading(random.uniform(0, 360))
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.04

    def move(self) -> None:
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self) -> None:
        self.x_move *= -1
        self.increase_speed()

    def bounce_y(self) -> None:
        self.y_move *= -1

    def reset_position(self) -> None:
        self.home()
        self.reset_speed()
        self.bounce_x()

    def increase_speed(self):
        if self.move_speed >= 0.01:
            self.move_speed *= 0.9

    def reset_speed(self):
        self.move_speed = 0.04
