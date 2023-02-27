# initial imports
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20


# snake class
class Snake:
    # constructor of the class
    def __init__(self):
        self.length = 3
        self.segments = []
        self.speed = SPEED

        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.setposition(position)
            self.segments.append(segment)

    def follow(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[i - 1].xcor()
            y_cor = self.segments[i - 1].ycor()
            self.segments[i].goto(x_cor, y_cor)
        self.segments[0].forward(20)

    def turn_left(self):
        for i in range(len(self.segments)):
            self.segments[i].left(90)

    def turn_right(self):
        for i in range(len(self.segments)):
            self.segments[i].right(90)

    def get_position(self):
        return self.segments[0].pos()

    def grow(self):
        self.length += 1
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.setposition(self.segments[-1].pos())
        self.segments.append(segment)

    def collide(self):
        for segment1 in self.segments:
            for segment2 in self.segments:
                if abs(segment1.pos()-segment2.pos()) < 3:
                    print("died")







