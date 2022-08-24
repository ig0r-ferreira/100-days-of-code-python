from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.print_division()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 68, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 68, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def print_division(self) -> None:
        painter = Turtle(visible=False)
        painter.color("white")
        painter.penup()
        painter.speed("fastest")
        painter.goto(0, -self.screen.canvheight)
        painter.setheading(90)

        while painter.ycor() < self.screen.canvheight:
            painter.down()
            painter.forward(10)
            painter.penup()
            painter.forward(10)
