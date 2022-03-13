from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
screen = Screen()

rpaddle = Paddle((360, 0))
lpaddle = Paddle((-360, 0))
ball = Ball()
screen.tracer(0)
game_is_on = True
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
score = ScoreBoard()
screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        # change the directino of the ball
        ball.bouncey()

    # detect collision with the paddle
    if ball.xcor() > 310 and ball.distance(rpaddle) < 50 or ball.xcor() < -310 and ball.distance(lpaddle) < 50:
        ball.bouncex()

    # detect R paddle misses
    if ball.xcor() > 360:
        ball.reset()
        score.lpoint()

    # detect L paddle misses
    if ball.xcor() < -360:
        ball.reset()
        score.rpoint()
        ball.move_speed = 0.1
screen.exitonclick()
