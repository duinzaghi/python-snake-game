from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


def start_game():
    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(reset_game, "r")
    screen.onkey(reset_game, "space")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        snake.move()
        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()


def reset_game():
    screen.clear()
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)
    start_game()


# Start the initial game
start_game()

screen.exitonclick()
