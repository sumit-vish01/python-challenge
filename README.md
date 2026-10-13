import turtle
import random

screen = turtle.Screen()
screen.title("Catch the coin")
screen.setup(width=600, height=600)
screen.bgcolor("Black")

#-----------------Player----------------

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, 0)

#-----------------Coin-----------

coin = turtle.Turtle()
coin.shape("circle")
coin.color("yellow")
coin.penup()

def move_code():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    coin.goto(x, y)

move_code()

#----------------SCORE----------------

score = 0

score_text = turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(-270, 260)
score_text.write("Score: 0", font=("Arial", 18,"normal"))

#-------------MOvement--------------

def move_up():
    player.sety(player.ycor() + 20)

def move_down():
    player.sety(player.ycor() - 20)

def move_left():
    player.setx(player.xcor() -20)

def move_right():
    player.setx(player.xcor() + 20)


screen.listen()

screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

#--------------Game loop-----------

def check_collision():
    global score

    if player.distance(coin) < 25:
        score += 1

        score_text.clear()
        score_text.write(
            f"Score: {score}", 
            font=("Arial", 18, "normal")
        )

        move_coin()

    screen.ontimer(check_collision, 100)

check_collision()

screen.mainloop()
