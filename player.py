from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
screen = Screen()

class Player(Turtle):
    def __init__(self, up_key):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.shapesize(.8)
        self.setheading(90)
        self.goto(x= 0, y= -300)
        screen.listen()
        screen.onkeypress(self.move_up, key=up_key)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x= self.xcor() ,y= new_y)

