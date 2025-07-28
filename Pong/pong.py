""""Pong game using turtle module. From Udemy course by Abdurrahman Tekin"""
from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.bgcolor('blue')
screen.setup(800, 600)

# Paddle setup
paddle = Turtle()
paddle.color('white')
paddle.shape('square')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


# paddle movement
def go_up():
    '''Moves the paddle up'''
    new_y = paddle.ycor() + 30
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    '''Moves the paddle down'''
    new_y = paddle.ycor() - 30
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


# Exit screen
screen.exitonclick()
