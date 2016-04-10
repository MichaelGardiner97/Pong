from time import sleep
from random import randrange, random
from graphics import *

class Paddle:

    def __init__(self, win):
        self.xp1 = 450
        self.yp1 = 200
        self.xp2 = 460
        self.yp2 = 300
        self.pad = Rectangle(Point(self.xp1,self.yp1), Point(self.xp2, self.yp2))        
        self.pad.setFill("red")
        self.pad.setOutline("black")
        self.pad.draw(win)
        self.dx = 450
        
    def getMiddle(self):
        return self.pad.getCenter()

    def getLen(self):
        length = abs(self.yP1 - self.yP2)
        return length

    def newRectangle(self, num):
        self.pad = Rectangle(Point(self.xp1,self.yp1+num), Point(self.xp2, self.yp2))        
        self.pad.setFill("red")
        self.pad.setOutline("black")
        return self.pad
    
    def getStart(self):
        self.point = self.pad.getP1()
        self.xEdge = self.point.getX()
        self.yEdge = self.point.getY()
        return (self.xEdge, self.yEdge)

    def getEnd(self):
        self.end = self.pad.getP2()
        self.xEnd = self.end.getX()
        self.yEnd = self.end.getY()
        return (self.xEnd, self.yEnd)

    def movePad(self, pt):
        yCord = pt.getY()
        self.dy = yCord - self.pad.getCenter().getY()
        
        self.pad.move(0, self.dy)


