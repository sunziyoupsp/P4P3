from turtle import *
t = Turtle()
t.speed(0)

def flag(x,y,l, w, color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(2):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)
    t.end_fill()

def lines(width,color):
    t.up()
    t.goto(-200,100)
    t.down()
    t.color(color)
    t.width(width)
    t.goto(0,0)
    t.up()
    t.goto(0,100)
    t.down()
    t.goto(-200,0)

def lines2(width,color):
    t.up()
    t.goto(-200,50)
    t.down()
    t.color(color)
    t.width(width)
    t.goto(0,50)
    t.up()
    t.goto(-100,100)
    t.down()
    t.goto(-100,0)

    
def star5(x,y,size):
    t.up()
    t.goto(x,y)
    t.color('white')
    t.begin_fill()
    t.width(1)
    t.down()
    for i in range(5):
        t.forward(size)
        t.left(72)
        t.forward(size)
        t.right(180-360/10)
    t.end_fill()

def star7(x,y,size):
    t.up()
    t.goto(x,y)
    t.color('white')
    t.begin_fill()
    t.width(1)
    t.down()
    for i in range(7):
        t.forward(size)
        t.left(180-360/14*3)
        t.forward(size)
        t.right(180-360/14)
    t.end_fill()
    
flag(-200,100,400,200,'blue')
lines(15,'white')
lines(5,'red')
lines2(20,'white')
lines2(10,'red')

star5(140,-5,6)
t.right(180)
star7(-100,-50,25)
star7(130,70,10)
star7(130,-70,10)
star7(70,0,10)
star7(180,20,10)


