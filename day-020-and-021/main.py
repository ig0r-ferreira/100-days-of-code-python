import time
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("My Snack Game")
    screen.bgcolor("black")
    screen.tracer(0)

    root = screen.getcanvas().winfo_toplevel()
    root.resizable(False, False)

    snake = Snake("red")
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while not snake.collided():
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) <= 18:
            snake.grow_up()
            scoreboard.increase()
            food.refresh()

    scoreboard.game_over()
    screen.mainloop()


if __name__ == "__main__":
    main()
