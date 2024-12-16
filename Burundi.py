from turtle import *
t = Turtle()
t.speed(0)


#red rectangle
t.up()
t.goto(-250,150)
t.down()
t.color("red")
t.begin_fill()
t.goto(250,150)
t.goto(250,-150)
t.goto(-250,-150)
t.end_fill()

#left green triangle
t.up()
t.goto(-250,150)
t.down()
t.color("green")
t.begin_fill()
t.goto(0,0)
t.goto(-250,-150)
t.end_fill()

#right green triangle
t.up()
t.goto(250,150)
t.down()
t.color("green")
t.begin_fill()
t.goto(0,0)
t.goto(250,-150)
t.end_fill()

#white circle
t.up()
t.goto(0,-85)
t.down()
t.color("white")
t.begin_fill()
t.circle(85)
t.end_fill()

#white line
t.up()
t.goto(-250,150)
t.down()
t.color("white")
t.width(40)
t.goto(250,-150)
t.up()
t.goto(250,150)
t.down()
t.goto(-250,-150)
t.width(1)
t.right(60)

#draw black border
t.up()
t.goto(-250,150)
t.down()
t.color("black")
t.goto(250,150)
t.goto(250,-150)
t.goto(-250,-150)
t.goto(-250,150)


def star(x,y,size,color):
    t.up()
    t.goto(x,y+size/2)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(6):
        t.forward(size/3)
        t.left(60)
        t.forward(size/3)
        t.right(120)
    t.end_fill()

star(0,44,50,"green")
star(0,44,40,"red")
star(-40,-20,50,"green")
star(-40,-20,40,"red")
star(40,-20,50,"green")
star(40,-20,40,"red")


        
    
        

    
        













