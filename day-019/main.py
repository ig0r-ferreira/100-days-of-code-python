import turtle
import random


def main():
    screen = turtle.Screen()
    screen.setup(700, 400)
    x_pos, y_pos = 20 - (screen.window_width() / 2), -screen.window_height() / 4

    colors = ["red", "blue", "green", "black", "orange", "purple"]

    for color in colors:
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=x_pos, y=y_pos)

        y_pos += 30

    while True:
        user_color = screen.textinput(title="Make your bet", prompt="Which turtle will the race? Enter a color: ")
        if user_color is None:
            return
        elif user_color in colors:
            break

        print("Error: There is not a turtle with that color. Try again.")

    race_in_progress, winner_color = True, None

    while race_in_progress:
        for runner_turtle in screen.turtles():
            runner_turtle.forward(random.randint(0, 10))

            if runner_turtle.xcor() >= (screen.window_width() / 2) - 20:
                race_in_progress = False
                winner_color = runner_turtle.pencolor()

    print("You", "win." if user_color == winner_color else "lose.",
          f"The {str(winner_color).upper()} turtle is the winner!")

    screen.mainloop()


if __name__ == "__main__":
    main()
