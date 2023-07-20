from turtle import Screen
from Padle import Right_Padle,Left_Padle
from Ball import ball
from Scoreboard import scoreboard
import time
#TODO 1 :create the main screen
screen=Screen()
screen.setup(width=800,height=600)
screen.title("Arcade Game")
screen.bgcolor("black")
screen.tracer(0)
#TODO 2 : create a paddle
right_padle=Right_Padle()
left_padle=Left_Padle()
#TODO 3 :create the ball
ball=ball()
#TODO 4 : create the scoreboerd
scoreboard=scoreboard()
#TODO 5 : listen to the keyboard and move the right padle
screen.listen()
screen.onkey(fun=right_padle.go_up,key="Up")
screen.onkey(fun=right_padle.go_down,key="Down")
screen.onkey(fun=left_padle.go_up,key= "w")
screen.onkey(fun=left_padle.go_down, key="s")

game_is_on=True
while game_is_on :
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    #detecting collision with the ballq
    if ball.ycor()>280 or ball.ycor()<-280  :
        ball.y_bouncing()
    if ball.distance(right_padle)<50 and ball.xcor()>320 or ball.distance(left_padle)<50 and ball.xcor()<-320 :
        ball.x_bouncing()
    if ball.xcor()>380  :
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.l_point()
















screen.exitonclick()