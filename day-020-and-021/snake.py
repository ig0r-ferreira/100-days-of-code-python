from turtle import Turtle
from typing import Tuple, List

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0
MOVE_DISTANCE = 20


class Snake:
    def __init__(self, color: str = "red") -> None:
        self.segments: List[Turtle] = []
        self.color: str = color
        for i in range(3):
            position = (0 - (i * 20), 0)
            self.add_segment(position)

        self.head: Turtle = self.segments[0]

    def add_segment(self, position: Tuple[float, float]):
        segment = Turtle(shape="square")
        segment.color(self.color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def grow_up(self) -> None:
        self.add_segment(self.segments[-1].pos())

    def move(self) -> None:
        for pos in range(len(self.segments) - 1, 0, -1):
            self.segments[pos].goto(self.segments[pos - 1].pos())

        self.head.forward(MOVE_DISTANCE)

    def collided(self) -> bool:
        head = self.head
        return abs(head.xcor()) >= 295 or abs(head.ycor()) >= 295 or \
            any(head.distance(segment) < 10 for segment in self.segments[2:])

    def up(self) -> None:
        if self.head.heading() not in (DOWN, UP):
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() not in (UP, DOWN):
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() not in (RIGHT, LEFT):
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() not in (LEFT, RIGHT):
            self.head.setheading(RIGHT)
