from turtle import*
from sity import*
from turtle import*
def dom():
    penup()
    goto(-90,-90)
    pendown()
    pensize(5)
    begin_fill()
    color('thistle')
    right(25)
    forward(50)
    left(25)
    forward(100)
    left(180)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(180)
    forward(100)
    left(90)
    forward(100)
    right(25)
    forward(50)
    left(115)
    forward(100)
    end_fill()
    left(60)
    forward(50)
    color('pink')
    left(30)        
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    left(90)
    forward(100)
    right(30)
    begin_fill()
    color('burlywood')
    for a in range(3):
        forward(100)
        right(120)
    end_fill()
    left(90)
    color('tan')
    begin_fill()
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    end_fill()

def window():
    goto(-30,-70)
    color('aliceblue')
    begin_fill()
    for w in range(2):
        forward(25)
        left(90)
        forward(20)
        left(90)
    end_fill()
    
def door():
    color('cornsilk')
    begin_fill()
    for e in range(2):
        forward(45)
        left(90)
        forward(60)
        left(90)
    end_fill()

def tree():
    color('sienna')
    begin_fill()
    for q in range(2):
        forward(25)
        left(90)
        forward(70)
        left(90)
    end_fill()
    left(90)
    forward(70)
    right(90)
    begin_fill()
    color('olivedrab')
    circle(60)
    end_fill()

def sun():
    
    color('yellow')
    def p():
        for r in range(3):
            forward(50)
            left(120)
    for y in range (36):
        p()
        left(10)


speed(10)
pensize(5)

color('light blue')
begin_fill()
goto(250,250)
goto(250,-250)
goto(-250,-250)
goto(-250,250)
goto(250,250)
end_fill()

penup()
color('light green')

goto(-250,-250)
pendown()
begin_fill()
goto(-250,0)
goto(250,0)
goto(250,-250)
goto(-250,-250)
end_fill()

dom()

penup()
goto(-30,-70)
pendown()
right(75)

penup()
goto(-190,-90)
pendown()

right(170)
tree()

penup()
goto(100,90)
pendown()
sun()

exitonclick() 
