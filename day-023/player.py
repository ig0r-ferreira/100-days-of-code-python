from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle", visible=False)
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.showturtle()

    def go_forward(self):
        if self.ycor() <= FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

