import turtle as t
import random as r

moveSpeed = 50
def GoHome():
    t.penup()
    t.home()
    t.pendown()
    pass

def Move(radius):
    t.setheading(radius)
    t.stamp()
    t.forward(moveSpeed)
    pass

def Move_W() : Move(90)
def Move_S() : Move(-90)
def Move_A() : Move(180)
def Move_D() : Move(0)

def KeySetting():
    t.onkey(Move_W,'w')
    t.onkey(Move_S,'s')
    t.onkey(Move_A,'a')
    t.onkey(Move_D,'d')
    t.onkey(t.reset,'Escape')
    t.onkey(GoHome,' ')

    t.listen()
    pass

def Update():
    t.shape('turtle')
    KeySetting()
    while True:
        cmd = input()
        if cmd == 'q':
            break;

Update()