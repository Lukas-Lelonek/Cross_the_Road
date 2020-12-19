from turtle import Turtle
import random
Bodies = ("walker_graph/dead2.gif", "walker_graph/dead1.gif")

MOVE_COORDINATES = (-225, -190, -140, -90, -40, 0, 40, 90, 140, 190, 225)
STARTING_POINT = MOVE_COORDINATES[0]
FINISH = MOVE_COORDINATES[-1]

class Walker(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.sety(STARTING_POINT)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.shape("walker_graphic.gif")
        self.color("yellow")
        self.setheading(90)
        self.showturtle()


    def move_up(self):
        if self.ycor() < FINISH:
            move = MOVE_COORDINATES[MOVE_COORDINATES.index(self.ycor()) +1]
            self.goto(0, move)

    def move_down(self):
        if self.ycor() > STARTING_POINT:
            move = MOVE_COORDINATES[MOVE_COORDINATES.index(self.ycor()) - 1]
            self.goto(0, move)

    def reach_finish(self):
        if self.ycor() == FINISH:

            return True

    def new_level(self):
        self.goto(0, FINISH)
        self.hideturtle()
        self.goto(0, STARTING_POINT)
        self.showturtle()

    def death(self):
        body = Bodies[random.randint(0,1)]
        self.shape(body)