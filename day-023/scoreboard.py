from turtle import Turtle
from typing import Tuple


FONT: Tuple[str, int, str] = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(-280, 250)
        self.game_level = 1
        self.show_level()

    def show_level(self):
        self.clear()
        self.write(f"Level: {self.game_level}", align="left", font=FONT)

    def increase_level(self):
        self.game_level += 1
        self.show_level()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align="center", font=FONT)
