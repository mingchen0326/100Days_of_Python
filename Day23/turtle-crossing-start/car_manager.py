from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.number_of_cars = 20
        self.carList = []
        self.collision = False
        self.speed = STARTING_MOVE_DISTANCE
    
    def make_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(300, random.randint(-250, 280))
        car.setheading(180)
        return car

    def add_car(self):
        self.carList.append(self.make_car())

    def next_move(self):
        for car in self.carList:
            car.forward(self.speed)

    def speed_increase(self):
        self.speed += MOVE_INCREMENT

    def check_collision(self, player):
        for car in self.carList:
            if car.distance(player) < 20:
                self.collision = True
        return self.collision


