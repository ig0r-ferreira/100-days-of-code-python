import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def new_car(self):
        car = Turtle(shape="square", visible=False)
        car.shapesize(stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(self.calculate_pos())
        car.forward(STARTING_MOVE_DISTANCE)
        car.showturtle()
        self.cars.append(car)

    def calculate_pos(self):
        y_positions = {(car.ycor() + 30, car.ycor() - 30) for car in self.cars if 350 >= car.xcor() >= 250}
        while True:
            y_pos = random.uniform(-300, 300)
            if not any(y_max >= y_pos >= y_min for y_max, y_min in y_positions):
                break

        return 300, y_pos

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
