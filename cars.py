from turtle import Turtle
import time

LANE = (-190, -140, -90, -40, 40, 90, 140, 190)


class Car(Turtle):

    def __init__(self, lane, direction):
        super().__init__()

        if direction == 0:
            direc = -450
            self.shape("cars/right_truck.gif")
        else:
            direc = 450
            self.shape("cars/truck.gif")

        self.hideturtle()
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color("#BC8F8F")
        self.setx(direc)
        self.sety(lane)
        self.showturtle()
        self.speed(1)
        self.setheading(direction)

    def move(self, speed):

        self.forward(speed)
