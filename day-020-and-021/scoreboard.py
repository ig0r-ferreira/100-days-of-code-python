from turtle import Turtle
import os


ALIGN, FONT = "center", ("Arial", 18, "bold")
FILE_PATH = "data.txt"


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.pencolor("white")
        self.penup()
        self.goto(x=0.0, y=260)

        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.update_scoreboard()

    def increase(self) -> None:
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score:>4}\tHigh Score: {self.high_score:>4}", align=ALIGN, font=FONT)

    def reset_scoreboard(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

        self.score = 0
        self.update_scoreboard()

    def save_high_score(self) -> None:
        with open(FILE_PATH, "w") as file:
            file.write(str(self.high_score))

    def load_high_score(self) -> None:
        if os.path.isfile(FILE_PATH):
            with open(FILE_PATH) as file:
                self.high_score = int(file.readline())
