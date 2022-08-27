import time
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

enter = False


def on_enter(*_) -> None:
    global enter
    enter = True


def main() -> None:
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("My Snack Game")
    screen.bgcolor("black")
    screen.tracer(0)

    root = screen.getcanvas().winfo_toplevel()
    root.resizable(False, False)

    turtle.hideturtle()
    turtle.penup()
    turtle.color("white")
    turtle.write("PRESS ENTER TO START", align="center", font=("Arial", 22, "bold"))

    screen.listen()
    while not enter:
        screen.update()
        screen.onkey(on_enter, "Return")

    turtle.clear()

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while True:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) <= 18:
            snake.grow_up()
            scoreboard.increase()
            food.refresh()

        if snake.collided():
            scoreboard.reset_scoreboard()
            snake.reset()


if __name__ == "__main__":
    main()
