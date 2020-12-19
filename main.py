from turtle import Screen
from background import create_world
from walker import Walker
from cars import Car
from signs import Level, GameOver
import random
import time

screen = Screen()
screen.setup(height=480, width=800)
screen.title("Cross the Road")
screen.register_shape("walker_graphic.gif")
screen.register_shape("cars/truck.gif")
screen.register_shape("cars/right_truck.gif")
screen.register_shape("walker_graph/dead1.gif")
screen.register_shape("walker_graph/dead2.gif")
screen.tracer(0)

create_world()
john = Walker()
level = Level(190, - 350, "white")
screen.update()


game_over = False

TRAFFIC = []
LEFT = 180
RIGHT = 0

LANE_RIGHT = (-190, -140, -90, -40)
LANE_LEFT = (40, 90, 140, 190)
cars_passed = 0
DIFFICULTY_FACTOR = 800
speed = 5

def allow_move():
    screen.listen()
    screen.onkey(john.move_up, "Up")
    screen.onkey(john.move_down, "Down")


while not game_over:
    tick = time.time()
    TRAFFIC_FACTOR = random.randint(1, int(DIFFICULTY_FACTOR))

    if TRAFFIC_FACTOR < 20:
        lan_l = random.choice(LANE_LEFT)
        TRAFFIC.append(Car(lan_l, LEFT))
        cars_passed += 1
        print(f"The number of cars on the highway: {cars_passed}")

    if TRAFFIC_FACTOR in range(80, 101):
        lan_r = random.choice(LANE_RIGHT)
        TRAFFIC.append(Car(lan_r, RIGHT))
        cars_passed += 1
        print(f"The number of cars on the highway: {cars_passed}")

    if john.reach_finish():
        screen.update()
        screen.ontimer(john.new_level(), 300)
        level.increase_level()
        if DIFFICULTY_FACTOR > 130:
            DIFFICULTY_FACTOR = DIFFICULTY_FACTOR * 0.95
        speed += 1
        print(f"Current difficulty is {DIFFICULTY_FACTOR}")

    time.sleep(0.04)
    screen.update()
    for i in range(len(TRAFFIC)):
        TRAFFIC[i].move(speed)
        #Detect collision
        if TRAFFIC[i].distance(0, john.ycor()) < 35:
            game = GameOver(cars_passed)
            john.death()
            game_over = True

    if len(TRAFFIC) > 50:
        del TRAFFIC[:-50]

    if cars_passed > 8:
        allow_move()


screen.update()
screen.exitonclick()