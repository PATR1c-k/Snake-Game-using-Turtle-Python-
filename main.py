import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
screen.setup(width=700, height=700)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Todo 1: detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

    # Todo 2: detect collision with the wall
    if snake.head.xcor() > 330 or snake.head.ycor() > 330 or snake.head.xcor() < -330 or snake.head.ycor() < -330:
        game_is_on = False
        scoreboard.game_over()

    # todo Detect collision with the tail
    for segment in snake.segments[1::]:   # here we do list slicing
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
