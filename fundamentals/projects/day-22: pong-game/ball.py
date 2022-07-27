from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 8
        self.dy = 8
        self.move_speed = 0.1

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)
#        new_x = self.xcor() + self.dx
#        new_y = self.ycor() + self.dy
#        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



