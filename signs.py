from turtle import Turtle

class Level(Turtle):

    def __init__(self, yset, xset, color):
        super().__init__()

        self.LEVEL = 1
        self.hideturtle()
        self.penup()
        self.pencolor(color)
        self.sety(yset)
        self.setx(xset)
        self.show_level()

    def show_level(self):
        self.write(f"LEVEL: {self.LEVEL}", False, align="center", font=("Courier", 18, "bold"))

    def increase_level(self):

        self.clear()
        self.LEVEL += 1
        self.show_level()

class GameOver(Turtle):
    def __init__(self, carsnumber):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.pencolor("red")
        self.write(f"GAME OVER", False, align="center", font=("Courier", 30, "bold"))
        self.sety(-40)
        self.color("yellow")
        self.write(f"The {carsnumber} cars passed.", False, align="center", font=("Courier", 18, "bold"))