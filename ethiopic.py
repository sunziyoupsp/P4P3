from turtle import *
t = Turtle()
t.speed(0)

def rectangle(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    t.goto(x+600,y)
    t.goto(x+600,y+100)
    t.goto(x,y+100)
    t.goto(x,y)
    t.end_fill()

def circle(x,y,r,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def star(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.width(10)
    for i in range(5):
        t.forward(130)
        t.right(144)
    
def line():
    t.up()
    t.goto(0,0)
    t.width(8)
    t.right(90)
    for i in range(5):
        t.right(72)
        t.forward(50)
        t.down()
        t.forward(40)
        t.up()
        t.backward(90)
        

rectangle(-300,-150,"red")
rectangle(-300,-50,"yellow")
rectangle(-300,50,"green")
circle(0,-100,100,"blue")
star(-65,25,"yellow")
line()
