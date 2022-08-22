from turtle import Turtle

ALIGN, FONT = "center", ("Arial", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.pencolor("white")
        self.penup()
        self.goto(x=0.0, y=260)

        self.score = 0
        self.update_scoreboard()

    def increase(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
