import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def main() -> None:
    screen = Screen()
    screen.title("The Pong Game")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    r_paddle = Paddle(position=(screen.canvwidth - 40, 0), color="blue")
    l_paddle = Paddle(position=(-(screen.canvwidth - 30), 0), color="red")
    ball = Ball()
    scoreboard = Scoreboard()

    screen.onkeypress(r_paddle.go_up, "Up")
    screen.onkeypress(r_paddle.go_down, "Down")
    screen.onkeypress(l_paddle.go_up, "w")
    screen.onkeypress(l_paddle.go_down, "s")
    screen.listen()

    while True:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if abs(ball.ycor()) >= (screen.canvheight - 30):
            ball.bounce_y()

        if (ball.distance(r_paddle) < 50 and ball.xcor() > (r_paddle.xcor() - 30)) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < (l_paddle.xcor() + 30)):
            ball.bounce_x()

        if ball.xcor() >= (screen.canvwidth - 10):
            scoreboard.l_point()
            ball.reset_position()

        if ball.xcor() <= -(screen.canvwidth - 10):
            scoreboard.r_point()
            ball.reset_position()


if __name__ == "__main__":
    main()
