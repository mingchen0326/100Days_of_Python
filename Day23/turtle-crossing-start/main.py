import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

carList = CarManager()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(0, 100) < 20:
        carList.add_car()

    if player.check_pass():
        scoreboard.refresh()
        player.reset_position()
        carList.speed_increase()

    if carList.check_collision(player):
        scoreboard.game_over()
        break

    carList.next_move()

screen.exitonclick()