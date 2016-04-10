from time import sleep
from random import randrange, random
from graphics import *

colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']

class Ball:
    def __init__(self, win):
        center = Point(40, 200)
        center2 = Point(100, 50)
        self.ball = Circle(center, 20)
        self.ball.setFill("yellow")
        self.ball.draw(win)
        self.newB = self.ball.clone()
        self.newB.setFill("purple")
        self.newB.draw(win)
        self.dx = randrange(2,5)
        self.dy = randrange(2,5)
        self.dx2 = randrange(2,5)
        self.dy2 = randrange(2,5)
                  
    def getCenter(self):
        ball1 = self.ball.getCenter()
        return ball1

    def getCenter2(self):
        ball2 = self.newB.getCenter()
        return ball2
                        
    def getRadius(self):
        ball1 = self.ball.getRadius() 
        return ball1

    def getRadius2(self):
        ball2 =  self.newB.getRadius()
        return ball2

    def goFaster(self):
        self.dx = self.dx * (random() + 1)
        self.dy = self.dy * (random() + 1)
        self.dx2 = self.dx2 * (random() + 1)
        self.dy2 = self.dy2 * (random() + 1)

    def reverseX(self):
        self.dx = self.dx * -1

    def reverse2X(self):
        self.dx2 = self.dx2 * -1

    def reverseY(self):
        self.dy = self.dy * -1

    def reverse2Y(self):
        self.dy2 = self.dy2 * -1

    def moveBall(self, win):
        if self.getCenter().getX() - self.getRadius() <= 0:
            self.reverseX()
        if self.getCenter().getY() + self.getRadius() >= 500:
            self.reverseY()
        if self.getCenter().getY() - self.getRadius() <= 0:
            self.reverseY()

        self.ball.move(self.dx,self.dy)

    def moveBall2(self, win):           
        if self.getCenter2().getX() - self.getRadius2() <= 0:
            self.reverse2X()
        if self.getCenter2().getY() + self.getRadius2() >= 500:
            self.reverse2Y()
        if self.getCenter2().getY() - self.getRadius2() <= 0:
            self.reverse2Y()
            
        self.newB.move(self.dx2,self.dy2)
        
