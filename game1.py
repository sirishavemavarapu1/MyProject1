import turtle
import random
wn=turtle.Screen()
wn.title("First game")
wn.bgcolor("blue")
wn.setup(width=800,height=600)
#wn.tracer(0)
# tracer stops the window to update
score_a=0
score_b=0


#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball=turtle.Turtle()
ball.speed(3)
ball.shape("square")
ball.color("grey")
ball.penup()
ball.dx=random.randint(0,2)
ball.dy=random.randint(0,2)

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A :0       Player B:0" ,align="center",font=30 )


#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=10
    paddle_a.sety(y)

#KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_up,"Up")



def paddle_a_down():
    y=paddle_a.ycor()
    y-=10
    paddle_a.sety(y)

#KEYBOARD BINDING
wn.listen()
wn.onkeypress(paddle_a_down,"Down")

def paddle_b_up():
    y=paddle_b.ycor()
    y+=10
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_up,"a")

def  paddle_b_down():
    y=paddle_b.ycor()
    y-=10
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_down,"z")







while True:
    wn.update()
    # Ball move
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #Border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A :{}       Player B:{}".format(score_a,score_b),align="center",font=30 )
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b +=1
        pen.clear()
        pen.write("Player A :{}       Player B:{}".format(score_a,score_b),align="center",font=30 )
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
    



   




















