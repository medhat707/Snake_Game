from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) #to turn GIF of moving snake off!


# ------- this piece of code is now moved to
# -------- create_snake in snake.py
# tims_list=[]
# # add 3 tims in 3 different places
# index_x = [0,-20,-40]
# for i in range(0,3):
#     tim = Turtle("square")
#     tim.color("white")
#     tim.penup()
#     tim.goto(index_x[i],0)
#     tims_list.append(tim) # to add all 3 tems to a list

snake=Snake()
food=Food()
scoreboard=Score()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")
screen.onkey(snake.down , "Down")



game_is_on=True
while(game_is_on):
    # for tinny_tim in tim_number:
        # tinny_tim.forward(20)
    time.sleep(0.1)
    screen.update()
    snake.mov()
    # detect collision with food
    # if the snake head near to food, then collide
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.add_new_segment()
        scoreboard.increase_score()

    #detecting collision with wall -> GAME OVER
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor() <-280:
        # game_is_on=False
        scoreboard.reset()
        snake.reset()

    # detecting collision with the tail
    for segments in snake.segments[1:]:
        # ---------- PASS HEAD --------------
        # if segments == snake.segments[0]:
        #     pass
        # --------- USING SLICING ----------
        # snake.segments = [(posx,posy),(posx,posy),(posx,posy)]
        if snake.segments[0].distance(segments) < 10:
            game_is_on=False
            scoreboard.reset()
    # for tinny_tim in range(start=2, stop=0 , step=-1): #tinny_tim[2] means tim(-40,0) is the last tim
    # the above for loop does not work with python .. only with C
    # for tinny_tim in range(len(tims_list)-1, 0, -1):
    #     new_x= tims_list[tinny_tim-1].xcor() #to get hold of tinny_tim at x-pos 1 .. tani wa7ed
    #     new_y= tims_list[tinny_tim-1].ycor() #to get hold of tinny_tim at y-pos 1 .. tani wa7ed
    #     tims_list[tinny_tim].goto(new_x,new_y) # to let last tinny_tim 2 move to pos of tinny_tim 1


screen.exitonclick()
