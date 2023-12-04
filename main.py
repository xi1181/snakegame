import turtle
import time
from Snake import Snake
from Food import Food
from score import Score

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.w, "w")
screen.onkey(snake.s, "s")
screen.onkey(snake.a, "a")
screen.onkey(snake.d, "d")

def quit():
    with open("highscore.txt") as file:
        prev_high_score = int(file.read())

    if (score.high_score > prev_high_score):
        with open("highscore.txt", "w") as file:
            file.write(str(score.high_score))

    if (score.score > prev_high_score):
        with open("highscore.txt", "w") as file:
            file.write(str(score.score))

    turtle.bye()

screen.onkey(quit, "q")

while True:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        snake.extend()
        food.reposition()
        score.add_score()

    if snake.head.xcor() < -280:
        snake.head.setx(280)
    elif snake.head.xcor() > 280:
        snake.head.setx(-280)
    elif snake.head.ycor() < -280:
        snake.head.sety(280)
    elif snake.head.ycor() > 280:
        snake.head.sety(-280)

    for segment in snake.segments:
        if segment == snake.head:
            continue
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


     

screen.exitonclick()

