from turtle import Turtle
from typing import Tuple

STARTING_POSITION: Tuple[float, float] = (0, -280)
MOVE_DISTANCE: float = 10
FINISH_LINE_Y: float = 250


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle", visible=False)
        self.penup()
        self.setheading(90)
        self.go_to_start()
        self.showturtle()

    def go_across(self) -> None:
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self) -> bool:
        return self.ycor() > FINISH_LINE_Y

    def go_to_start(self) -> None:
        self.goto(STARTING_POSITION)
