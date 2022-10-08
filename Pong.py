import turtle

win = turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600, starty=10)
win.tracer(0)

title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0,25)
title.write("PONG", align="center", font=("Arial", 50, "normal"))
title.goto(0,-35)
title.write("Press <Space> To Start", align="center", font=("Arial", 15, "normal"))
title.goto(0,-275)
title.write("Press <Q> To Enable Unbeatable AI", align="center", font=("Arial", 10, "normal"))

def game():
    title.clear()

    # Score
    score1 = 0
    score2 = 0

    # Paddle 1
    paddle1 = turtle.Turtle()
    paddle1.speed(0)
    paddle1.shape("square")
    paddle1.color("white")
    paddle1.shapesize(stretch_wid=5, stretch_len=1)
    paddle1.penup()
    paddle1.goto(-350, 0)

    # Paddle 2
    paddle2 = turtle.Turtle()
    paddle2.speed(0)
    paddle2.shape("square")
    paddle2.color("white")
    paddle2.shapesize(stretch_wid=5, stretch_len=1)
    paddle2.penup()
    paddle2.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)

    ball.dx = 0.4
    ball.dy = 0.4

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0,260)
    pen.write("Player 1: 0      Player 2: 0", align="center", font=("Arial", 15, "normal"))

    # Function
    def paddle1_up():
        y = paddle1.ycor()
        y += 20
        paddle1.sety(y)

    def paddle1_down():
        y = paddle1.ycor()
        y -= 20
        paddle1.sety(y)

    def paddle2_up():
        y = paddle2.ycor()
        y += 20
        paddle2.sety(y)

    def paddle2_down():
        y = paddle2.ycor()
        y -= 20
        paddle2.sety(y)

    # Keyboard Binds
    win.listen()
    win.onkeypress(paddle1_up, "w")
    win.onkeypress(paddle1_down, "s")
    
    win.onkeypress(paddle2_up, "Up")
    win.onkeypress(paddle2_down, "Down")

    while True:
        win.update()

        # Move Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            pen.clear()
            pen.write("Player 1: {}      Player 2: {}".format(score1, score2), align="center", font=("Arial", 15, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            pen.clear()
            pen.write("Player 1: {}      Player 2: {}".format(score1, score2), align="center", font=("Arial", 15, "normal"))

        if paddle1.ycor() > 250:
            paddle1.goto(-350, 240)

        if paddle1.ycor() < -250:
            paddle1.goto(-350, -240)

        if paddle2.ycor() > 250:
            paddle2.goto(350, 240)

        if paddle2.ycor() < -250:
            paddle2.goto(350, -240)

        # Paddle and Ball Collision
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
        
        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

# Main Game Loop
while True:
    win.update()
    
    win.listen()
    win.onkeypress(game, "space")