# we want to inherit from turtle class
from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # shape is a method in turtle
        self.penup()
        self.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.color("green")
        self.speed("slow")
        self.refresh() # keda el food kol mra hyro7 rand location
        # now we go to our main and import our food

    def refresh(self):
        rand_x=random.randint(-280,280)
        rand_y=random.randint(-280,280)

        self.goto(rand_x,rand_y)