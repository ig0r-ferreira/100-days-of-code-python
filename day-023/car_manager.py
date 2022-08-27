import random
from turtle import Turtle
from typing import Tuple, List

COLORS: List[str] = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE: float = 10
MOVE_INCREMENT: float = 5


class CarManager:
    def __init__(self) -> None:
        self.all_cars: list[Turtle] = []
        self.cars_speed: float = STARTING_MOVE_DISTANCE

    def create_car(self) -> None:
        chance = random.randint(1, 4)

        if chance == 1:
            new_car = Turtle(shape="square", visible=False)
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(self.calculate_pos())
            new_car.showturtle()
            self.all_cars.append(new_car)

    def calculate_pos(self) -> Tuple[float, float]:
        y_positions = {(car.ycor() + 30, car.ycor() - 30) for car in self.all_cars if 350 >= car.xcor() >= 250}
        while True:
            random_y = random.uniform(-250, 250)
            if not any(y_max >= random_y >= y_min for y_max, y_min in y_positions):
                break

        return 300, random_y

    def move_cars(self) -> None:
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def has_collision_with(self, target: Turtle) -> bool:
        return any(int(car.distance(x=target.xcor(), y=target.ycor() + 2)) <= 22 for car in self.all_cars)

    def level_up(self):
        if self.cars_speed <= 55:
            self.cars_speed += MOVE_INCREMENT
