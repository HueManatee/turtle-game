
#-----import statements-----
from tkinter import font
import turtle as trl
import random as rand
import time
import myleaderboard as bd
#---Starting game variables
score = 0
timeLeft = 6
countInt = 1000
font_choice = ("Comic Sans MS", 20, "normal")
colors = ('thistle', 'dodgerblue', 'mintcream', 'mediumvioletred','chartreuse','peru', 'olive', 'rosybrown', 'gainsboro', 'orchid', 'papayawhip', 'cadetblue', 'ivory', 'crimson','wheat', 'teal', 'azure', 'slategrey', 'lavender', 'plum', 'gray', 'olivedrab')
challenge = False
name = str(input('What is your name? '))





#title turtle
title = trl.Turtle()
title.penup()
title.speed(0)
title.hideturtle()

title.goto(-100,50)

title.color('pink')
title.write("Catch the Pink Turtle!", font=font_choice)

#wait to start turtle

button = trl.Turtle()

button.speed(0)
button.hideturtle()
button.penup()
button.shapesize(5,5)
button.goto(-150,-50)
button.pendown()
button.color('indigo')
button.write('The game will start in 5 seconds', font=font_choice)

def start():
    global challenge
    button.clear()
    button.penup()
    button.goto(-500,-500)
    title.clear()
    title.penup()
    title.goto(-500,-500)
    #-----game configuration(Init variables)----
    x = rand.randint(-200,200)
    y = rand.randint(-150,150)
    
    
    
    

    #-----initialize turtle for game-----
    #turtle that is clicked
    draw = trl.Turtle()
    draw.shape('turtle')
    draw.shapesize(2,2)
    draw.fillcolor('pink')
    draw.penup()
    draw.speed(0)
    #turtle that draws the score
    scoreWrite = trl.Turtle()
    scoreWrite.speed(0)
    scoreWrite.hideturtle()
    scoreWrite.penup()
    scoreWrite.goto(-50,300)
    scoreWrite.pendown()
    #turtle that draws the countdown
    countdown = trl.Turtle()
    countdown.speed(0)
    countdown.hideturtle()
    countdown.color('red')
    countdown.penup()
    countdown.goto(-50, 200)
    countdown.pendown()

    #-----game functions--------
    def counter():
        global timeLeft
        countdown.clear()
        timeLeft -= 1
        if(timeLeft == 0):
            draw.goto(-500, -500)
            scoreWrite.clear()
            draw.clear()
            gamewn.bgcolor('plum')
            countdown.penup()
            countdown.goto(-400, 200)
            countdown.pendown()

        

            countdown.write(bd.addScore(name,score))
            countdown.penup()
            countdown.goto(-150,0)
            countdown.pendown()
            countdown.write("Time's Up! Your score was " + str(score) + '.', font=font_choice)
        else:
            countdown.write("Time Left: " + str(timeLeft), font=font_choice)
            countdown.getscreen().ontimer(counter, countInt) 


    def moveTurtle(x,y):
        draw.goto(x, y)
    def updateScore():
        global score
        score += 1
        scoreWrite.write("Score: " + str(score), font=font_choice)

    def checkClick(x,y):
        global timeLeft, challenge
        #print(x,y)
        timeLeft = 6
        scoreWrite.clear()
        updateScore()
        draw.fillcolor(colors[rand.randint(0,(len(colors) - 1))])
        draw.stamp()
        if(challenge == True):
            draw.fillcolor('pink')
        newx = rand.randint(-400,400)
        newy = rand.randint(-300,300)
        moveTurtle(newx,newy)
    #-----events----------------
    moveTurtle(x,y)
    draw.onclick(checkClick)
    # game screen timer check and loop
    gamewn = trl.Screen()
    gamewn.ontimer(counter, countInt)
    gamewn.mainloop()
#-------title screen loop--------


time.sleep(5)
start()

titlewn = trl.Screen()
titlewn.mainloop()








