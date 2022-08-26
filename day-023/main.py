import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
can_manager = CarManager()

screen.onkeypress(fun=player.go_forward, key="Up")
screen.listen()

show_car = False
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if not show_car:
        can_manager.new_car()
        show_car = True
    else:
        show_car = False

    can_manager.move_cars()
    if any((car.ycor() + 30) >= player.ycor() >= (car.ycor() - 30) and player.distance(car) <= 25
           for car in can_manager.cars):
        print("GAME OVER")
        break

screen.exitonclick()
