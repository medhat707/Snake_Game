# we want to inherit from turtle class
import turtle
from turtle import Turtle
import random
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        #introducing high score
        # self.highscore
        with  open("data.txt") as mydatafile:
            self.highscore = mydatafile.read()
            self.highscore = int(self.highscore)

        self.color("red")
        self.penup()
        self.goto(0,270)
        self.write(f"score = {self.score}" , False, align="center",font=("Arial",25,"normal"))
        self.hideturtle()



    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with  open("data.txt", mode="w") as mydatafile:
                mydatafile.write(str(self.highscore))
        self.score=0

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score} High score: {self.highscore}",    False, align="center", font=("Arial", 25, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER! = {self.score}", False, align="center", font=("Arial", 25, "normal"))
