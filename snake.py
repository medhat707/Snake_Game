#snake Game
from turtle import Turtle
class Snake:
    def __init__(self):
        # now we define our attributes
        #  1st attribute for list of snakes
        self.segments = []
        # this is a method
        self.create_snake()

    def create_snake(self):
        # add 3 tims in 3 different places
        position = [(0,0), (-20,0), (-40,0)]
        for i in range(0, 3):
            self.append_new_extension(position[i]) #hna bt2olo wadi tim 3nd pos[i] code line 26 wb3den append in list
            # tim = Turtle("square")
            # tim.color("white")
            # tim.penup()
            # tim.speed("slowest")
            # tim.goto(index_x[i], 0)
            # self.segments.append(tim)  # to add all 3 tems to a list

    def append_new_extension(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)  # to add all 3 tems to a list

    def add_new_segment(self):
        extension_position = self.segments[-1].position()
        self.append_new_extension(extension_position)

    def mov(self):
        for tinny_tim in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[tinny_tim - 1].xcor()  # to get hold of tinny_tim at x-pos 1 .. tani wa7ed
            new_y = self.segments[tinny_tim - 1].ycor()  # to get hold of tinny_tim at y-pos 1 .. tani wa7ed
            self.segments[tinny_tim].goto(new_x, new_y)  # to let last tinny_tim 2 move to pos of tinny_tim 1
        self.segments[0].forward(20)

    #snake will continue even after hitting wall
    def reset(self):
        #looping through snake segments and sending them to another place far away
        for seg in self.segments:
            seg.goto(1000,1100)
        self.segments.clear()
        self.create_snake()
        self.segments[0]

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)






