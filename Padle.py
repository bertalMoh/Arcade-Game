from turtle import Turtle
from random import randint
#TODO 1 : create the  Right paddle
paddle_segements=[]
class Right_Padle(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto((350, 0))
    def go_up(self) :
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self) :
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

#TODO 2 : create the left paddle
class Left_Padle(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed("fastest")
        self.goto((-350, 0))
    def go_up(self) :
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self) :
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

