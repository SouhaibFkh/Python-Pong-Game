from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_x = 12
        self.ball_y = 12
        self.ball_speed = 0.1
        
    
    def move(self):
        new_x = self.xcor() + self.ball_x
        new_y = self.ycor() + self.ball_y
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.ball_y *= -1
        self.ball_speed *= 0.9
    
    def bounce_x(self):
        self.ball_x *= -1
        self.ball_speed *= 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()
