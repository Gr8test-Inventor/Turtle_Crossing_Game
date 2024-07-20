import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=650)
screen.bgcolor("black")
screen.tracer(0)

player = Player("Up")
carmanager = CarManager()
scoreboard = Scoreboard()

sleep_time = 0.1
car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_counter += 1
    if car_counter % 6 == 0 or car_counter == 1:
        carmanager.create_car()

    carmanager.move()

    # Reset turtle and increase score
    if player.ycor() > 280:
        player.goto(x= 0, y= -275)
        screen.update()
        scoreboard.increase_level()
        carmanager.increase_level()
        sleep_time -= .005

        scoreboard.update_scoreboard()

    # Game over if car touches
    for vehicle in carmanager.list_of_cars:
        if player.distance(vehicle) < 20:
            game_is_on = False
scoreboard.game_over()

screen.exitonclick()
