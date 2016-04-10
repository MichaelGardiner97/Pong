# Michael Gardiner
# Due: 12-8-15
# Lab 11 Purpose: Virtual game of Pong
# Bonus: -Improved Design (Background, Scoreboard, Countdown)
#        -Paddle Shrinks Over Time
#        -Play With Multiple Balls
#        -Play Again Function

from time import sleep
from random import randrange, random
from graphics import *
from Ball import Ball
from Paddle import Paddle

class Pong:

    def __init__(self):
        
        w = 500
        h = 500
        self.pWin = GraphWin("Pong", w, h )
        myIMG = Image(Point(250, 250), "linesfinished.gif")
        myIMG.draw(self.pWin)
        self.b = Ball(self.pWin)
        self.p = Paddle(self.pWin)
        self.hits = 0
        self.score = 0
        self.level = 1
        
        self.scoreTitle = Text(Point(350, 25), "Score:")
        self.scoreTitle.setTextColor("white")
        self.scoreTitle.setSize(25)
        
        self.userScore = Text(Point(405, 25), self.score)
        self.userScore.setTextColor("white")
        self.userScore.setSize(25)
        
        self.levelTitle = Text(Point(100, 25), "Level:")
        self.levelTitle.setTextColor("white")
        self.levelTitle.setSize(25)
        
        self.userLevel = Text(Point(150, 25), self.level)
        self.userLevel.setTextColor("white")
        self.userLevel.setSize(25)
        
        self.scoreTitle.draw(self.pWin)
        self.userScore.draw(self.pWin)
        self.levelTitle.draw(self.pWin)
        self.userLevel.draw(self.pWin)

    def checkContact(self):
        
        xMiddle = self.p.getMiddle().getX()
        xPadLeft = xMiddle - 5
        xPadRight = xMiddle + 5
        xCenter = self.b.getCenter().getX()
        xBallRight = xCenter + self.b.getRadius()
        xBallLeft = xCenter - self.b.getRadius()

        yMiddle = self.p.getMiddle().getY()
        yPadTop = yMiddle - 50
        yPadBottom = yMiddle + 50
        yCenter = self.b.getCenter().getY()
        yBallTop = yCenter - self.b.getRadius()
        yBallBottom = yCenter + self.b.getRadius()

#       If the x value of right side of the ball is = to the x value of the left side of the paddle,
#       and the y value of the top/bottom of the ball is not outside the y value of the top/bottom of the paddle,
#       then the ball has made contact

        if (xBallRight >= xPadLeft and yBallBottom >= yPadTop) and (xBallRight >= xPadLeft and yBallTop <= yPadBottom):
            self.hits += 1
            self.score += 1
            self.userScore.setText(self.score)
            if self.hits % 2 == 0:
                self.level += 1
                self.userLevel.setText(self.level)
                self.b.goFaster()

                if self.level % 4 == 0:
                    self.tier = Text(Point(250, 250), "You have reached a new tier")
                    self.tier.setTextColor("red")
                    self.tier.setSize(20)
                    self.tier.draw(self.pWin)
                    self.wow = Text(Point(250, 81), "WOW!")
                    self.wow.setSize(30)
                    self.wow.setTextColor("red")
                    self.wow.draw(self.pWin)
                    sleep(3)
                    self.tier.undraw()
                    self.wow.undraw()

            return True
        else:
            return False          


    def checkContactShrink(self):
        
        xMiddle = self.p.getMiddle().getX()
        xPadLeft = xMiddle - 5
        xPadRight = xMiddle + 5
        xCenter = self.b.getCenter().getX()
        xBallRight = xCenter + self.b.getRadius()
        xBallLeft = xCenter - self.b.getRadius()

        yMiddle = self.p.getMiddle().getY()
        yPadTop = yMiddle - 50
        yPadBottom = yMiddle + 50
        yCenter = self.b.getCenter().getY()
        yBallTop = yCenter - self.b.getRadius()
        yBallBottom = yCenter + self.b.getRadius()

#       If the x value of right side of the ball is = to the x value of the left side of the paddle,
#       and the y value of the top/bottom of the ball is not outside the y value of the top/bottom of the paddle,
#       then the ball has made contact

        if (xBallRight >= xPadLeft and yBallBottom >= yPadTop) and (xBallRight >= xPadLeft and yBallTop <= yPadBottom):
            self.hits += 1
            self.score += 1
            self.userScore.setText(self.score)
            if self.hits % 2 == 0:
                self.level += 1
                self.userLevel.setText(self.level)
                self.b.goFaster()
                
#               Undraw the original Paddle, and Replace with new, smaller Paddle
                self.p.pad.undraw()
                self.p.newRectangle(self.hits*4)
                self.p.pad.draw(self.pWin)

                if self.level % 4 == 0:
                    self.tier = Text(Point(250, 250), "You have reached a new tier")
                    self.tier.setTextColor("red")
                    self.tier.setSize(20)
                    self.tier.draw(self.pWin)
                    self.wow = Text(Point(250, 81), "WOW!")
                    self.wow.setSize(30)
                    self.wow.setTextColor("red")
                    self.wow.draw(self.pWin)
                    sleep(3)
                    self.tier.undraw()
                    self.wow.undraw()

            return True
        else:
            return False
        
#   First Ball Used for Multiple-Ball Pong
    def checkContactBallA(self):
        
        xMiddle = self.p.getMiddle().getX()
        xPadLeft = xMiddle - 5
        xPadRight = xMiddle + 5
        xCenter = self.b.getCenter().getX()
        xBallRight = xCenter + self.b.getRadius()
        xBallLeft = xCenter - self.b.getRadius()
        
        yMiddle = self.p.getMiddle().getY()
        yPadTop = yMiddle - 50
        yPadBottom = yMiddle + 50
        yCenter = self.b.getCenter().getY()
        yBallTop = yCenter - self.b.getRadius()
        yBallBottom = yCenter + self.b.getRadius()
        

#       If the x value of right side of the ball is = to the x value of the left side of the paddle,
#       and the y value of the top/bottom of the ball is not outside the y value of the top/bottom of the paddle,
#       then the ball has made contact

        
        if (xBallRight >= xPadLeft and yBallBottom >= yPadTop) and (xBallRight >= xPadLeft and yBallTop <= yPadBottom):
            self.hits += 1
            self.score += 1
            self.userScore.setText(self.score)
            if self.hits % 4 == 0:
                self.level += 1
                self.userLevel.setText(self.level)
                self.b.goFaster()
                
                if self.level % 10 == 0:
                    self.tier = Text(Point(250, 250), "You have reached a new tier")
                    self.tier.setTextColor("red")
                    self.tier.setSize(20)
                    self.tier.draw(self.pWin)
                    self.wow = Text(Point(250, 81), "WOW!")
                    self.wow.setSize(30)
                    self.wow.setTextColor("red")
                    self.wow.draw(self.pWin)
                    sleep(3)
                    self.tier.undraw()
                    self.wow.undraw()

            return True
        else:
            return False
        
#   Second Ball Used for Multiple-Ball Pong
    def checkContactBallB(self):

        xMiddle = self.p.getMiddle().getX()
        xPadLeft = xMiddle - 5
        xPadRight = xMiddle + 5
        xCenter2 = self.b.getCenter2().getX()
        xBallRight2 = xCenter2 + self.b.getRadius2()
        xBallLeft2 = xCenter2 - self.b.getRadius2()

        yMiddle = self.p.getMiddle().getY()
        yPadTop = yMiddle - 50
        yPadBottom = yMiddle + 50
        yCenter2 = self.b.getCenter2().getY()
        yBallTop2 = yCenter2 - self.b.getRadius2()
        yBallBottom2 = yCenter2 + self.b.getRadius2()
        
#       If the x value of right side of the ball is = to the x value of the left side of the paddle,
#       and the y value of the top/bottom of the ball is not outside the y value of the top/bottom of the paddle,
#       then the ball has made contact

        
        if (xBallRight2 >= xPadLeft and yBallBottom2 >= yPadTop) and (xBallRight2 >= xPadLeft and yBallTop2 <= yPadBottom):
            self.hits += 1
            self.score += 1
            self.userScore.setText(self.score)
            if self.hits % 4 == 0:
                self.level += 1
                self.userLevel.setText(self.level)
                self.b.goFaster()

                if self.level % 3 == 0:
                    self.tier = Text(Point(250, 250), "You have reached a new tier")
                    self.tier.setTextColor("red")
                    self.tier.setSize(20)
                    self.tier.draw(self.pWin)
                    self.wow = Text(Point(250, 81), "WOW!")
                    self.wow.setSize(30)
                    self.wow.setTextColor("red")
                    self.wow.draw(self.pWin)
                    sleep(3)
                    self.tier.undraw()
                    self.wow.undraw()

            return True
        else:
            return False
        
    def gameOver(self):
#       If the ball goes past the paddle, the game is over and the user is asked to play again

        xCenter = self.b.getCenter().getX()
        xBallLeft = xCenter - self.b.getRadius()

        xCenter2 = self.b.getCenter2().getX()
        xBallLeft2 = xCenter2 - self.b.getRadius2()

        xMiddle = self.p.getMiddle().getX()
        xPadRight = xMiddle + 5
        
        if (xBallLeft > xPadRight) or (xBallLeft2 > xPadRight):
            loser = Text(Point(250, 150), "GAME OVER!")
            loser.setSize(25)
            loser.setTextColor("red")
            
            again = Text(Point(250, 200), "PLAY AGAIN?")
            again.setSize(25)
            again.setTextColor("red")

            loser.draw(self.pWin)
            again.draw(self.pWin)

            return True

    def restart(self):
#       If the player types 'yes', the game will restart completely
        
        restart = input("\nWould You Like To Restart (yes/no)? ")
        if restart.lower() == "yes":
            self.pWin.close()
            newGame = Pong()
            print("WARNING!! IN SHRINKING MODE, PADDLE RESETS TO MIDDLE AFTER EACH LEVEL")       
            game = input("Which version would you like to play: 'shrinking mode' (s), 'multiple mode' (m), or 'normal mode' (n)? ")
            newGame.play(game)
        else:
            self.pWin.close()
       
    def play(self, ans):
#       The user will be given 3 seconds after asked to play until the game begins

        sleep(1)

        self.ready = Text(Point(250, 81), "Are You Ready?")
        self.ready.setSize(30)
        self.ready.setTextColor("red")
        self.ready.draw(self.pWin)
        
        self.three = Text(Point(250, 200), "THREE")
        self.three.setSize(35)
        self.three.setTextColor("white")
        self.three.draw(self.pWin)
        sleep(1)
        self.three.undraw()

        self.two = Text(Point(250, 200), "TWO")
        self.two.setSize(35)
        self.two.setTextColor("white")
        self.two.draw(self.pWin)
        sleep(1)
        self.two.undraw()

        self.one = Text(Point(250, 200), "ONE")
        self.one.setSize(35)
        self.one.setTextColor("white")
        self.one.draw(self.pWin)
        sleep(1)
        self.one.undraw()

        self.ready.undraw()
        while True:
            click = self.pWin.checkMouse()
            if click != None:
                self.p.movePad(click)
            if ans.lower() == 's':
                if self.checkContactShrink():
                    self.b.reverseX()
            elif ans.lower() == 'm':
                if self.checkContactBallA():
                    self.b.reverseX()
                if self.checkContactBallB():
                    self.b.reverse2X()
                self.b.moveBall2(self.pWin)
            elif ans.lower() == 'n':
                if self.checkContact():
                    self.b.reverseX()
            else:
                print("\nOh Well, I Didn't Want To Play With You Anyway!")
            self.b.moveBall(self.pWin)
            if self.gameOver():
                self.restart()
    
def main():

    instructions = input("Welcome To Pong! Would You Like Instructions (yes/no)? ") 
    warning = "WARNING!! IN SHRINKING MODE, PADDLE RESETS TO MIDDLE AFTER EACH LEVEL"
    if instructions.lower() == 'yes':
        start = input("The Instructions Are Simple; Don't Let The Ball Hit The Wall Behind Your Paddle!\nIf You Are You Ready, Enter 'Yes' And Move This Window: ")
        if start.lower() == 'yes':
            print(warning)
            game = input("Which version would you like to play: 'shrinking mode' (s), 'multiple mode' (m), or 'normal mode' (n)? ")
            newGame = Pong()
            newGame.play(game)
        else:
            print("\nOh Well, I Didn't Want To Play With You Anyway!")
    else:
        start = input("If You Are You Ready, Enter 'Yes' And Move This Window: ")
        if start.lower() == 'yes':
            print(warning)
            game = input("Which version would you like to play: 'shrinking paddle' (s), 'multiple balls' (m), or 'normal mode' (n)? ")
            newGame = Pong()
            newGame.play(game)
        else:
            print("\nOh Well, I Didn't Want To Play With You Anyway!")

main()
