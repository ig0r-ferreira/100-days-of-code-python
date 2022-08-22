import random
import turtle

ALIGN, FONT = "center", ("Arial", 14, "bold")


class Food(turtle.Turtle):

    def __init__(self) -> None:
        super().__init__(shape="circle")
        self.shapesize(0.8, 0.8)
        self.color("green")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        while True:
            x_random = random.uniform(-280.0, 280.0)
            y_random = random.uniform(-280.0, 250.0)
            if (x_random, y_random) not in \
                    [turtle_.pos() for turtle_ in turtle.turtles() if not isinstance(turtle_, Food)]:
                break

        self.goto(x_random, y_random)

