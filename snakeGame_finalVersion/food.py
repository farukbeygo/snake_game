# food class
from turtle import Turtle


class Food:
    def __init__(self, xcor, ycor):
        self.food = Turtle("circle")
        self.food.color("blue")
        self.food.penup()
        self.food.goto(xcor, ycor)

    def get_position(self):
        return self.food.pos()

    def set_position(self, xcor, ycor):
        self.food.goto(xcor, ycor)

