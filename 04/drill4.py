from random import randrange
import turtle as t

for i in range(6):
    t.penup()
    t.goto(0,100*i)
    t.pendown()
    t.forward(500)
    pass

t.left(90)
for i in range(6):
    t.penup()
    t.goto(100*i, 0)
    t.pendown()
    t.forward(500)
    pass

t.exitonclick()