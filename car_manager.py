from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10







class CarManager():
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.level_of_increment = 0




    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(x= 300, y= random_y)
        self.list_of_cars.append(new_car)

    def move(self):
        for car in self.list_of_cars:
            car.backward(STARTING_MOVE_DISTANCE + (self.level_of_increment * MOVE_INCREMENT))

    def increase_level(self):
        self.level_of_increment += 1
