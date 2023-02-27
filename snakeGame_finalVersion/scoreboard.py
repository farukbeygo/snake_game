# scoreboard class
from turtle import Turtle

class ScoreBoard:

    def __init__(self):
        self.score = 0
        self.score_board = Turtle()
        self.final_board = Turtle()
        self.final_board.hideturtle()

    def create_board(self):
        self.score_board.color("white")
        self.score_board.penup()
        self.score_board.hideturtle()
        self.score_board.setposition(0, 270)
        self.score_board.write(f"Score = {self.score}", True, align="center", font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.score_board.clear()

    def final_result(self):
        self.final_board.color("red")
        self.final_board.write(f"Your Final Score = {self.score}!!", True, align="center", font=('Arial', 30, 'normal'))