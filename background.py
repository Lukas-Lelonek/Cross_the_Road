from turtle import Screen, Turtle
import random


class BackgroundSetter(Turtle):

    def __init__(self, y_coord, pen_s, col):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.setx(400)
        self.sety(y_coord)
        self.pencolor(col)
        self.pensize(pen_s)

    def paint(self):
        self.pendown()
        self.goto(-400, self.ycor())

    def paint_stripes(self):
        self.setheading(180)
        self.pencolor("#FFD700")
        self.pensize(3)
        self.forward(random.randint(1, 30))

        while self.xcor() > -400:
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(40)


def create_world():
    grass_down = BackgroundSetter(-228, 25, "#228B22")
    grass_up = BackgroundSetter(228, 25, "#228B22")
    grass_middle = BackgroundSetter(0, 30, "#228B22")

    grass_down.paint()
    grass_up.paint()
    grass_middle.paint()

    road_down = BackgroundSetter(-116, 200, "#696969")
    road_up = BackgroundSetter(115, 200, "#696969")

    road_down.paint()
    road_up.paint()

    STRIPES_Y_POSITION = (63, 116, 166, -65, -116, -168)

    for i in STRIPES_Y_POSITION:
        stripe = BackgroundSetter(i, 5, "#FFD700")
        stripe.paint_stripes()

