# initial imports
import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

# screen attributes and functions
main_screen = Screen()
main_screen.bgcolor("black")
main_screen.setup(600, 600)
main_screen.title("Snake Game in Bilkent!!")
main_screen.tracer(0)

snake = Snake()

x_rand = random.randint(-270, 270)
y_rand = random.randint(-270, 270)

food = Food(x_rand, y_rand)

main_screen.onkey(snake.turn_left, "Left")
main_screen.onkey(snake.turn_right, "Right")
main_screen.listen()

# game instances
game_on = True

while game_on:
    main_screen.update()
    time.sleep(0.1)

    snake.follow()
    if abs(food.get_position() - snake.get_position()) < 20:
        x_rand = random.randint(-270, 270)
        y_rand = random.randint(-270, 270)
        food.set_position(x_rand, y_rand)
        snake.grow()
        snake.collide()












"""
game_on = True
while game_on:
    main_screen.setup()
    time.sleep(0.1)

    move()
    follow()
    turn_left()
    follow()
"""











main_screen.listen()


main_screen.exitonclick()