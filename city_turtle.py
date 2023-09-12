from turtle import*
from sity import*
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
