import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


def main() -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    scoreboard = Scoreboard()
    player = Player()
    can_manager = CarManager()

    screen.onkeypress(fun=player.go_across, key="Up")
    screen.listen()

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()

        can_manager.create_car()

        if not player.is_at_finish_line():
            can_manager.move_cars()
        else:
            scoreboard.increase_level()
            can_manager.level_up()
            player.go_to_start()

        if can_manager.has_collision_with(player):
            scoreboard.game_over()
            game_is_on = False

    screen.exitonclick()


if __name__ == "__main__":
    main()
